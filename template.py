import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

projectName = 'textSummarizer'

fileList = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/utils/common.py",
    f"src/{projectName}/logging/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipeline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for fpath in fileList:
    fpath = Path(fpath)
    fdir, fname = os.path.split(fpath)
    
    if fdir != "":
        os.makedirs(fdir, exist_ok=True)
        logging.info(f"Created directory: {fdir} for {fname}")

    if (not os.path.exists(fpath)) or (os.path.getsize(fpath) == 0):
        with open(fpath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {fpath}")
    
    else:
        logging.info(f"File already exists: {fpath}")




