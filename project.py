import win32ui
import dde

serverName = "Spark"
topic = "BHP.Quote"
#topic = "BHP.Depth"

command = "Price"
#command = "!BuyCount.BuyVolume.Buy.Sell.SellVolume.SellCount"

server = dde.CreateServer()
server.Create("TestClient")
conversation = dde.CreateConversation(server)

conversation.ConnectTo(serverName, topic)
# conversation.Exec(command)

requestedData = conversation.Request(command)
print(requestedData)