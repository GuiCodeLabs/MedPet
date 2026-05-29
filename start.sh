#!/bin/bash

# Inicia o backend (FastAPI) em segundo plano (background)
echo "Iniciando o Backend (FastAPI)..."
cd /workspace/backend
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Inicia o frontend (Streamlit) em primeiro plano
echo "Iniciando o Frontend (Streamlit)..."
cd /workspace/frontend
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
