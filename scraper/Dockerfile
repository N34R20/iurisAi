# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el script de scraping y el archivo de requisitos al contenedor
COPY scraper.py .

# Instala las dependencias necesarias
RUN pip install requests beautifulsoup4

# Comando para ejecutar el script
CMD ["python", "scraper.py"]

#docker build -t mi_scraper .

#docker run --name mi_scraper_container mi_scraper
