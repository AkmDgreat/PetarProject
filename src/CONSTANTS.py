from datetime import datetime

START_TIME = datetime.now().replace(hour=6, minute=30, second=0, microsecond=0)
END_TIME = datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)
TIME_INTERVAL_TO_WRITE_MARKET_DATA = 120
TIME_INTERVAL_TO_WRITE_SIG_VALUE = 30
NUM_LINES = (3*24*60) / 2
ONE_DAY = 24*60 / 2