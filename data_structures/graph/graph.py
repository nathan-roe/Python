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
    def getConnection(self, con_first=None, con_last=None):
        con_list = []
        if con_first == None and con_last == None:
            return "Not Valid"
        for c in self.connections:
            if con_first == None and con_last != None:
                if c.last_name == con_last:
                    print(f"{c.first_name} {c.last_name}")
                    con_list.append(c)
            elif con_last == None and con_first != None:
                if c.first_name == con_first:
                    print(f"{c.first_name} {c.last_name}")
                    con_list.append(c)
            else:
                if c.first_name == con_first and c.last_name == con_last:
                    print(f"{c.first_name} {c.last_name}")
                    con_list.append(c)
            print(c)
        print("____________________")
        return con_list
    def removeConnection(self, node):
        ret = node
        self.connections.remove(node)
        return ret

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
c3_first_mimic = g.getNode("natfdasdfasde", "boasdfbdfdsaasdfasd")
c4 = g.getNode("natfdaasdfsdfasde", "boasdfbdasdffdsa")
# this_node.addConnection(con_node)
con_node.addConnection(c1)
this_node.addConnection(c1)
c1.addConnection(c2)
c2.addConnection(c3)
c2.addConnection(c3_first_mimic)
c3.addConnection(c4)
c4.addConnection(con_node)
this_node.printConnections()
print(g.findConnectionSpace(this_node, con_node))
# c2.getConnection("natfdasdfasde", "boasdfbdfdsa")
unk_node = this_node.getConnection(c1.first_name)
print("__________")
print(unk_node[0].first_name)
print("__________")
c3.printConnections()
print("!")
print(c3.removeConnection(c4).first_name)
print("!")
c3.printConnections()

