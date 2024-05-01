import win32ui
import dde

# setting up
serverName = "Spark"
server = dde.CreateServer()
server.Create("TestClient") # The argument name used inside Create function doesn't matter
conversation = dde.CreateConversation(server)

# This is the main function which bypasses Excel to use DDE directly using Python
# calling command(topic, field) is equivalent to calling
# =Spark|<topic>!<fields> in Excel
def command(topic, field):
    conversation.ConnectTo(serverName, topic)
    requestedData = conversation.Request(field)
    return requestedData

# Getting the current price of the stock BHP
topic = "BHP.Quote"
field = "Code.Price"
currPriceOfBHP = command(topic, field)
print("Current BHP price \n", currPriceOfBHP)

# Getting the last 10 EOD price of BHP stock
topic = "BHP.History" 
field = "Code.Price.10" 
last10EODValuesOfBHP = command(topic, field)
print("Last 10 EOD price of BHP \n", last10EODValuesOfBHP)