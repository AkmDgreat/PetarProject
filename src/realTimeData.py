# run the get price function, every 30 seconds, from 6.30 am pst to 1pm pst
import connect
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