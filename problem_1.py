'''
Show me the data structures
Problem 1: LRU cache
'''

class LinkedListNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.array = [None for _ in range(capacity)]
        self.capacity = capacity


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        bucket_index = self.get_bucket_index(key)
        head = self.array[bucket_index]

        # Traverse dict to find key
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        
        # If key not found
        return -1


    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.array[bucket_index]
        new_node.next = head
        self.array[bucket_index] = new_node


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


    assert our_cache.get(1) == 1    # returns 1
    assert our_cache.get(2) == 2    # returns 2
    assert our_cache.get(9) == -1   # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    assert our_cache.get(3) == -1   # returns -1 because the cache reached it's capacity

