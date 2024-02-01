import logging
import os
from datetime import datetime


LOG_FILE = f"log_{datetime.now().strftime('%m_%d_%H_%M_%S')}.log"

LOG_DIR = "flower_log" #Log folder
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE) #Log file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO 
)

