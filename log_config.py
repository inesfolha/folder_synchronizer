import logging
import datetime as dt


def configure_logger(root_path):
    today = dt.datetime.today()
    filename = f"{today.day:02d} - {today.month:02d} - {today.year}.log"

    # Create the logger only if it doesn't exist
    logger = logging.getLogger(__name__)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create a file handler and set the level to INFO
        file_handler = logging.FileHandler(f"{root_path}/{filename}")
        file_handler.setLevel(logging.INFO)

        # Create a stream handler and set the level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
