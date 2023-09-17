import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), LOG_FILE)
os.makedirs(LOGS_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)

