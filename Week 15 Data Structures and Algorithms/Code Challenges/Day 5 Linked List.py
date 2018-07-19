"""
Linked List... again! 

In Python, the class constructor method is called __init__, and also that every class method accepts self as its first input parameter, in order to delineate to the Python interpreter that it is a class method instead of a regular function. We would just define a new node with something like 
new_node = Node(data).

Note that when we invoke a class method, you don't actually pass self into the class method. For example, if we want to instantiate a new Node instance, we can do that with new_node = Node(data), where data is the piece of data we want the Node to hold. We don't need to actually pass in some context as the first parameter. 

Try to do this without looking at your work from Monday/Tuesday, if you get stuck or need to take a peek to jog your memory that's great. Just getting in another rep to help OOP and the linked list data structure.
"""

"""Define a class with the `class` keyword"""
class Node:
    """The `__init__` method specifies how a 
    class should be initialized give some parameters. You'll 
    also notice the `self` keyword, which is passed in to 
    every class method as the first argument."""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    """Returns the data stored at the current node"""
    def get_data(self):
        return self.data

    """Returns the next node this node points to"""
    def get_next(self):
        return self.next_node

    """Sets this node's `next_node` pointer"""
    def set_next(self, new_next):
        self.next_node = new_next
        
    
"""Now that we've defined our `Node`, we can define our Linked List
class, which will utilize our `Node` class"""
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    """Wraps the input item in a Node and adds it as the 
    new head of the linked list"""
    def insert(self, item):
        current_head = self.head
        self.head = Node(item, current_head)
        
    """Returns the number of nodes in the linked list"""
    def size(self):
        size = 0
        if self.head:
            current = self.head
            size += 1
            while current.get_next():
                current = current.get_next()
                size += 1
        return size
    
    
    """Returns the Node containing the target item if 
    it is in the linked list, and None otherwise"""
    def search(self, target):
        if self.head:
            current = self.head
            while current:
                if current.data == target:
                    return current
                current = current.get_next()
        return None

    
    """Deletes the target item from the linked list if it is 
    in the list. Raises a ValueError exception otherwise if 
    the target item is not in the list"""
    def delete(self, target):
        current = self.head
        
        if current.data == target:
            self.head = current.get_next()
            del(current)
            return
        
        while current.get_next():
            parent = current
            current = current.get_next()
            if current.data == target:
                parent.set_next(current.get_next())
                del(current)
                return

        raise ValueError('Target item is not in the list')