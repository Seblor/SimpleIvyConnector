from SimpleIvyAPI.Connector import Connector

def listListener(agent, list):
    print("Got a list !")
    print(list)

def textListener(agent, text):
    print("Got a text !")
    print(text)

def connected(agent):
    print("Connected")

con = Connector(clientName="Client", port="2222", onConnected=connected)
con.addKeywordListener("list", listListener)
con.addRegexListener("text (.*)", textListener)

