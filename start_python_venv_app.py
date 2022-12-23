import os
os.system("""
python -m venv venv
venv\\Scripts\\activate.bat
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip list
""".strip().replace('\n', '&&'))
