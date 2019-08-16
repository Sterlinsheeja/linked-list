class Node:
  def __init__(self,data):
    self.data=data
    self.nextt=None
class SLL:
  def __init__(self):
    self.head=None
  def delete_at_end(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        temp = self.head
        while temp.nextt.nextt is not None:
            temp = temp.nextt
        temp.nextt = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp= self.head
        while temp.nextt is not None:
            temp= temp.nextt
        temp.nextt = new_node;
  def printList(self):
      temp=self.head
      while temp!=None:
          print(temp,"==>",end='')
          temp=temp.nextt
      print("None")  
obj=SLL()
ch=0
while ch!=4:
    print("Linked list implementation\n","1.Insertion at begining 2. Deletion 3. Print list 4. Exit")
    ch=int(input())
    if ch==1:
        print("enter value of the node")
        data=input()
        obj.insert_at_end(data)
        obj.printList()
    elif ch==2:
        obj.delete_at_end()
        obj.printList()
    elif ch==3:
         obj.printList()
