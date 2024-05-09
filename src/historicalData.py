# algorithm:
# get the prices of a stock for every two minute time interval
# get the prices for t=0, t=2, 
# open_price, closed_price, time
# (price at time=t, price at time=t+2, time t)
# (price at time=t+2, price at time=t+4, time t+2)
# (0,2) (2,4)

# find a way to get current time in python
# find a way to get current time minus 3 days
# find a way to get the stock price for each time 

import pandas as pd
import CONSTANTS

# returns the last 2160 lines from the csv file
# if there are less than 2160 lines, then, returns all the lines
def historicalData(stockName):
    filePath = f"csv/{stockName} DATA.csv"
    df = pd.read_csv(filePath)

    with open(filePath, 'r') as file:
        totalLines = sum(1 for _ in file)

    if CONSTANTS.NUM_LINES > totalLines:
        df.tail(totalLines).to_csv(filePath, index=False)
   
    df.tail(CONSTANTS.NUM_LINES).to_csv(filePath, index=False)
