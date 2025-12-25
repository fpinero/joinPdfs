import os
import re
from pypdf import PdfWriter

def natural_sort_key(s):
    """Clave para ordenar cadenas con números de forma lógica (1, 2, 10...)."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

def unificar_pdfs_profesional():
    # 1. Obtención y limpieza de la ruta
    entrada_usuario = input("Arrastra la carpeta aquí o escribe la ruta: ").strip()
    ruta_origen = entrada_usuario.strip("'\"")
    
    if not os.path.isdir(ruta_origen):
        print(f"\nError: No se encuentra el directorio: {ruta_origen}")
        return

    # 2. Definición del archivo de salida y validación
    nombre_salida = input("Nombre del PDF final (ej: guia_final): ").strip().strip("'\"")
    if not nombre_salida.lower().endswith(".pdf"):
        nombre_salida += ".pdf"
    
    ruta_final = os.path.join(ruta_origen, nombre_salida)

    # Comprobación de existencia previa
    if os.path.exists(ruta_final):
        confirmacion = input(f"\nAtención: El archivo '{nombre_salida}' ya existe. ¿Deseas sobrescribirlo? (s/n): ").lower()
        if confirmacion != 's':
            print("Operación cancelada por el usuario.")
            return

    # 3. Proceso de unión
    escritor = PdfWriter()
    try:
        # Filtramos solo archivos PDF
        archivos = [f for f in os.listdir(ruta_origen) if f.lower().endswith(".pdf")]
        
        # Importante: eliminamos el archivo de salida de la lista si ya existía 
        # para no intentar unir el archivo resultante consigo mismo
        if nombre_salida in archivos:
            archivos.remove(nombre_salida)
            
        archivos.sort(key=natural_sort_key)

        if not archivos:
            print("No se encontraron otros archivos PDF para unir.")
            return

        print(f"\nIniciando la unión de {len(archivos)} archivos...")
        for nombre in archivos:
            print(f" -> Añadiendo: {nombre}")
            escritor.append(os.path.join(ruta_origen, nombre))

        with open(ruta_final, "wb") as f_salida:
            escritor.write(f_salida)
        
        print(f"\n¡Éxito! Archivo final generado en: {ruta_final}")

    except Exception as e:
        print(f"\nSe ha producido un error durante el proceso: {e}")
    finally:
        escritor.close()

if __name__ == "__main__":
    unificar_pdfs_profesional()