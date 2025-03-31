import re
import os

ARCHIVO_DATOS = "Curso_python"

patrones = {
    "teléfono": (r"\+?\d{1,3}-\d{2,3}-\d{4}-\d{4}",),
    "cumpleaños": (r"\b\d{2}/\d{2}/\d{4}\b",),
    "contraseña": (r"\b\w{8,}\b",),
    "sitio_web": (r"https?://[\w.-]+",),
    "tarjeta": (r"\b\d{4}-\d{4}-\d{4}-\d{4}\b",),
    "saldo": (r"Saldo:\s*\$?(\d+(\.\d{1,2})?)",),
    "nombre": (r"Nombre:\s*([A-Za-z\s]+)"),
    "curp": (r"\b[A-Z]{4}\d{6}[HM][A-Z]{5}\d{2}\b")
    }

def buscar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        
        datos = {}
        for clave, (patron, _) in patrones.items():
            coincidencia = re.search(patron, contenido)
            datos[clave] = coincidencia.group(1) if coincidencia else "No encontrado"
        
        return datos
    
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
        return None


def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        
        for clave, (patron, reemplazo) in patrones.items():
            contenido = re.sub(patron, reemplazo, contenido)

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

        print(f"Procesado: {nombre_archivo}")

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

datos_encontrados = buscar_datos(ARCHIVO_DATOS)

if datos_encontrados:
    print("\n Información encontrada en el archivo:")
    for clave, valor in datos_encontrados.items():
        print(f"{clave.capitalize()}: {valor}")

procesar_archivo(ARCHIVO_DATOS)

print(" Proceso completado.")
