class SLNode:
    def __init__ (self, value):
        self.Value = value
        self.Next = None
class SLList:
    def __init__ (self):
        self.Head = SLNode(None)
    def add(self, val):
        newNode = SLNode(val)
        if self.Head.Value == None:
            self.Head = newNode
        else:
            runner = self.Head
            while(runner.Next != None):
                runner = runner.Next
            runner.Next = newNode
    def removeAtFirst(self, val):
        runner = self.Head
        while(runner.Next.Value != val):
            runner = runner.Next
        runner.Next = runner.Next.Next
    def display(self):
        runner = self.Head 
        while(runner != None):
            print(runner.Value)
            runner = runner.Next
        print("_____________")
newList = SLList()
# newList.display()
newList.add(1)
newList.add(2)
newList.add(2)
newList.add(3)
newList.add(4)
newList.display()
newList.removeAtFirst(2)
newList.display()






