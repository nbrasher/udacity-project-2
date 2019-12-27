'''
Show me the data structures
Problem 3: Huffman Encoding
'''
from collections import defaultdict
import sys


class Huffman():
    def __init__(self):
        self.queue = list()
        self.tree = None
        self.codes = dict()


    def encode(self, data):
        # Lower-case input string and build queue
        self._build_queue(data.lower())

        # Build Huffman tree and get encoding values
        self._built_tree()
        self._get_codes()

        # TODO: Encode data string
        return ''


    def decode(self, data):
        # TODO: Decode data string
        return ''


    def _build_queue(self, data):
        # Iterate through characters in string and build queue
        queue_dict = defaultdict(int)
        for c in data:
            queue_dict[c] += 1
        
        # Create queue as sorted list of tuples with frequency first
        self.queue = [(v,k) for k,v in queue_dict.items()]
        self.queue.sort()
    

    def _built_tree(self):
        # TODO: Build Huffman Tree
        return
    

    def _get_codes(self):
        # TODO: Extract codes from Huffman Tree
        return


if __name__ == "__main__":

    a_great_sentence = "The bird is the word"

    # Encode data with custom Huffman class
    huff = Huffman()
    encoded_data = huff.encode(a_great_sentence)

    # Test for proper building of the queue
    assert huff.queue, 'Empty queue'
    assert huff.queue[0] == (1,'b'), 'Incorrect first element'

    # Test for proper building of the tree
    assert huff.tree, 'Empty tree'
    assert huff.tree.root.value == 20, 'Incorrect frequency count on root node'

    # Test for proper encoding
    assert huff.codes, 'Empty codes dict'
    assert huff.codes[' '] == '10', 'Incorrect code for the single space'

    # Evaluate quality of results
    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huff.decode(encoded_data)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
