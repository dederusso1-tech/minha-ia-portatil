@echo off
cls
echo ===================================================
echo     INICIANDO O SEU CEREBRO PORTATIL (IA)
echo ===================================================

if not exist venv (
    echo Criando ambiente virtual isolado no pendrive...
    python -m venv venv
    echo Ambiente criado com sucesso!
    echo.
)

echo Ativando ambiente...
call venv\Scripts\activate

echo Verificando dependencias (Streamlit/Requests)...
pip install -r requirements.txt --quiet

echo.
echo Executando a IA...
streamlit run app.py

pause