import logging
logger = logging.getLogger(__name__)

#Handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#Level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logging.warning("this is a basic warning message")
logging.error("this is a basic error message")

