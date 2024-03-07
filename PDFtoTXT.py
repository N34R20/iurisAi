# Ruta al archivo PDF de entrada y al archivo de texto de salida
pdf_file_path = 'FALLO CSS 081244_2015_CS001.pdf'
txt_file_path = 'fallo.txt'

import argparse

class SharedState:
    def __init__(self):
        pdf_path = None

shared_state = SharedState()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Set path for the pdf and .txt file.')
    parser.add_argument('--pdf_path', type=str, help='Path to the pdf file')
    return parser.parse_args()

args = parse_arguments()

shared_state.pdf_path = args.pdf_path

print(shared_state.pdf_path)

"""
https://pypdf2.readthedocs.io/en/3.0.0
"""
from PyPDF2 import PdfReader

reader = PdfReader(pdf_file_path)
len_pages = len(reader.pages)

# Inicializar una cadena para almacenar el texto extraído
text = ''

for page_num in range(len_pages):
    page = reader.pages[page_num]
    text += page.extract_text()

print(text)

"""
Falta dumpear el .txt en un folder/archivo y que sea tambien un argumento de la cli

"""