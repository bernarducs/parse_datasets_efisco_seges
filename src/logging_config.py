import os
import logging

def create_logger(log_file_path):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(
        log_file_path
    )
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
        )
    logger.addHandler(file_handler)
    return logger
