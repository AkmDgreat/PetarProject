import win32ui
import dde

serverName = "Spark"
topic = "BHP.Quote"
command = "Price"

server = dde.CreateServer()
server.Create("TestClient")
conversation = dde.CreateConversation(server)

conversation.ConnectTo(serverName, topic)
conversation.Exec(command)

requestedData = conversation.Request("some")