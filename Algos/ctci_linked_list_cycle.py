"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    runner1 = head
    mySet = set([head]);
    while runner1 != None:
        if runner1.next in mySet:
            return True
        else:
            mySet.add(runner1)
            runner1 = runner1.next
    return False