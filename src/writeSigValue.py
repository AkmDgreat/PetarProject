from getDateAndTime import getDate, getPrice
import runFunctionsEveryTSeconds
import writeCsv
from CONSTANTS import START_TIME, END_TIME

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
    runFunctionsEveryTSeconds.runEveryTSeconds(30, START_TIME, END_TIME, write(stockName), stockName)

