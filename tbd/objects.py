class city:
    #each city can have up to 4 connections for now, we can change this later
    def __init__(self, name, connection1 = None, connection2 = None, connection3 = None, connection4 = None):
        self.name = name
        #check for each given connection and then add them to self.connections
        connections = []
        for i in [connection1, connection2, connection3, connection4]:
            if i != None:
                connections.append(i)
        self.connections = connections
    

class map():
    def __init__(self):
        #this dictionary stores the node of each city at all times
        self.cities = {}

    def addcity(self, name, connection1 = None, connection2 = None, connection3 = None, connection4 = None):
        self.cities[name] = city(name, connection1, connection2, connection3, connection4)