class Node:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.connections = set([])
    def addConnection(self, node):
        self.connections.add(node)
    def printConnections(self):
        for c in self.connections:
            print(f"{c.first_name} {c.last_name}")

class Graph:
    def __init__ (self):
        self.nodes = set([])
    def addNode(self, first, last):
        newNode = Node(first, last)
        self.nodes.add(newNode)
    def printNodes(self):
        for node in self.nodes:
            print(f"{node.first_name} {node.last_name}")
        print("___________________")
    def getNode(self, first, last):
        for node in self.nodes:
            if node.first_name == first and node.last_name == last:
                return node
        return None
g = Graph()
g.addNode("nate", "bob")
g.addNode("nateasdf", "boasdfb")
g.addNode("natfdasde", "bobdfdsa")
g.addNode("logan", "bob")
g.printNodes()
this_node = g.getNode("nate", "bob")
con_node = g.getNode("logan", "bob")
this_node.addConnection(con_node)
this_node.printConnections()
