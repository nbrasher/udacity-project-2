'''
Show me the data structures
Problem 5: Blockchain
'''
import time
import hashlib


class Block:

    def __init__(self, timestamp, data, previous=None):
        
        self.timestamp = timestamp
        self.data = str(data)
        self.previous = previous

        # Get previous blocks hash
        if self.previous:
            self.previous_hash = self.previous.hash
        else:
            self.previous_hash = None

        self.hash = self.calc_hash()


    # Calculate SHA-256 hash of input data
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = hash_str = f'{self.timestamp}\n{self.data}\n{self.previous_hash}'.encode('utf-8')
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
            block = Block(timestamp=time.time(), 
                        data=data,
                        previous=self.head)
        else:
            block = Block(timestamp=time.time(), 
                        data=data)

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
    
    first_hash = bc.head.hash

    print(bc) # Should print the first block with data "First block data"

    bc.add_block('Second block data')

    # Test that blockchain is being built properly
    print(bc) # Should show the head with data "Second block data"

    # Assert that previous_hash is the hash of the first block
    assert bc.head.previous_hash == first_hash, 'Incorrect first hash value'

    # Should handle non-string data, and show a head block with data '1234'
    bc.add_block(1234)
    print(bc)

    # Assert that can traverse to the first block and that hash is still correct
    assert bc.head.previous.previous_hash == first_hash, 'Incorrect first hash value'


    # Empty Blockchain
    bc = BlockChain()

    # Should print 'Blockchain with 0 blocks'
    print(bc)
    