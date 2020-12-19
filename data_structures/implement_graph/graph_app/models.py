from django.db import models

# Create your models here.
class PersonManager(models.Manager):
    def findConnectionSpace(self, user, potCon, count = 0):
        if count == 3:
            return count
        if potCon in user.connections:
            return count
        else:
            for u in user.connections:
                return self.findConnectionSpace(u, potCon, count+1)
class Person(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    connections = models.ForeignKey('self', related_name="connection", on_delete=models.CASCADE)
    objects = PersonManager()

    def addConnection(self, node):
        self.connection.add(node)
    def printConnections(self):
        for c in self.connection:
            print(f"{c.first_name} {c.last_name}")



# class Node:
#     def __init__ (self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.connections = set([])
#     def addConnection(self, node):
#         self.connections.add(node)
#     def printConnections(self):
#         for c in self.connections:
#             print(f"{c.first_name} {c.last_name}")

# class Graph:
#     def __init__ (self):
#         self.nodes = set([])
#     def addNode(self, first, last):
#         newNode = Node(first, last)
#         self.nodes.add(newNode)
#     def printNodes(self):
#         for node in self.nodes:
#             print(f"{node.first_name} {node.last_name}")
#         print("___________________")
#     def getNode(self, first, last):
#         for node in self.nodes:
#             if node.first_name == first and node.last_name == last:
#                 return node
#         return None
#     def findConnectionSpace(self, user, potCon, count = 0):
#         if count == 3:
#             return count
#         if potCon in user.connections:
#             return count
#         else:
#             for u in user.connections:
#                 return self.findConnectionSpace(u, potCon, count+1)