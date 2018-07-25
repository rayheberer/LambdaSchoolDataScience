"""
Implement a doubly-linked list, where each node points to both the node after it in the list, as well as the node that came before it. 

This challenge is difficult, but please put your best foot forward, as with every morning code challenge, to at the very least get pseudocode for how you would implement this data structure. Taking the easy route and just waiting for the solution without making any sort of attempt is not only a disservice to you but also to us, the instructors. 

If questions arise while you're working on the challenge, please ask questions in the appropriate channels to get you unstuck.
"""

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next
  
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this Node could already
    have a next node it is pointing to."""
    def insert_after(self, val):
       self.next = ListNode(val, prev=self)
       return self.next
     
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this Node could already
    have a previous node it is pointing to."""
    def insert_before(self, val):
       self.prev = ListNode(val, next=self)
       return self.prev
    
    def get_value(self):
        return self.val
        
    def get_prev(self):
        return self.prev
        
    def get_next(self):
        return self.next
    
      
    """Rearranges this ListNode's previous and next pointers 
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.next:
            self.next.prev = self.get_prev()
        if self.prev:
            self.prev.next = self.get_next()

      
"""Our doubly-linked list class. It holds references to 
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
  
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, val):
        if self.head:
            self.head = self.head.insert_before(val)
        else:
            self.head = ListNode(val)
            self.tail = self.head
    
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the removed Node."""
    def remove_from_head(self):
        removed = self.head.get_value()
        self.head.delete()
        return removed
      
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, val):
        if self.tail:
            self.tail = self.tail.insert_after(val)
        else:
            self.tail = ListNode(val)
            self.head = self.tail
      
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the removed Node."""
    def remove_from_tail(self):
        removed = self.tail.get_value()
        self.tail.delete()
        return removed
    
      
    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        current = self.head
        while current:
            if current == node:
                value = node.get_value()
                self.delete(node)
                self.add_to_head(value)
            current = current.get_next()
    
    
    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        current = self.head
        while current:
            if current == node:
                value = node.get_value()
                self.delete(node)
                self.add_to_tail(value)
            current = current.get_next()
            
    def delete(self, node):
        node.delete()