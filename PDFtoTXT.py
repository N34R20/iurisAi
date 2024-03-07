# Ruta al archivo PDF de entrada y al archivo de texto de salida
pdf_file_path = 'FALLO CSS 081244_2015_CS001.pdf'
txt_file_path = 'fallo.txt'


# Abre el archivo PDF en modo lectura binaria
with open(pdf_file_path, 'rb') as pdf_file:
    # Lee todo el contenido binario del archivo
    pdf_content = pdf_file.read()

    # Decodifica el contenido binario a una cadena Unicode
    #pdf_text = pdf_content.decode('utf-8')

    # Imprime o procesa pdf_text según tus necesidades
    print(pdf_content)

