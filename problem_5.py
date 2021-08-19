import hashlib
from datetime import datetime
import time


"""
-------------------------------------------------------------------------------
                            Defining Classes
-------------------------------------------------------------------------------
"""
class Block:

    def __init__(self, timestamp,data,previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.next = None
        self.hash = self.calc_hash()

    def calc_hash(self):
        """
        Returns the hash value based on the data of the block and the timestamp
        of the blocks creation.

        Returns:
            sha.hexdigist() (class:hashlib): The hash value of the block
        """
        sha = hashlib.sha256()
        string = str(self.data) + str(self.timestamp) + str(self)
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    #Getters, setters, and condition checkers
    def get_hash(self):
        return self.hash
    def get_data(self):
        return self.data
    def get_timestamp(self):
        return str(self.timestamp)
    def get_previous_hash(self):
        return self.previous_hash
    def get_next(self):
        return self.next
    def set_next(self, value):
        self.next = value

class Linked_List():

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def append(self, data):
        """
        Creates a block based on the input data and appends it to the end of
        the linked list. Raises error for null value.

        Args:
            data (string): Transaction data of the block

        """
        if not data:
            print('Null values are not permitted. {!r} has been omitted.'.format(data))
            return
        if self.is_empty():
            self.head = Block(datetime.utcnow(),data, 0)
            self.tail = self.head
            self.num_items += 1
        else:
            new_block = Block(datetime.utcnow(),data, self.tail.get_hash())
            self.tail.set_next(new_block)
            self.tail = self.tail.get_next()
            self.num_items += 1

    def print_block(self):
        """
        Prints the block chain
        """
        if self.num_items == 0:
            print('Block Chain is Empty')
            return
        node = self.head
        string_time = ''
        string_data = ''
        string_hash = ''
        string_prev = ''
        while node:
            string_time = '|{:^12} {:<28s} |'.format('Timestamp:',str(node.get_timestamp()))
            string_data = '|{:^12} {:<28s} |'.format('Data:',str(node.get_data()))
            string_hash = '|{:^12} {:<28s} |'.format('Hash:',str(node.get_hash())[:28])
            string_prev = '|{:^12} {:<28s} |'.format('Prev_Hash:',str(node.get_previous_hash())[:28])
            print(string_time + '\n' + string_data + '\n' + string_hash + '\n' + string_prev)
            print('    ^ \n    | \n    |')
            node = node.get_next()

    #Getters, setters, and condition checkers
    def get_tail(self):
        return self.tail
    def is_empty(self):
        return self.num_items == 0

"""
-------------------------------------------------------------------------------
                            Defining Functions
-------------------------------------------------------------------------------
"""



"""
-------------------------------------------------------------------------------
                            Test Case #1
-------------------------------------------------------------------------------
"""



edge_value_2 = ['Car purchased','Beep','Car purchased','Car purchased','Car purchased','Car purchased']
value_3 = ['Car purchased', 'Cat purchased', 'dog purchased', '']

print("Test Run #1:")
print()

block_chain = Linked_List()
block_chain.append(None)
block_chain.append('')
block_chain.append(None)
block_chain.append('')
block_chain.print_block()
print('_____________________________________________________________________')
'''
Expected:
Null values are not permitted. None has been omitted.
Null values are not permitted. '' has been omitted.
Null values are not permitted. None has been omitted.
Null values are not permitted. '' has been omitted.
Block chain is empty.
'''

"""
-------------------------------------------------------------------------------
                            Test Case #2
-------------------------------------------------------------------------------
"""
print("Test Run #2:")
print()

block_chain = Linked_List()
block_chain.append('Car purchased')
block_chain.append('Car purchased')
block_chain.append('Car purchased')
block_chain.append('Car purchased')
block_chain.append('Car purchased')
block_chain.append('Car purchased')
block_chain.print_block()
print('_____________________________________________________________________')

'''
6 block similar to the one below. The data will be 'Car Purchased' for each. They
will each have a unique hash. First block has a previous hash of 0, and then
each proceeding block has previous hash of the previous block in the linked list.
|  Timestamp: (time)            |
|  Data: Car purchased          |
|  Hash: hash_value             | <---
|  Prev_hash: Prev_hash_value   |
'''

"""
-------------------------------------------------------------------------------
                            Test Case #3
-------------------------------------------------------------------------------
"""
print("Test Run #3:")
print()

block_chain = Linked_List()
block_chain.append('Car purchased')
block_chain.append('Cat purchased')
block_chain.append('Dog purchased')
block_chain.append('Car Sold')
block_chain.append('Dragon purchased')
block_chain.append('Cat Sold')
block_chain.print_block()
print('_____________________________________________________________________')


'''
6 block similar to the one below. From the first block to last, the data will be
'Car Purchased', 'Cat purchased', 'Dog Purchased', 'Car Sold', 'Dragon Purchased',
'Cat Sold'. They will each have a unique hash. First block has a previous hash of 0,
and then each proceeding block has previous hash of the previous block in the linked list.
|  Timestamp: (time)            |
|  Data: Car purchased          |
|  Hash: hash_value             | <---
|  Prev_hash: Prev_hash_value   |
'''
"""
-------------------------------------------------------------------------------
                            Test Case #4
-------------------------------------------------------------------------------
"""
print("Test Run #4:")
print()

block_chain = Linked_List()

block_chain.print_block()

block_chain.append('Car purchased')

block_chain.print_block()
print('_____________________________________________________________________')


'''
Block chain is empty
|  Timestamp: (time)            |
|  Data: Car purchased          |
|  Hash: hash_value             | <---
|  Prev_hash: Prev_hash_value   |
'''

"""
-------------------------------------------------------------------------------
                            Test Case #5
-------------------------------------------------------------------------------
"""
print("Test Run #5:")
print()

block_chain = Linked_List()
block_chain.append('One')
block_chain.append('Two')
block_chain.append('Three')
node = block_chain.head
while node:
    print(node.timestamp)
    node = node.get_next()

block_chain.print_block()
print('_____________________________________________________________________')


'''
Same Time stamp 3x
Then 3 blocks with the same time stamp but unique hashes
|  Timestamp: (time)            |
|  Data: Car purchased          |
|  Hash: hash_value             | <---
|  Prev_hash: Prev_hash_value   |
'''
