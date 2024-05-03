# use cases

import connect
import writeCsv

# trying some thing
#topic = "BHP.order"
topic = "BHP.Depth"
field = "Time.Date.Price"
requestedData = connect.command(topic, field)
print(requestedData)
writeCsv.writeCsv("csv/historic.csv", requestedData)
# print(requestedData)



topic = "ASX.indexValues"
field = "Time.Date.Price"
requestedData = connect.command(topic, field)
# print(requestedData)

'''
# Getting the current price of the stock BHP
topic = "BHP.Quote"
field = "Code.Price"
currPriceOfBHP = connect.command(topic, field)
print("Current BHP price \n", currPriceOfBHP)

# Getting the last 10 EOD price of BHP stock
topic = "BHP.History" 
field = "Code.Price.10" 
last10EODValuesOfBHP = connect.command(topic, field)
print("Last 10 EOD price of BHP \n", last10EODValuesOfBHP)
'''
