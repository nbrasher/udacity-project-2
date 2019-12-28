'''
Show me the data structures
Problem 3: Huffman Encoding
'''
from collections import defaultdict
import sys


# Binary Tree node with additional frequency attribute
class Node(object): 
    def __init__(self, 
                 value = None,
                 frequency: int = 0):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None


# Binary Tree
class Tree():
    def __init__(self, 
                 value = None,
                 frequency: int = 0):
        self.root = Node(value=value, frequency=frequency)
    
    # Define comparison operator for trees
    def __lt__(self, tree2):
        return self.root.frequency < tree2.root.frequency

    # Huffman combination for trees
    def combine(self, tree2):
        old_root = self.root
        new_root = Node(frequency=(old_root.frequency + \
                                   tree2.root.frequency))
        new_root.left = old_root
        new_root.right = tree2.root
        self.root = new_root


# Custom class for Huffman encoding
class Huffman():
    def __init__(self):
        self.queue = list()
        self.tree = None
        self.codes = dict()


    def encode(self, data: str):
        if not isinstance(data, str):
            print('String required for input')
            return
        elif not data:
            print('Input string is empty')
            return
        
        # Lower-case input string and build queue
        data=data.lower()
        self._build_queue(data)

        # Build Huffman tree and get encoding values
        self._build_tree()
        self._get_codes(self.tree.root, '')

        # Encode data string
        return ''.join([self.codes[c] for c in data])


    def decode(self, data: str):
        # Huffman decoding
        decode = ''
        i=0
        while i < len(data):
            # Start at root, traverse tree until value found
            node = self.tree.root
            while node.left or node.right:
                if data[i] == '1':
                    node = node.left
                else:
                    node = node.right
                i += 1
            decode += node.value
        
        return decode


    def _build_queue(self, data):
        # Iterate through characters in string and build queue
        queue_dict = defaultdict(int)
        for c in data:
            queue_dict[c] += 1
        
        # Create queue as sorted list of trees
        self.queue = [Tree(value=k, frequency=v)
                      for k,v in queue_dict.items()]
        self.queue.sort()
    

    def _build_tree(self):
        # Build Huffman Tree
        while len(self.queue) > 1:
            # Combine top two items
            tree1 = self.queue.pop(0)
            tree2 = self.queue.pop(0)
            tree1.combine(tree2)

            # Add the resultant tree to queue and sort
            self.queue.append(tree1)
            self.queue.sort()

        # When the queue is down to a single element, this is the tree
        self.tree = self.queue[0]
    

    def _get_codes(self, node, code):
        # Extract codes from Huffman Tree with pre-order traversal
        if node:
            if node.left is None and node.right is None:
                self.codes[node.value] = code
            else:
                self._get_codes(node.left, code+'1')
                self._get_codes(node.right, code+'0')


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    # Encode data with custom Huffman class
    huff = Huffman()
    encoded_data = huff.encode(a_great_sentence)

    # Test for proper building of the queue
    assert huff.queue, 'Empty queue'
    assert huff.queue[0].root.frequency == 20, 'Incorrect first element frequency'

    # Test for proper building of the tree
    assert huff.tree, 'Empty tree'
    assert huff.tree.root.frequency == 20, 'Incorrect frequency count on root node'

    # Test for proper encoding
    assert huff.codes, 'Empty codes dict'
    assert huff.codes[' '] == '001', 'Incorrect code for the single space'

    # Evaluate quality of results
    # Expect to see size of data is 69 plus the example string
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    # Expect to see size of data is less than original plus a binary string
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huff.decode(encoded_data)

    # Expect to see the original size and string, in lower case form
    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test that encoding raises a warning if the input is not a string
    huff.encode(12345)

    # Test that encoding raises a warning if the input is an empty string
    huff.encode('')