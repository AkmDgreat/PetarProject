# run the get price function, every 30 seconds, from 6.30 am pst to 1pm pst
import connect
import writeCsv
from datetime import datetime

# Gets the current date and time in correct format
def getDate():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime

# Gets the current price of the stock with name stockName
def getPrice(stockName):
    topic = "{}.Quote".format(stockName)
    field = "Price"
    currPriceOfStock = connect.command(topic, field)
    return float(currPriceOfStock)

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


writeCsv.writeCsv("csv/output.csv", getArr("BHP"))






