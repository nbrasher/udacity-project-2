## Problem 5: Blockchain

For this problem I implemented the `Block` class as shown in the problem definition, and added a `Blockchain` class. I also added a `__repr__` function to each class for clarity's sake. `Block().__repr__` will print the block's timestamp, data and previous hash. `Blockchain().__repr__` will print the length of the Blockchain in total blocks, as well as the head block's data.

The time and storage complexity for this process is O(1). In order to add a block to the chain, all that is needed is a hash of the current blocks data, and the previous block's hash value. The computational complexity will not change as the block grows, because only the last block is needed, and no iteration is involved.

The Blockchain is implemented as a linked list, and therefore space complexity will grow as O(n).

In `problem_5.py` I've added a section with `if __name__ == '__main__'` that will run if you run the file in the command line. Each print statement is commented with the expected output. I've also added a few `assert` statements that were used in development to ensure correct behavior.