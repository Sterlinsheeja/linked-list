class Node:
  def __init__(self,data):
    self.data=data
    self.nextt=None
    self.size=0
class SLL:
  def __init__(self):
    self.head=None
    self.size=0
  def addInMid(self, data):  
        newNode = Node(data) 
        if(self.head == None):  
            self.head = newNode  
            self.nextt = newNode 
        else:  
            count = (self.size//2) if(self.size % 2 == 0) else ((self.size+1)//2) 
            temp = self.head 
            current = None 
            for i in range(0, count):  
                current = temp  
                temp = temp.next  
            current.next = newNode  
            newNode.next = temp
        self.size = self.size + 1 
  def deleteNode(self, position): 
        if self.head == None: 
            return 
        temp = self.head 
        if position == 0: 
            self.head = temp.next
            temp = None
            return
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break 
            if temp is None: 
                return 
            if temp.next is None: 
                return 
        next = temp.next.next
        temp.next = None
        temp.next = next
  def printList(self):
      temp=self.head
      while temp!=None:
          print(temp,"==>",end='')
          temp=temp.nextt
      print("None")  
obj=SLL()
ch=0
while ch!=4:
    print("Linked list implementation\n","1.Insertion 2. Deletion 3. Print Llist 4. Exit")
    ch=int(input())
    if ch==1:
        print("enter value of the node")
        data=input()
        obj.addInMid(data)
        obj.printList()
    elif ch==2:
        obj.deleteNode()
        obj.printList()
