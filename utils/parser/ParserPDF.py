from PyPDF2 import PdfReader

def parse_pdf_to_text(pdf_path):
    reader = PdfReader(pdf_path)
    len_pages = len(reader.pages)
    text = ''
    for page_num in range(len_pages):
        page = reader.pages[page_num]
        text += page.extract_text()

    return(text)

def save_txt(text,text_path):
    f = open (text_path,'w')
    f.write(text)
    f.close()

def save_pdf_to_txt(pdf_path,text_path):
    text = parse_pdf_to_text(pdf_path)
    save_txt(text,text_path)
