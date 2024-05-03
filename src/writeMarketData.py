import realTimeData
import time
import writeCsv
import runFunction
from datetime import datetime

# create aN array of size n
def createOneDArray(n):
    arr = [0]*n
    return arr

def getArr(stockName):
    arr = createOneDArray(3)
    arr[0] = realTimeData.getPrice(stockName)
    arr[2] = realTimeData.getDate()
    time.sleep(120)
    arr[1] = realTimeData.getPrice(stockName)
    print(arr)
    return arr

# Define the starting and ending times
start_time = datetime.now().replace(hour=6, minute=30, second=0, microsecond=0)
end_time = datetime.now().replace(hour=13, minute=50, second=0, microsecond=0)

# writes the data to sig value file
def writeMarketData(stockName):
    writeCsv.appendCsv(f"csv/{stockName} DATA.csv", getArr(stockName))

runFunction.run_function_every_t_seconds(0, start_time, end_time, writeMarketData, "BHP")