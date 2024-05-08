from datetime import datetime, timedelta
import time

# runs a function every t seconds, from start_time to end_time
def runEveryTSeconds(t, start_time, end_time, function, stockName):
    while True:
        current_time = datetime.now()

        if current_time < start_time:
            waitTime = start_time - datetime.now()
            print("Waiting for {}".format(waitTime))
            time.sleep(waitTime.total_seconds())
        elif start_time <= current_time <= end_time:
            function(stockName)
            time.sleep(t)
        elif current_time > end_time:
            waitTime = start_time+timedelta(days=1) - datetime.now()
            print("Waiting for {}".format(waitTime))
            time.sleep(waitTime.total_seconds())

