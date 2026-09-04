<#
revisar_modelo_nwd.ps1 - Extrae el contenido del entregable 3D .nwd usando
Navisworks Manage, para poder revisarlo de verdad y no solo acusar recibo.

ESTE ARCHIVO ES ASCII PURO A PROPOSITO. PowerShell 5.1 lee un .ps1 sin BOM en la
codepage ANSI del sistema. Un em-dash en UTF-8 termina en el byte 0x94, que en
cp1252 decodifica como comilla tipografica de cierre, y PowerShell SI la acepta
como delimitador de cadena: cierra el string antes de tiempo y todo lo que sigue
cae en modo expresion, con errores que apuntan a lineas equivocadas. No
introducir tildes, enes ni em-dashes aqui.

POR QUE ESTE CAMINO Y NO OTRO (los tres se probaron, en este orden):

  1. COM (ProgID Navisworks.Document). ABRE el archivo, pero el objeto es un
     proxy de .NET Remoting sin type library reflejable, y no puebla el
     Application.ActiveDocument de la API .NET. Sirve para abrir, no para leer.

  2. Automation API (Autodesk.Navisworks.Api.Automation.NavisworksApplication).
     OJO con el nombre: lleva `.Api.` en medio. Su superficie es de nivel
     ARCHIVO -- OpenFile, SaveFile, AppendFile, Print, CreateCache -- y no
     expone el arbol del modelo. SaveFile solo acepta .nwf en este contexto:
     los exportadores a FBX, DWFx, DAE y KMZ no estan cargados fuera de la UI.

  3. Plugin in-process via AddPluginAssembly + ExecuteAddInPlugin. Es la unica
     via que corre CON la API completa dentro de Roamer. El plugin se compila al
     vuelo con Add-Type contra Autodesk.Navisworks.Api.dll y se carga en la
     instancia automatizada, sin escribir nada en Program Files.

Uso:
    powershell -NoProfile -ExecutionPolicy Bypass -File revisar_modelo_nwd.ps1
#>
[CmdletBinding()]
param(
    [string]$Nwd = "V14 Taltal.nwd",
    [string]$OutDir = "md",
    [int]$MaxNodos = 20000
)

$ErrorActionPreference = "Stop"
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not [System.IO.Path]::IsPathRooted($Nwd)) { $Nwd = Join-Path $base $Nwd }
if (-not [System.IO.Path]::IsPathRooted($OutDir)) { $OutDir = Join-Path $base $OutDir }
if (-not (Test-Path $Nwd)) { Write-Output "ERROR: no existe $Nwd"; exit 1 }
if (-not (Test-Path $OutDir)) { New-Item -ItemType Directory -Path $OutDir -Force | Out-Null }

$nwRoot = "C:\Program Files\Autodesk\Navisworks Manage 2026"
$apiDll = Join-Path $nwRoot "Autodesk.Navisworks.Api.dll"
$autDll = Join-Path $nwRoot "Autodesk.Navisworks.Automation.dll"
foreach ($d in @($apiDll, $autDll)) { if (-not (Test-Path $d)) { Write-Output "ERROR: falta $d"; exit 1 } }

$mb = [math]::Round((Get-Item $Nwd).Length / 1MB, 2)
$outMd = Join-Path $OutDir "P22-DWG-09-005-007_3D-Model_RevA_extraccion.md"
Write-Output "== Modelo: $Nwd ($mb MB)"

# ---------------------------------------------------------------- plugin C#
$cs = @'
using System;
using System.IO;
using System.Text;
using System.Collections.Generic;
using Autodesk.Navisworks.Api;
using Autodesk.Navisworks.Api.Plugins;

namespace AdasaNwd
{
    [Plugin("AdasaDump", "ADASA", DisplayName = "ADASA Dump", ToolTip = "Volcado de revision")]
    public class Dump : AddInPlugin
    {
        StringBuilder sb = new StringBuilder();
        StringBuilder csv = new StringBuilder();
        StringBuilder muestra = new StringBuilder();
        int nodos = 0;
        int maxNodos = 20000;

        void W(string s) { sb.AppendLine(s); }

        static string Csv(string s)
        {
            if (s == null) return "";
            s = s.Replace("\r", " ").Replace("\n", " ");
            return (s.IndexOf('"') >= 0 || s.IndexOf(',') >= 0)
                ? "\"" + s.Replace("\"", "\"\"") + "\"" : s;
        }

        static string Val(DataProperty p)
        {
            try { return p.Value.ToDisplayString(); } catch { return ""; }
        }

        // Busca el valor de una propiedad por nombre dentro de una categoria.
        static string Prop(ModelItem it, string cat, string prop)
        {
            foreach (PropertyCategory pc in it.PropertyCategories)
            {
                if (!string.Equals(pc.DisplayName, cat, StringComparison.OrdinalIgnoreCase)) continue;
                foreach (DataProperty p in pc.Properties)
                    if (string.Equals(p.DisplayName, prop, StringComparison.OrdinalIgnoreCase))
                        return Val(p);
            }
            return "";
        }

        void Walk(ModelItem it, int depth)
        {
            if (nodos >= maxNodos) return;
            nodos++;
            string nm = it.DisplayName;
            if (string.IsNullOrEmpty(nm)) nm = "(sin nombre)";
            W(new string(' ', depth * 2) + "- [" + it.ClassDisplayName + "] " + nm);
            foreach (ModelItem c in it.Children) Walk(c, depth + 1);
        }

        public override int Execute(params string[] parameters)
        {
            string outPath = (parameters != null && parameters.Length > 0)
                ? parameters[0] : Path.Combine(Path.GetTempPath(), "nwdump.md");
            if (parameters != null && parameters.Length > 1)
                int.TryParse(parameters[1], out maxNodos);

            // Centinela: prueba que el cuerpo del plugin corrio de verdad. Sin el,
            // un ExecuteAddInPlugin que devuelve 0 sin haber encontrado el plugin
            // es indistinguible de una ejecucion exitosa.
            string sentinela = Path.Combine(Path.GetTempPath(), "adasa_nwd_sentinela.txt");
            try
            {
                File.WriteAllText(sentinela,
                    "plugin ejecutado " + DateTime.Now.ToString("s")
                    + Environment.NewLine + "params=" + (parameters == null ? "null" : parameters.Length.ToString())
                    + Environment.NewLine + "outPath=" + outPath + Environment.NewLine);
            }
            catch { }

            Document doc = Autodesk.Navisworks.Api.Application.ActiveDocument;
            if (doc == null)
            {
                File.WriteAllText(outPath, "ActiveDocument nulo dentro del plugin.", new UTF8Encoding(false));
                return 1;
            }

            W("# Modelo 3D `P22-DWG-09-005-007` Rev A - extraccion tecnica");
            W("");
            W("> Generado por `revisar_modelo_nwd.ps1` mediante un plugin in-process de Navisworks Manage 2026. Registro interno de revision, no se envia.");
            W("");
            W("## Metadatos");
            W("");
            W("| Campo | Valor |");
            W("|---|---|");
            W("| Titulo | " + doc.Title + " |");
            W("| Unidades | " + doc.Units + " |");
            W("| Modelos agregados | " + doc.Models.Count + " |");
            try { W("| Es cache de archivo | " + doc.IsClear.ToString() + " |"); } catch { }
            W("");

            W("## Archivos fuente agregados");
            W("");
            W("De que esta hecho el modelo federado y con que herramienta se genero cada parte.");
            W("");
            W("| # | Archivo fuente | Archivo original | Creador | Unidades |");
            W("|---|---|---|---|---|");
            int i = 0;
            foreach (Model m in doc.Models)
            {
                i++;
                string fn = "", src = "", cr = "";
                try { fn = m.FileName; } catch { }
                try { src = m.SourceFileName; } catch { }
                try { cr = m.Creator; } catch { }
                W("| " + i + " | " + fn + " | " + src + " | " + cr + " | " + m.Units + " |");
            }
            W("");

            // Metadatos de publicacion del NWD. Un entregable For Approval deberia
            // declarar autor, fecha y destinatario; si viene vacio, es hallazgo de
            // calidad documental, no de ingenieria.
            W("## Propiedades de publicacion del NWD");
            W("");
            W("| # | Titulo | Autor | Publicado por | Fecha de publicacion | Publicado para | Asunto | Expira | Permite resave | Ya resaveado | Con clave |");
            W("|---|---|---|---|---|---|---|---|---|---|---|");
            i = 0;
            foreach (Model m in doc.Models)
            {
                i++;
                try
                {
                    PublishProperties pp = m.PublishProperties;
                    string exp = pp.HasExpiryDate ? pp.ExpiryDate.ToString("yyyy-MM-dd") : "no";
                    W("| " + i + " | " + pp.Title + " | " + pp.Author + " | " + pp.Publisher + " | "
                      + pp.PublishDate.ToString("yyyy-MM-dd HH:mm") + " | " + pp.PublishedFor + " | "
                      + pp.Subject + " | " + exp + " | " + pp.AllowResave + " | "
                      + pp.HasBeenResaved + " | " + pp.HasPassword + " |");
                    if (!string.IsNullOrEmpty(pp.Comments))
                    {
                        W("");
                        W("Comentarios del modelo " + i + ": " + pp.Comments.Replace("\r\n", " ").Replace("\n", " "));
                    }
                }
                catch (Exception ex) { W("| " + i + " | (sin propiedades de publicacion: " + ex.Message + ") | | | | | | | | | |"); }
            }
            W("");

            W("## Conjuntos de seleccion declarados");
            W("");
            var sets = doc.SelectionSets.ToSavedItemCollection();
            if (sets.Count == 0)
                W("**Ninguno.** El modelo no declara conjuntos de seleccion, de modo que no trae estructura propia de disciplinas ni grupos entre los que correr interferencias.");
            else
                foreach (var s in sets) W("- " + s.DisplayName);
            W("");

            W("## Viewpoints guardados");
            W("");
            var vps = doc.SavedViewpoints.ToSavedItemCollection();
            if (vps.Count == 0)
                W("**Ninguno.** El modelo no trae vistas guardadas, de modo que no propone puntos de revision.");
            else
                foreach (var v in vps) W("- " + v.DisplayName);
            W("");

            W("## Arbol del modelo");
            W("");
            W("```");
            foreach (Model m in doc.Models) Walk(m.RootItem, 0);
            W("```");
            W("");
            W("Nodos recorridos: **" + nodos + "**" + (nodos >= maxNodos ? " (truncado en " + maxNodos + ")" : "") + ".");
            W("");

            W("## Categorias de propiedad presentes");
            W("");
            W("De aqui salen los TAG, materiales y diametros que el modelo declara; es lo que se cruza contra el Piping Layout y el P&ID.");
            W("");
            var cats = new Dictionary<string, HashSet<string>>();
            var ejemplos = new Dictionary<string, string>();
            int cnt = 0;
            foreach (Model m in doc.Models)
            {
                foreach (ModelItem it in m.RootItem.DescendantsAndSelf)
                {
                    cnt++;
                    if (cnt > 6000) break;
                    foreach (PropertyCategory pc in it.PropertyCategories)
                    {
                        string k = pc.DisplayName;
                        if (!cats.ContainsKey(k)) cats[k] = new HashSet<string>();
                        foreach (DataProperty p in pc.Properties)
                        {
                            cats[k].Add(p.DisplayName);
                            string key = k + "|" + p.DisplayName;
                            if (!ejemplos.ContainsKey(key))
                            {
                                try
                                {
                                    string v = p.Value.ToDisplayString();
                                    if (!string.IsNullOrEmpty(v) && v.Length < 60) ejemplos[key] = v;
                                }
                                catch { }
                            }
                        }
                    }
                }
                if (cnt > 6000) break;
            }
            W("| Categoria | Propiedades | Ejemplo de valor |");
            W("|---|---|---|");
            var keys = new List<string>(cats.Keys);
            keys.Sort();
            foreach (string k in keys)
            {
                var props = new List<string>(cats[k]);
                props.Sort();
                string lst = string.Join(", ", props.ToArray());
                if (lst.Length > 260) lst = lst.Substring(0, 260) + " ...";
                string ej = "";
                foreach (string p in props)
                {
                    string key = k + "|" + p;
                    if (ejemplos.ContainsKey(key)) { ej = p + " = " + ejemplos[key]; break; }
                }
                W("| " + k + " | " + lst + " | " + ej + " |");
            }
            W("");
            W("Items inspeccionados: **" + Math.Min(cnt, 6000) + "**.");
            W("");

            // ============================================================
            // VOLCADO DE METADATA POR OBJETO
            // El TAG de linea NO se toma del nombre de capa: se toma de la
            // propiedad del objeto. Que campo la lleva no se asume, se mira:
            // por eso primero va una muestra completa de los primeros objetos
            // que traen categoria AutoCAD, con TODAS sus propiedades.
            // ============================================================
            csv.AppendLine("idx,tipo,nombre,capa,categoria,propiedad,valor");
            int idx = 0, conAutoCAD = 0, muestras = 0, filas = 0;
            foreach (Model m in doc.Models)
            {
                foreach (ModelItem it in m.RootItem.DescendantsAndSelf)
                {
                    idx++;
                    string capa = Prop(it, "Elemento", "Capa");
                    if (string.IsNullOrEmpty(capa)) capa = Prop(it, "General", "Layer");
                    string nom = it.DisplayName == null ? "" : it.DisplayName;
                    string tipo = it.ClassDisplayName == null ? "" : it.ClassDisplayName;

                    bool tieneAC = false;
                    foreach (PropertyCategory pc in it.PropertyCategories)
                        if (string.Equals(pc.DisplayName, "AutoCAD", StringComparison.OrdinalIgnoreCase))
                        { tieneAC = true; break; }
                    if (tieneAC) conAutoCAD++;

                    // Muestra: los primeros 6 objetos con categoria AutoCAD, completos.
                    if (tieneAC && muestras < 6)
                    {
                        muestras++;
                        muestra.AppendLine("");
                        muestra.AppendLine("### Objeto " + idx + " - " + tipo + " - " + (nom == "" ? "(sin nombre)" : nom));
                        muestra.AppendLine("");
                        muestra.AppendLine("| Categoria | Propiedad | Valor |");
                        muestra.AppendLine("|---|---|---|");
                        foreach (PropertyCategory pc in it.PropertyCategories)
                            foreach (DataProperty p in pc.Properties)
                            {
                                string v = Val(p);
                                if (string.IsNullOrEmpty(v)) continue;
                                if (v.Length > 90) v = v.Substring(0, 90) + "...";
                                muestra.AppendLine("| " + pc.DisplayName + " | " + p.DisplayName + " | " + v + " |");
                            }
                    }

                    // CSV largo: una fila por propiedad NO vacia de las categorias
                    // que pueden portar identidad de ingenieria.
                    foreach (PropertyCategory pc in it.PropertyCategories)
                    {
                        string cn = pc.DisplayName == null ? "" : pc.DisplayName;
                        bool interesa =
                            cn.Equals("AutoCAD", StringComparison.OrdinalIgnoreCase) ||
                            cn.Equals("Elemento", StringComparison.OrdinalIgnoreCase) ||
                            cn.Equals("General", StringComparison.OrdinalIgnoreCase) ||
                            // Por prefijo, no por igualdad: la categoria se llama
                            // "Descripcion" con tilde en el modelo, y este archivo es
                            // ASCII puro a proposito (ver cabecera).
                            cn.StartsWith("Descrip", StringComparison.OrdinalIgnoreCase) ||
                            cn.Equals("Text", StringComparison.OrdinalIgnoreCase);
                        if (!interesa) continue;
                        foreach (DataProperty p in pc.Properties)
                        {
                            string v = Val(p);
                            if (string.IsNullOrEmpty(v)) continue;
                            csv.AppendLine(idx + "," + Csv(tipo) + "," + Csv(nom) + "," + Csv(capa) + ","
                                           + Csv(cn) + "," + Csv(p.DisplayName) + "," + Csv(v));
                            filas++;
                        }
                    }
                }
            }

            W("## Metadata de objeto");
            W("");
            W("Objetos recorridos: **" + idx + "**. Con categoria `AutoCAD`: **" + conAutoCAD + "**. "
              + "Filas volcadas al CSV: **" + filas + "**.");
            W("");
            W("El CSV acompana a este archivo con el sufijo `_propiedades.csv`, en formato largo "
              + "(una fila por propiedad), para pivotarlo y cruzarlo contra los listados aprobados.");
            W("");
            W("## Muestra completa de objetos con categoria AutoCAD");
            W("");
            W("Todas las propiedades no vacias de los primeros seis objetos que la traen. Sirve para "
              + "ver que campo porta realmente el TAG antes de asumir su nombre.");
            W(muestra.ToString());

            File.WriteAllText(outPath, sb.ToString(), new UTF8Encoding(false));
            string csvPath = Path.ChangeExtension(outPath, null) + "_propiedades.csv";
            File.WriteAllText(csvPath, csv.ToString(), new UTF8Encoding(false));
            return 0;
        }
    }
}
'@

$dll = Join-Path $env:TEMP "AdasaNwdDump.dll"
if (Test-Path $dll) { Remove-Item $dll -Force -ErrorAction SilentlyContinue }
Write-Output "== Compilando el plugin"
try {
    Add-Type -TypeDefinition $cs -ReferencedAssemblies @($apiDll) -OutputAssembly $dll -OutputType Library -Language CSharp
    Write-Output "   compilado: $dll"
} catch {
    Write-Output ("   FALLO al compilar: " + $_.Exception.Message)
    exit 3
}

[void][Reflection.Assembly]::LoadFrom($apiDll)
[void][Reflection.Assembly]::LoadFrom($autDll)

$app = $null
try {
    $app = New-Object Autodesk.Navisworks.Api.Automation.NavisworksApplication
    $app.DisableProgress()
    Write-Output "== Cargando el plugin en la instancia automatizada"
    $app.AddPluginAssembly($dll)
    Write-Output "== Abriendo el modelo"
    $app.OpenFile($Nwd)
    Write-Output "== Ejecutando el volcado"
    # UN SOLO parametro: ExecuteAddInPlugin CONCATENA los argumentos en una sola
    # cadena separada por espacios. Pasar @($ruta, $tope) produce una ruta con el
    # tope pegado al final, y el plugin escribe un archivo con ese nombre absurdo
    # sin fallar. El tope de nodos va como default dentro del plugin.
    $r = $app.ExecuteAddInPlugin("AdasaDump.ADASA", $outMd)
    Write-Output ("   ExecuteAddInPlugin devolvio: " + $r)
} catch {
    Write-Output ("== FALLO: " + $_.Exception.Message)
    if ($app) { try { $app.Dispose() } catch {} }
    exit 2
}
if ($app) { try { $app.Dispose() } catch {} }

if (Test-Path $outMd) {
    $n = (Get-Content $outMd | Measure-Object -Line).Lines
    Write-Output "== Escrito: $outMd ($n lineas)"
    exit 0
} else {
    Write-Output "== El plugin no escribio el archivo de salida."
    exit 2
}
