from getDateAndPrice import getDate, getPrice
import time
import writeCsv
from runFunctionsEveryTSeconds import runEveryTSeconds
import CONSTANTS

# create aN array of size n
def createOneDArray(n):
    arr = [0]*n
    return arr

def getArr(stockName):
    arr = createOneDArray(3)
    arr[0] = getPrice(stockName)
    arr[2] = getDate()
    time.sleep(CONSTANTS.TIME_INTERVAL_TO_WRITE_MARKET_DATA)
    arr[1] = getPrice(stockName)
    return arr

# writes the data to sig value file
def write(stockName):
    writeCsv.appendCsv(f"csv/{stockName} DATA.csv", getArr(stockName))

def writeMarketData(stockName): 
    runEveryTSeconds(0, CONSTANTS.START_TIME, CONSTANTS.END_TIME, write, stockName)