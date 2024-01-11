import os
import logging
from constants import PROJECT_DIR

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler(
    os.path.join(PROJECT_DIR, 'logs/app_seges.txt')
)
file_handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    )
logger.addHandler(file_handler)
