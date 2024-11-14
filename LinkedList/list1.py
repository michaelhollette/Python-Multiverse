class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def get_val(self):
        return self.val
    
    def set_val(self,val):
        self.val = val
    
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next


class LinkedList:
    def __init__(self, val  = None):
        self.head = val     

    def get_head(self):
        return self.head
    
    def append_node(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head =new_node

    def stringify_list(self):
        stringList = ''
        current_node  = self.get_head()
        while current_node is not None:
            if current_node.get_val() != None:
                stringList += str(current_node.get_val()) + '\n'
            current_node = current_node.get_next()
        return stringList
    
    def get_size(self):
        count = 0
        current = self.get_head()
        while current is not None and current.get_val() is not None:
            count += 1
            current = current.get_next()
        return count
    
    def find(self, item):
        current = self.get_head()
        while current is not None and current.get_val() is not None:
            if current.get_val() == item:
                return True
            current = current.get_next()
        return False
    
    def search(self, index):
        count = 0
        current = self.get_head()
        while current is not None and current.get_val() is not None:
            if count == index:
                return current.get_val()
            else:
                current = current.get_next()
                count += 1
    
    def delete_first(self):
        current = self.get_head()
        current = current.get_next()
        self.head = current
        
    def delete_last(self):
        current = self.get_head()
        previous = None
        while current is not None and current.get_val() is not None:
            if current.get_next() is None and previous is None:
                self.head = None

            if current.get_next() is None:
                previous.set_next(None)
            
            previous = current
            current = current.get_next()






list = LinkedList()
list.append_node(4)
list.append_node(3)
list.append_node(2)
list.append_node(1)

print(list.stringify_list())
print("Count is: ", list.get_size())
print(list.find(3))
print(list.find(5))
print(list.search(2))

list.delete_first()
print("After deleting first", list.stringify_list())
print("Count is: ", list.get_size())

list.delete_last()
print ("After deleting last", list.stringify_list())
print("Count is: ", list.get_size())
