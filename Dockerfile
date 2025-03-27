# Usar uma imagem oficial do Python
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos para o container
COPY requirements.txt .
COPY app.py .

# Instalar as dependências
RUN pip install -r requirements.txt

# Expor a porta 5000
EXPOSE 8080

# Comando para rodar o app
CMD ["python", "app.py"]

VOLUME ["/mnt/secret"]