def parsear_archivo_txt(nombre_archivo)-> None:
    """
    Imprime todo un txt en la consola
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea.strip())  # strip() elimina los espacios en blanco al inicio y final de la línea
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print("Ocurrió un error al intentar leer el archivo:", e)

# Ejemplo de uso:
nombre_archivo = '/home/fran/Github/AI_iuris/data/text/FALLO CSS 081244_2015_CS001.txt'  # Reemplaza 'archivo.txt' con el nombre de tu archivo
parsear_archivo_txt(nombre_archivo)
