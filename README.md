# SimpleIvyConnector
Simple connector for [Ivy API](http://www.eei.cena.fr/products/ivy/) made by the french CENA (*Centre d'Etudes de la Navigation Aérienne*).

# Story
I made this API for a university project where I had to use Ivy with Python.
Since there is no clear & simple `hello world`-like example, I decided to make a simple connector with a basic *client-server* example (even though it's more like a peer-to-peer system) to help anyone who wanted to start prototyping something with Ivy.

# Dependencies
SimpleIvyConnector was developped with Python 3.5 on Windows.

Only needs Ivy ("`sudo pip install ivy`").

# Example
For people who just want to copy and past the file and not look at the *example* folder :

##### Server.py
(Technically, this is just the client initiating the Ivy bus)
```Python
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
```
##### Client.py
```Python
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
```

# Licence
Just please respect the GNU GPL licence (file "*LICENSE*" included at the root folder)

I won't be mad if you don't, but please do ;)
