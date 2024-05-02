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

