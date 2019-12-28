'''
Show me the data structures
Problem 1: LRU cache
'''


# Node that also tracks access order
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
        self.array = [None for _ in range(capacity)]
        self.capacity = capacity
        self.num_entries = 0

        # Head and tail of access order list
        self.most_recent = None
        self.least_recent = None


    def get(self, key):
        # Return value if present, -1 if no node returned
        try:
            node = self.get_node(key)

            # Update tracking of which node was accessed
            self.update_access_order(node)

            return self.get_node(key).value
        except:
            return -1


    def set(self, key, value):
        assert isinstance(key, int), 'Cache keys must be integers'
        bucket_index = self.get_bucket_index(key)
        
        new_node = LinkedListNode(key, value)
        head = self.array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                self.update_access_order(new_node)
                return
            head = head.next

        # If a new value needs to be inserted, first check capacity
        if self.num_entries == self.capacity:
            self.delete_last(self.least_recent.key)

        # Insert new node
        head = self.array[bucket_index]
        new_node.next = head
        self.array[bucket_index] = new_node
        self.update_access_order(new_node)
        self.num_entries += 1


    # Delete the least recently accessed node
    def delete_last(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.array[bucket_index]

        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.array[bucket_index] = head.next
                else:
                    previous.next = head.next

                # Update num_entries and least_recent attributes
                self.num_entries -= 1
                self.least_recent = head.before
                return
            else:
                previous = head
                head = head.next


    # Update tracking of most recently accessed node
    def update_access_order(self, node):
        current_most_recent = self.most_recent

        # If insertion order is empty, set new node to most and least recent
        # Otherwise set node to head of access order list
        if self.most_recent is None:
            self.most_recent = node
            self.least_recent = node
        else:
            # If node is already in list, re-link list
            if node.before is not None:
                node.before.after = node.after

                # If node is least_recent, update
                if self.least_recent is node:
                    self.least_recent = node.before

            # Set node to the head of access order 
            node.before = None
            node.after = current_most_recent
            current_most_recent.before = node
            self.most_recent = node


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

    # Test access order tracking for insertion
    assert our_cache.most_recent.value == 4, 'Incorrect tracking of most_recent for insertion'

    # Test behavior when returning existing keys
    print(our_cache.get(1)) # should print 1
    assert our_cache.most_recent.value == 1, 'Incorrect tracking of most_recent for access'
    print(our_cache.get(2)) # should print 2
    assert our_cache.least_recent.value == 3, 'Incorrect tracking of least_recent'

    # Test behavior for unset keys
    print(our_cache.get(9)) # should print -1

    # Fill cache so that LRU falls out
    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    # Test expected beahvior for least recent value
    print(our_cache.get(3)) # should print -1

    # If initialized with no capacity, capacity should be equal to 5
    our_cache = LRU_Cache()
    print(our_cache.capacity) # should print 5

    # If given a non-integer key, should raise an error
    our_cache.set('a', 5)