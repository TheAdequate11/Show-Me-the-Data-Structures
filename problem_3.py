import sys

class Internal_Node():

    def __init__(self, value, left, right):
        self.value = value
        self.left_child = left
        self.right_child = right

    #Getters, Setters, and condition checkers
    def get_value(self):
        return self.value
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child

class Node():

    def __init__(self,value, letter):
        self.value = value
        self.letter = letter

    #Getters, Setters, and condition checkers
    def get_letter(self):
        return self.letter
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value


class Min_Heap():

    def __init__(self):
        self.heap_array = []

    def insert(self, node):
        """
        Inserts a node to the end of the heap array; then ensures that the
        value of the node does not break the rules of a min-heap

        Args:
          node (class: Node or Internal_Node): node to be added to the heap
        """
        self.heap_array.append(node)
        self.heapify(self.get_size()-1)

    def heapify(self, current_index):
        """
        Checks to ensure that the value of the node at the given index is
        greater than that of its parent. If not, the parent and child are swapped.
        Heapify is then recursed to ensure that the node - in its new position -
        still meets the conditions.

        Args:
          current_index (int): The index of a node that needs to be checked
        """
        parent_index = int(current_index/2) - 1 if current_index % 2 == 0 and current_index != 0  else int(current_index/2)
        if self.get_node_value(current_index) < self.get_node_value(parent_index):
            self.swap(parent_index,current_index)
            self.heapify(parent_index)

    def swap(self,lower_index, higher_index):
        """
        Swaps the nodes at the two given indices.

        Args:
          lower_index (int): The index of a node at a lower level in the heap tree
          higher_index (int): The index of a node at a higher level in the heap tree
        """
        lower_value = self.heap_array[lower_index]
        higher_value = self.heap_array[higher_index]
        self.set_node_value(lower_index, higher_value)
        self.set_node_value(higher_index, lower_value)

    def extract_min(self):
        """
        Removes and returns the value of the root node. The tree is then resorted;
        has complexity (O(log(n))).

        Return:
          pop_value (class: Node or Internal_Node): The root node/smallest valued node.
        """
        size = self.get_size()
        if size == 0:
            return None
        self.swap(0,size - 1)
        pop_value = self.heap_array.pop()
        def reverse_heapify(index):
            """
            Ensures that the children of the node at the given index are larger
            than that of their parent. If not, smallest child is swapped with parent.
            'reverse_heapify' is then recursed to ensure that the conditions are
            still met with the node in its new position.

            Args:
              index (int): Index of parent node
            """
            left_index = 2*index + 1
            right_index = 2*index + 2
            if left_index >= size - 1:
                return
            elif right_index >= size - 1:
                right_index = left_index
            smaller_child = left_index if self.get_node_value(left_index) <= self.get_node_value(right_index) else right_index
            if self.get_node_value(smaller_child) < self.get_node_value(index):
                self.swap(smaller_child,index)
                reverse_heapify(smaller_child)
            return
        reverse_heapify(0)
        return pop_value

    def print_heap(self):
        """
        Prints min-heap in the form of an array
        """
        print([node.get_value() for node in self.heap_array])

    #Getters, Setters, and condition checkers
    def get_size(self):
        return len(self.heap_array)
    def get_node_value(self, index):
        return self.heap_array[index].get_value()
    def set_node_value(self, index, value):
        self.heap_array[index] = value
    def get_heap(self):
        return self.heap_array



class Huffman_Tree():

    def __init__(self):
        self.root = None

    #Getters, Setters, and condition checkers
    def get_root(self):
        return self.root
    def set_root(self,node):
        self.root = node

"""
-------------------------------------------------------------------------------
                            Defining Functions
-------------------------------------------------------------------------------
"""

def create_priority_queue(data):
    """
    Returns priority queue based on the frequency of letters of the input string.

    Args:
        data (string): Desired string for encoding

    Return:
        priority_queue (class: Min_Heap): Priority queue built from a min-heap
        data structure
    """
    priority_queue = Min_Heap()
    if data:
        letter_frequency = {}
        for letter in data:
            letter_frequency[letter] = letter_frequency.get(letter, 1) + 1
        for letter, frequency in letter_frequency.items():
            priority_queue.insert(Node(frequency,letter))
    return priority_queue

def create_huffman_tree(queue):
    """
    Returns a huffman tree by using the input priority queue.

    Args:
      queue (class: Min_Heap): Priority queue used to sort smallest values

    Return:
        huffman_tree (class:Huffman_Tree): Tree to be used for encoding
    """
    huffman_tree = Huffman_Tree()
    while queue.get_size() > 1:
        small_1 = queue.extract_min()
        small_2 = queue.extract_min()
        sum = small_1.get_value() + small_2.get_value()
        queue.insert(Internal_Node(sum, small_1, small_2))
    huffman_tree.set_root(queue.extract_min())
    return huffman_tree

def define_codes(tree):
    """
    Traverses through the input tree and returns a dictionary containing the codes
    for each leaf's letter value.

    Args:
      tree (class:Huffman_Tree): Huffman tree to be traversed to determine codes

    Returns:
        codes (dictionary): keys are letters and their corresponding values are
        the letters respective code.
    """
    codes = {}
    def traverse(node, code):
        if isinstance(node, Node):
            codes[node.get_letter()] = code
            return
        traverse(node.get_left_child(), code + '0')
        traverse(node.get_right_child(), code + '1')

    traverse(tree.get_root(), '')
    return codes

def huffman_encoding(data):
    """
    Runs through the string replacing each letter with their respective huffman
    code

    Args:
        data (string): Desired string for encoding

    Returns:
        final_code (string): The encoded string of the input data
        huffman_tree (class:Huffman_Tree): Tree to be used for encoding
    """
    if data:
        priority_queue = create_priority_queue(data)
        huffman_tree = create_huffman_tree(priority_queue)
        codes = define_codes(huffman_tree)
        final_code = ''
        for letter in data:
            final_code += codes[letter]
        return final_code, huffman_tree
    return None,None
def huffman_decoding(data,tree):
    """
    Decodes the input string by traversing through the tree and determining
    the letter that corresponds to a code.

    Args:
        data (string): Encoded version of the original input
        huffman_tree (class:Huffman_Tree): Tree to be used for decoding

    Returns:
        string (string): The decoded data which should be equal to the original
        string.
    """
    if data:
        string = ''
        node = tree.get_root()
        for bit in data:
            if bit == '0':
                node = node.get_left_child()
            elif bit == '1':
                node = node.get_right_child()
            if isinstance(node, Node):
                string += node.get_letter()
                node = tree.get_root()
        return string
    return None

"""
-------------------------------------------------------------------------------
                            Test Case #1
-------------------------------------------------------------------------------
"""
print("Test Run #1:")
print()
sentence = 'This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough.'
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: {!r}\n".format(sentence))

encoded_data,tree = huffman_encoding(sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {!r}\n".format(decoded_data))

'''
Expected:

The encoded data will be different every time since a set is unordered.
However, the decoded sentence should say:
This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough. This will be a very long sentence. I am not sure what else I should write except for that fact. I guess: testing, testing; 1, 2 ,3. That seems long enough.
'''

print('_____________________________________________________________________')

"""
-------------------------------------------------------------------------------
                            Test Case #2
-------------------------------------------------------------------------------
"""
print("Test Run #2:")
print()
sentence = ''
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: {!r}\n".format(sentence))

encoded_data,tree = huffman_encoding(sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {!r}\n".format(decoded_data))

'''
Expected:

The decoded sentence should say: None (since there is nothing to encode)
'''
print('_____________________________________________________________________')

"""
-------------------------------------------------------------------------------
                            Test Case #3
-------------------------------------------------------------------------------
"""
print("Test Run #3:")
print()
sentence = None
print ("The size of the data is: {}\n".format(sys.getsizeof(sentence)))
print ("The content of the data is: {!r}\n".format(sentence))

encoded_data,tree = huffman_encoding(sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the decoded data is: {!r}\n".format(decoded_data))

'''
Expected:

The decoded sentence should say: None
'''
print('_____________________________________________________________________')
