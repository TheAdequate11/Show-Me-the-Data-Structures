"""
-------------------------------------------------------------------------------
                            Defining Classes
-------------------------------------------------------------------------------
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

    #Getters, setters, and condition checkers
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        """
        Creates a node using the input value and then appends it to the end of
        the linked list.
        Args:
            value (string): Desired value of node.
        """
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        """
        Iterates through the linked list and counts each iteration; then returns
        the cound which is equivalent to the linked list's size.

        Returns:
            size (int): number of items in linked list
        """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    #Getters, setters, and condition checkers
    def get_head(self):
        return self.head

"""
-------------------------------------------------------------------------------
                            Defining Functions
-------------------------------------------------------------------------------
"""
def union(llist_1, llist_2):
    """
    Finds the values that are in llist_1, llist_2, or in both.

    Args:
      llist_1: A linked list containing values of any type
      llist_2: A linked list containing values of any type

    Returns:
        Linked list containing the values that are in llist_1, llist_2, or in both.
    """
    union_set = set()
    return_linked_list = LinkedList()
    node = llist_1.get_head()
    while node:
        union_set.add(node.get_value())
        node = node.get_next()
    node = llist_2.get_head()
    while node:
        union_set.add(node.get_value())
        node = node.get_next()
    for item in union_set:
        return_linked_list.append(item)
    if return_linked_list.size() == 0:
        return 'No unions found'
    return return_linked_list

def intersection(llist_1, llist_2):
    """
    Finds values that are in both, llist_1 and llist_2

    Args:
      llist_1: A linked list containing values of any type
      llist_2: A linked list containing values of any type

    Returns:
        Linked list containing the values that are in both, llist_1 and llist_2
    """
    hashmap = {}
    return_linked_list = LinkedList()
    node = llist_1.get_head()
    while node:
        hashmap[node.get_value()] = 0
        node = node.get_next()
    node = llist_2.get_head()
    while node:
        if node.get_value() in hashmap:
            if hashmap[node.get_value()] == 1:
                node= node.get_next()
                continue

            return_linked_list.append(node.get_value())
            hashmap[node.get_value()] = 1
        node = node.get_next()
    if return_linked_list.size() == 0:
        return 'No intersections found'
    return return_linked_list

"""
-------------------------------------------------------------------------------
                            Test Case #1
-------------------------------------------------------------------------------
"""
print("Test Run #1:")
print()

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
'''
Expected:
[3,2,4,35,6,65,6,4,3,21,32,9,1,11]
[6, 4, 21]
'''

print('_______________________________________________________________________')


"""
-------------------------------------------------------------------------------
                            Test Case #2
-------------------------------------------------------------------------------
"""
print("Test Run #2:")
print()
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
'''
Expected:
[3,2,4,35,6,65,6,4,3,23,1,7,8,9,11]
No intersections found
'''

print('_______________________________________________________________________')


"""
-------------------------------------------------------------------------------
                            Test Case #3
-------------------------------------------------------------------------------
"""
print("Test Run #3:")
print()
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
'''
Expected:
No unions found
No intersections found
'''
print('_______________________________________________________________________')
"""
-------------------------------------------------------------------------------
                            Test Case #4
-------------------------------------------------------------------------------
"""
print("Test Run #4:")
print()
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,2,3,4,5,6,7,8,9,10]
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
'''
Expected:
[1,2,3,4,5,6,7,8,9,10]
No Intersections found
'''
print('_______________________________________________________________________')
"""
-------------------------------------------------------------------------------
                            Test Case #5
-------------------------------------------------------------------------------
"""
print("Test Run #5:")
print()
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,1,1,1,1,1,1,2]
element_2 = [2]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
'''
Expected:
[1,2]
[2]
'''
print('_______________________________________________________________________')
