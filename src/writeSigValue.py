import realTimeData
import runFunction
import writeCsv
from datetime import datetime

# create a 2d array with given rows and columns
def createTwoDArray(rows, cols):
    arr = []
    for i in range(rows):
        arr.append([0] * cols)   
    return arr
       
# gets the array, which will be used to write data in CSV
def getArr(stockName):
    arr = createTwoDArray(1, 2)
    arr[0][0] = realTimeData.getPrice(stockName)
    arr[0][1] = realTimeData.getDate()
    return arr

# Define the starting and ending times
start_time = datetime.now().replace(hour=6, minute=30, second=0, microsecond=0)
end_time = datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)

# writes the data to sig value file
def writeSigValue(stockName):
    writeCsv.writeCsv("csv/sigValue.csv", getArr(stockName))

runFunction.run_function_every_t_seconds(30, start_time, end_time, writeSigValue("BHP"), "BHP")