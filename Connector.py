'''
Created on 19 apr. 2017
@author: Seblor
@repo: https://github.com/Seblor/SimpleIvyConnector
'''

from ivy.std_api import *
from logging import info, getLogger, ERROR, debug


class Connector():
    def __init__(self, clientName, onConnected=None, onDisconnected=None, ip="127.0.0.1", port="2222", loggerEnabled=False):
        """
        Connector constructor
        
        @param clientName: string with the name of the client
        @param onConnected: (Optional, default is None) Function triggered when connected to another client
        @param onDisconnected: (Optional, default is None) Function triggered when client disconnected
        @param ip: (Optional, default is 127.0.0.1) The IP to connect to. (Ivy is working locally only)
        @param port: the port to connect to. (default is 2222)
        @param loggerEnabled: (Optional, default is False) Enables the Ivy INFO logs
        """
        def on_connection_change(agent, event):
            """
            Connection change handler (private)
            """
            if event == IvyApplicationDisconnected :
                if self.onDisconnected is not None:
                    self.onDisconnected(agent)
                else:
                    info("Ivy application %r has disconnected", agent)
            else :
                if self.onConnected is not None:
                    self.onConnected(agent)
                else:
                    info("Ivy application %r has connected", agent)
            info("Ivy application currently on the bus: %s", ','.join(IvyGetApplicationList()))
        
        # Setting the attributes 
        self.clientName = clientName
        self.onConnected = onConnected
        self.onDisconnected = onDisconnected
        
        # Initiating Ivy
        IvyInit(clientName, "", 0, on_connection_change, self.on_die)
        
        # Enable or disable the logger
        if not loggerEnabled:
            getLogger("Ivy").setLevel(ERROR)
            print("disabled infos")
        
        # Start Ivy
        IvyStart('%s:%s' % (ip, port))
        
    
    def addRegexListener(self, regex, listener):
        """
        Adds a listener through a regular expression
        
        @param regex: Regular expression (do not forget to group the part you want to recover)
        @param listener: callback(agent, message)
        """
        debug("adding regex: %s" % regex)
        IvyBindMsg(listener, regex)
    
    def addKeywordListener(self, keyword, listener):
        """
        Adds a listener through a keyword
        
        @param keyword: will recover everything after the keyword (which needs to be followed by a whitespace)
        @param listener: callback(agent, message)
        """
        self.addRegexListener(regex="^%s ?(.*)" % (keyword), listener=listener)
    
    def on_die(self, agent, id):
        """
        Connection lost Listener
        
        @param agent: agent who disconnected
        @param id: callback(agent, message)
        """
        info('Received the order to die from %r with id = %d', agent, id)
        IvyStop()
    
    def sendMessage(self, message, keyword=None):
        """
        Sends a message to the other client
        
        @param message to be send
        @param keyword: (Optional, default is None) The keyword to use
        """
        debug("sending message %s with keyword %s" % (message, keyword))
        if keyword is None:
            msg = message
        else:
            msg = "%s %s" % (keyword, message)
        debug("final message sent %s" % msg)
        IvySendMsg(msg)
    
    def isAlone(self):
        """
        Returns True if no other client is detected
        """
        return (len(IvyGetApplicationList()) == 1)
    
    def getClients(self):
        """
        Returns the list of the connected clients
        """
        return IvyGetApplicationList()
    
    def closeConnection(self):
        """
        Stops Ivy
        """
        IvyStop()