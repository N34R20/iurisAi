from utils.parser.ParserPDF import save_pdf_to_txt
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Set paths for the pdf and the txt output.')
    parser.add_argument('--pdf_path', type=str, help='Path to the pdf file')
    return parser.parse_args()

args = parse_arguments()
pdf_file_path = args.pdf_path

text_folder = "./data/text/"
txt_file_name = pdf_file_path.split("/")[-1].split(".")[0]
txt_file_path = f"{text_folder}{txt_file_name}.txt"

# Ruta al archivo PDF de entrada y al archivo de texto de salida
#pdf_file_path = './data/pdf/FALLO CSS 081244_2015_CS001.pdf'
#txt_file_path = './data/text/FALLO CSS 081244_2015_CS001.txt'

save_pdf_to_txt(pdf_file_path,txt_file_path)