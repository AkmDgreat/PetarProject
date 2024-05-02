import realTimeData
import writeCsv

# writes the data to sig value file

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

writeCsv.writeCsv("csv/sigValue.csv", getArr("BHP"))