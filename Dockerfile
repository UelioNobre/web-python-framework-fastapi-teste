# # Imagem base oficial
# FROM python:3.12-slim

# # Diretório de trabalho
# WORKDIR /app

# # Instala dependências do sistema (opcional, caso precise de libs extras)
# # RUN apt-get update && apt-get install -y \
# #     build-essential dcmtk \
# #     && rm -rf /var/lib/apt/lists/*

# # Copia o requirements
# COPY requirements.txt .

# # Instala dependências Python
# RUN pip install --upgrade pip \
#     && pip install -r requirements.txt

# # Copia todo o projeto (mas na prática, o volume sobrescreve em dev)
# COPY . .

# # Expondo a porta
# EXPOSE 5000

# SHELL ["/bin/bash", "-c"]

# # Comando padrão (sobrescrito no compose)
# CMD ["flask --app server.py", "run", "--debug", "--host=0.0.0.0", "--port=5000"]

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]