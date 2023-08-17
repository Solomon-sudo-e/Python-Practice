import logging
import traceback
from logging.handlers import RotatingFileHandler
logger = logging.getLogger(__name__)

#Handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#Level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s :: %(levelname)s :: %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

# logger.warning('this is a warning')
# logger.error('this is an error')

# try:
#     a = [1, 2, 3]
#     val = a[4]
# except IndexError as e:
#     logger.error("The error is %s", traceback.format_exc())

info_logger = logging.getLogger(__name__)
info_logger.setLevel(logging.INFO)

# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# info_logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('salmon')

# from logging.handlers import TimedRotatingFileHandler
# import time
# timed_handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
# info_logger.addHandler(timed_handler)
#
# for _ in range(6):
#     logger.info('helo world')
#     time.sleep(5)
