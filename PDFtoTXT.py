from utils.parser.ParserPDF import save_pdf_to_txt

# Ruta al archivo PDF de entrada y al archivo de texto de salida
pdf_file_path = './data/pdf/FALLO CSS 081244_2015_CS001.pdf'
txt_file_path = './data/text/FALLO CSS 081244_2015_CS001.txt'

save_pdf_to_txt(pdf_file_path,txt_file_path)