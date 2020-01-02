## Problem 1: LRU Cache  

For this problem, I implemented an extension of the Python OrderedDict class to track access order. This structure ensures constant-time lookup and storage. 

In order to also satisfy the requirement of a fixed-size cache, I tracked access (insertion or read) order for each key-value pair. As the OrderedDict class already tracks insertion order, I reset keys whenever they are accessed (using the `.get` method, or `.set` method when key is already present) to ensure the cache tracks access order. Because this only involves manipulating a single key, the operations are still done in O(1) constant time. When the cache is at capacity, I use the `.popitem(last=False)` functionality to remove the item that has been least-recently accessed or set.

The space complexity of the underlying data structure is O(n), as each key-value pair is stored separately.

In `problem_1.py` I've added a section with `if __name__ == '__main__'` that will run if you run the file in the command line. Each print statement is commented with the expected output. I've also added a few `assert` statements that were used in development to ensure correct behavior.