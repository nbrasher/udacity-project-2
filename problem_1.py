'''
Show me the data structures
Problem 1: LRU cache
'''
from collections import deque


class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

        # Add attributes to track access order
        self.before = None
        self.after = None


class LRU_Cache:

    def __init__(self, capacity: int = 5):
        # Initialize class variables
        self.array = [None for _ in range(capacity)]
        self.capacity = capacity
        self.num_entries = 0

        # Head and tail of access order list
        self.most_recent = None
        self.least_recent = None


    def get(self, key):
        # Return value if present, -1 if no node returned
        try:
            return self.get_node(key).value
        except:
            return -1


    def set(self, key, value):
        bucket_index = self.get_bucket_index(key)
        
        new_node = LinkedListNode(key, value)
        head = self.array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.array[bucket_index]
        new_node.next = head
        self.array[bucket_index] = new_node
        self.num_entries += 1


    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next


    def get_node(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.array[bucket_index]

        # Traverse dict to find key
        while head is not None:
            if head.key == key:
                return head
            head = head.next
        
        # If key not found
        return None

    
    def get_bucket_index(self, key):
        # Simplest possible hash function for integers
        return key % self.capacity


if __name__ == '__main__':
    our_cache = LRU_Cache(5)

    # Fill cache
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    # Access order tracking for insertion
    assert our_cache.most_recent.value == 4, 'Incorrect tracking of most_recent for insertion'

    # Expected behavior when returning existing keys
    assert our_cache.get(1) == 1, 'Failed to return (1)'
    assert our_cache.most_recent.value == 1, 'Incorrect tracking of most_recent for access'
    assert our_cache.get(2) == 2, 'Failed to return (2)'
    assert our_cache.least_recent.value == 3, 'Incorrect tracking of least_recent'

    # Expected behavior for unset keys
    assert our_cache.get(9) == -1, 'Failed to return -1 for missing value'

    # Fill cache so that LRU falls out
    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1, 'Failed to return -1 for removed value'
