from SimpleIvyAPI.Connector import Connector
#import logging
#logging.basicConfig(level=logging.DEBUG)

def disconnected(agent):
    print("agent %s disconnected" % agent)

def onConnected(agent):
    list = (1, 1, 9, 5, 13.37, "test")
    
    con.sendMessage(list, keyword="list")
    con.sendMessage("text %s" % list.__str__())
    print("Sent")

con = Connector(clientName="Server", port="2222", onConnected=onConnected, onDisconnected=disconnected )

