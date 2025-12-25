# joinPdfs
# Guía de uso para el script joinPdfs

## Descripción

Este script de Python permite unificar múltiples archivos PDF en un único documento de forma ordenada. Está diseñado especialmente para casos donde los archivos están numerados (por ejemplo: 1.pdf, 2.pdf, 10.pdf), ya que utiliza una lógica de ordenación natural que evita los errores comunes de los exploradores de archivos.

El script gestiona automáticamente las rutas con espacios y protege contra la sobreescritura accidental de archivos existentes.

## Requisitos previos

Para utilizar esta herramienta es necesario tener instalado Python 3 y la librería de gestión de documentos especificada en el archivo de dependencias.

1. Crea el entorno virtual:
```bash
python3 -m venv .venv
```

2. Activa el entorno:
```bash
source .venv/bin/activate
```

3. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Instrucciones de uso

Sigue estos pasos para procesar tus documentos:

1. Ejecuta el script desde la terminal:
```bash
python3 unir_pdf.py
```

2. Cuando el programa lo solicite, indica la ruta de la carpeta donde se encuentran los archivos. En Mac OS puedes arrastrar la carpeta directamente a la ventana de la terminal para obtener la ruta de forma automática.

3. Introduce el nombre que deseas asignar al archivo final resultante.

4. Si el nombre elegido ya existe en la carpeta, el script solicitará una confirmación manual para proceder con la sobreescritura.

## Detalles técnicos sobre la ordenación natural

A diferencia de la ordenación estándar de los sistemas operativos (ordenación lexicográfica), que colocaría el archivo "10.pdf" antes que el "2.pdf", este script implementa una función de ordenación natural.

La lógica interna funciona de la siguiente manera:

* **Segmentación**: Utiliza expresiones regulares para dividir el nombre del archivo en partes de texto y partes numéricas.
* **Conversión**: Las partes detectadas como dígitos se convierten a números enteros (`int`).
* **Comparación**: Python compara las listas resultantes elemento a elemento. Al comparar números como enteros y no como texto, el valor 2 siempre será menor que 10, garantizando que el documento final mantenga la secuencia correcta de las infografías.

| Nombre de archivo | Ordenación estándar | Ordenación natural (script) |
|-------------------|---------------------|----------------------------|
| 1-guia.pdf        | 1-guia.pdf          | 1-guia.pdf                 |
| 2-guia.pdf        | 10-guia.pdf         | 2-guia.pdf                 |
| 10-guia.pdf       | 2-guia.pdf          | 10-guia.pdf                |
