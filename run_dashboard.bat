@echo off
cd /d "%~dp0"
echo Starting Vireo Audio Support Analytics...
python -m streamlit run app.py --server.address localhost --server.port 8501 > streamlit.log 2>&1
echo Streamlit stopped. Details are in streamlit.log.
pause
