import win32ui
import dde

serverName = "Spark"
topic = "BHP.Quote"
# topic = "BHP.Depth"
# topic = "BHP.A.Quote"
topic = "BHP.History" # EOD values of stock

command = "Code.Price.10" # gives u end of day stock price for last 10 days
# command = "BuyCount.BuyVolume.Buy.Sell.SellVolume.SellCount"

server = dde.CreateServer()
server.Create("TestClient")
conversation = dde.CreateConversation(server)

conversation.ConnectTo(serverName, topic)
# conversation.Exec(command)

requestedData = conversation.Request(command)
print(requestedData)