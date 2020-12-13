class DlNode:
    def __init__ (self, value):
        self.Value = value
        self.Next = None
        self.Prev = None
class DLList:
    def __init__ (self):
        self.Head = None
        self.Tail = None
    def add(self, val):
        newNode = DlNode(val)
        if self.Head == None:
            self.Head = newNode
            self.Tail = newNode
        else:
            runner = self.Head
            while runner.Next != None:
                runner = runner.Next
            runner.Next = newNode
            runner = newNode.Prev
            self.Tail = newNode
    def display(self):
        runner = self.Head
        while runner.Prev != None:
            print(runner.Prev.Value)
            runner = runner.Next
        print("____________")
    def get(self, val):
        runner = self.Head
        while runner != None:
            if runner.Value == val:
                return runner
            runner = runner.Next
        return -1
    def reverse(self):
        runner = self.Tail.Value
        print(self.Tail)
        while runner != None:
            print(runner.Value)
            runner = runner.Prev
        print("____________")
newList = DLList()
newList.add(1)
newList.add(2)
newList.add(3)
newList.display()
newList.reverse()





