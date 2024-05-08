from getDateAndPrice import getDate, getPrice
import runFunctionsEveryTSeconds
import writeCsv
from CONSTANTS import START_TIME, END_TIME, TIME_INTERVAL_TO_WRITE_SIG_VALUE

# create a 2d array with given rows and columns
def createTwoDArray(rows, cols):
    arr = []
    for i in range(rows):
        arr.append([0] * cols)   
    return arr
       
# gets the array, which will be used to write data in CSV
def getArr(stockName):
        arr = createTwoDArray(1, 2)
        arr[0][0] = getPrice(stockName)
        arr[0][1] = getDate()
        return arr

# writes the data to sig value file
def write(stockName):
    writeCsv.writeCsv("csv/sigValue.csv", getArr(stockName))

def writeSigValue(stockName):
    runFunctionsEveryTSeconds.runEveryTSeconds(TIME_INTERVAL_TO_WRITE_SIG_VALUE, START_TIME, END_TIME, write, stockName)
