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
    def findConnectionSpace(self, user, potCon, count = 0):
        if count == 3:
            return count
        if potCon in user.connections:
            return count
        else:
            for u in user.connections:
                return self.findConnectionSpace(u, potCon, count+1)

g = Graph()
g.addNode("nate", "bob")
g.addNode("nateasdf", "boasdfb")
g.addNode("natfdasde", "bobdfdsa")
g.addNode("logan", "bob")
g.addNode("natfdasdfasde", "boasdfbdfdsa")
g.addNode("natfdaasdfsdfasde", "boasdfbdasdffdsa")
g.printNodes()
this_node = g.getNode("nate", "bob")
con_node = g.getNode("logan", "bob")
c1 = g.getNode("nateasdf", "boasdfb")
c2 = g.getNode("natfdasde", "bobdfdsa")
c3 = g.getNode("natfdasdfasde", "boasdfbdfdsa")
c4 = g.getNode("natfdaasdfsdfasde", "boasdfbdasdffdsa")
# this_node.addConnection(con_node)
con_node.addConnection(c1)
this_node.addConnection(c1)
c1.addConnection(c2)
c2.addConnection(c3)
c3.addConnection(c4)
c4.addConnection(con_node)
this_node.printConnections()
print(g.findConnectionSpace(this_node, con_node))
