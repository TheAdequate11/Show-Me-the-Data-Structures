"""
-------------------------------------------------------------------------------
                            Defining Classes
-------------------------------------------------------------------------------
"""

class Node():

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def delete(self):
        """
        Removes the node from the linked list by having the nodes next and previous
        nodes point to each other.
        """
        if self.has_previous() and self.has_next():
            self.next.set_previous(self.previous)
            self.previous.set_next(self.next)
        elif self.has_previous():
            self.previous.set_next(self.next)
        elif self.has_next():
            self.next.set_previous(self.previous)
        self.set_next(None)
        self.set_previous(None)

    #Getters, Setters and Condition Checkers
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def get_previous(self):
        return self.previous
    def get_key(self):
        return self.key
    def set_value(self,value):
        self.value = value
    def set_previous(self,node):
        self.previous = node
    def set_next(self,node):
        self.next = node
    def has_next(self):
        return self.get_next() != None
    def has_previous(self):
        return self.get_previous() != None



class Queue():

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, key,value):
        """
        Initializes a node with the input key and value; the node is then inserted
        added the queue.

        Args:
            key (any datatype): define the key for a node
            value (any datatype): define the corresponding value for a node based
            on the input key
        """
        new_node = Node(key,value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = self.tail.get_next()
        self.num_elements += 1

    def dequeue(self):
        """
        Removes the oldest used item (the head of the queue) from the queue and
        returns its key; otherwise none is returned if the queue is empty.

        Return:
            return_key: The key variable attributed to the dequeued node
            or
            None
        """

        return_key = self.head.get_key()
        if self.head.has_next():
            self.head = self.head.get_next()
            self.head.set_previous(None)
        else:
            self.head = None

        self.num_elements -= 1
        return return_key



    def update(self,node):
        """
        Moves the input node from its current position in the queue to the end of
        the queue.

        Args:
            node (class: Node): recently used node to be updated
        """
        if self.num_elements < 2:
            return
        if node is self.head:
            self.head = node.get_next()
        elif node is self.tail:
            self.tail = node.get_previous()
        node.delete()
        self.tail.set_next(node)
        self.tail.get_next().set_previous(self.tail)
        self.tail = self.tail.get_next()

    def print_queue(self):
        """
        Prints out the queue.
        """
        node = self.head
        n_list = []
        while node:
            n_list.append('{} : {} '.format(node.get_key(),node.get_value()))
            node = node.get_next()
        print('--> '.join(n_list))

    #Getters, Setters and Condition Checkers
    def get_tail(self):
        return self.tail
    def get_num_elements(self):
        return self.num_elements
    def is_empty(self):
        return self.num_elements == 0



class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_queue = Queue()
        self.cache = {}

    def get(self, key):
        """
        Prints item from provided key. Or prints '-1' if nonexistent.

        Args:
            key (any datatype): Key value to find desired value
        """

        if key in self.cache:
            self.cache_queue.update(self.cache[key])
            print(self.cache_queue.get_tail().get_value())
        else:
            print('-1')

    def set(self, key, value):
        """
        Set the value of the key is not present in the cache. If the cache is
        at capacity remove the oldest item.

        Args:
            key (any datatype): Key value to be inserted into cache
            value (any datatype): Accompanied value for key
        """
        if key not in self.cache:
                self.cache_queue.enqueue(key,value)
                self.cache[key] = self.cache_queue.get_tail()
        else:
                self.cache_queue.update(self.cache[key])
                self.cache[key].set_value(value)
        if self.cache_queue.get_num_elements() > self.capacity:
                del self.cache[self.cache_queue.dequeue()]


"""
-------------------------------------------------------------------------------
                            Test Case #1
-------------------------------------------------------------------------------
"""
print("Test Run #1:")
print()

test_cache_1 = LRU_Cache(8)

test_cache_1.get(5)
test_cache_1.get(None)

test_cache_1.set(None,None)

test_cache_1.set(5,3)
test_cache_1.set(5,4)

test_cache_1.get(5)

test_cache_1.set(5,5)
test_cache_1.set(5,'Word')

test_cache_1.get(5)

test_cache_1.set(55,0)

test_cache_1.set(None,23)

test_cache_1.set(-5,20000000000000000)

test_cache_1.set(20000000000, 3.1234)

test_cache_1.get(20000000000)

test_cache_1.set(1, 10)

test_cache_1.set(2, 2)

test_cache_1.set(3, 3)

test_cache_1.set(4, 4)

test_cache_1.get(5)

test_cache_1.get(None)

'''
Expected Output:
-1
-1
4
word
3.1234
-1
23
'''

"""
-------------------------------------------------------------------------------
                            Test Case #2
-------------------------------------------------------------------------------
"""
print('_______________________________________________________________________')
print("Test Run #2:")
print()

test_cache_2 = LRU_Cache(1)

test_cache_2.set('', 3)

test_cache_2.get('')

test_cache_2.set(5,3)

test_cache_2.get('')

test_cache_2.get(5)

test_cache_2.set(5,4)

test_cache_2.get(5)

test_cache_2.set(55,0)

test_cache_2.get('')

test_cache_2.get(5)

test_cache_2.get(55)


'''
Expected Output:
3
-1
3
4
-1
-1
0
'''


"""
-------------------------------------------------------------------------------
                            Test Case #3
-------------------------------------------------------------------------------
"""
print('_______________________________________________________________________')
print("Test Run #3:")
print()

test_cache_3 = LRU_Cache(0)

test_cache_3.set(2, 3.1234)

test_cache_3.get(2)

test_cache_3.set(3.0,3)

test_cache_3.get(3.0)

test_cache_3.set(2, 3.1234)

test_cache_3.get(2)

test_cache_3.set(3.0,3)

test_cache_3.get(3.0)

'''
Expected Output:
-1
-1
-1
-1
'''

"""
-------------------------------------------------------------------------------
                            Test Case #4
-------------------------------------------------------------------------------
"""
print('_______________________________________________________________________')
print("Test Run #4:")
print()

test_cache_4 = LRU_Cache(-1)

test_cache_4.set(2, 3.1234)

test_cache_4.get(2)

test_cache_4.set(3.0,3)

test_cache_4.get(3.0)

test_cache_4.set(2, 3.1234)

test_cache_4.get(2)

test_cache_4.set(3.0,3)

test_cache_4.get(3.0)

'''
Expected Output:
-1
-1
-1
-1
'''
"""
-------------------------------------------------------------------------------
                            Test Case #5
-------------------------------------------------------------------------------
"""
print('_______________________________________________________________________')
print("Test Run #5:")
print()

test_cache_5 = LRU_Cache(70)

for i,j in enumerate(range(70)):
    test_cache_5.set(i,j)


for i in range(70):
    test_cache_5.get(i)

test_cache_5.get(0)
test_cache_5.set(70,70)
test_cache_5.get(1)

'''
Expected Output:
Values from 0 to 69
0
-1
'''
