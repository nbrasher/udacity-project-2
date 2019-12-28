'''
Show me the data structures
Problem 5: Blockchain
'''
import time
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        assert isinstance(data, str), 'Block data should be a string'
        
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()


    # Calculate SHA-256 hash of input data
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


    def __repr__(self):
        output = 'Block____\n'
        output += 'Time: {}\n'.format(self.timestamp)
        output += 'Data: {}\n'.format(self.data)
        output += 'Prev Hash: {}\n'.format(self.previous_hash)
        return output


# Example blockchain class
class BlockChain:

    def __init__(self):
        # Keep track of head of Blockchain
        self.head = None
        self.length = 0

    
    # Add block to blockchain
    def add_block(self, data):
        if self.head:
            previous_hash = self.head.hash
        else:
            previous_hash = None

        block = Block(timestamp=time.time(), 
                      data=data,
                      previous_hash=previous_hash)
        
        self.head = block
        self.length += 1
    

    def __repr__(self):
        output = 'Blockchain with {} blocks\n'.format(self.length)
        
        if(self.head):
            output += '\nHead block:\n'
            output += self.head.__repr__()
        
        return output


if __name__ == '__main__':
    # Build test blockchain
    bc = BlockChain()
    bc.add_block('First block data')

    print(bc) # Should print the first block with data "First block data"

    bc.add_block('Second block data')

    # Build test hash of first block data
    sha = hashlib.sha256()
    sha.update('First block data'.encode('utf-8'))
    first_hash = sha.hexdigest()

    # Test that blockchain is being built properly
    print(bc) # Should show the head with data "Second block data"

    # Assert that previous_hash is the hash of "First block data"
    assert bc.head.previous_hash == first_hash, 'Incorrect previous hash value'

    # Should raise an error if the blockchain tries to add a block with an non-string value
    bc.add_block(1234)
    