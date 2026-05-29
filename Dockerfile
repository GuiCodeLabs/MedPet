# Dockerfile unificado para executar Backend (FastAPI) e Frontend (Streamlit) no mesmo container
FROM python:3.10-slim

WORKDIR /workspace

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia os arquivos de requisitos primeiro para aproveitar o cache do Docker
COPY backend/requirements.txt /workspace/backend/
COPY frontend/requirements.txt /workspace/frontend/

# Instala todas as dependências
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r backend/requirements.txt && \
    pip install --no-cache-dir -r frontend/requirements.txt

# Copia o restante do código para o container
COPY backend /workspace/backend
COPY frontend /workspace/frontend
COPY start.sh /workspace/start.sh

# Dá permissão de execução para o script de inicialização
RUN chmod +x /workspace/start.sh

# Expõe as portas do Backend e do Frontend
EXPOSE 8000
EXPOSE 8501

# Define o script que subirá os dois serviços juntos
CMD ["/workspace/start.sh"]
