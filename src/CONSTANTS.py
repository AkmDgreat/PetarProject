from datetime import datetime

# Start and end times of the market 
START_TIME = datetime.now().replace(hour=6, minute=30, second=0, microsecond=0)
END_TIME = datetime.now().replace(hour=13, minute=50, second=0, microsecond=0)
TIME_INTERVAL_TO_WRITE_MARKET_DATA = 120
TIME_INTERVAL_TO_WRITE_SIG_VALUE = 30


# just for testing purposes
# Start and end times are changed so that I can test the code right now, instead of waiting for time to be 6AM
# time intervals are made shorter, to make testing faster
START_TIME = datetime.now().replace(hour=18, minute=00, second=0, microsecond=0)
END_TIME = datetime.now().replace(hour=22, minute=00, second=0, microsecond=0)
TIME_INTERVAL_TO_WRITE_MARKET_DATA = 2
TIME_INTERVAL_TO_WRITE_SIG_VALUE = 3