'''
Show me the data structures
Problem 6: Union and Intersection
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    union = list()
    
    # Loop through each list in sequence to get unique values
    node = llist_1.head
    while node:
        if node.value not in union:
            union.append(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value not in union:
            union.append(node.value)
        node = node.next
    
    union.sort()
    return union


def intersection(llist_1, llist_2):
    intersection = list()
    
    # Loop through both lists to compare values
    node1 = llist_1.head
    while node1:
        node2 = llist_2.head
        while node2:
            if node1.value == node2.value:
                if node1.value not in intersection:
                    intersection.append(node1.value)
                break
            node2 = node2.next
        node1 = node1.next

    intersection.sort()
    return intersection


if __name__ == '__main__':
    # Build test case 1
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    # Each of the print statements should show the expected output of the assert statement below
    print(union(linked_list_1,linked_list_2)) 
    print(intersection(linked_list_1,linked_list_2))
    assert union(linked_list_1,linked_list_2) == [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]
    assert intersection(linked_list_1,linked_list_2) == [4, 6, 21]


    # Build test case 2
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    # Each of the print statements should show the expected output of the assert statement below
    print (union(linked_list_3,linked_list_4))
    print (intersection(linked_list_3,linked_list_4))
    assert union(linked_list_3,linked_list_4) == [1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65]
    assert intersection(linked_list_3, linked_list_4) == []


    # Build an empty linked list test case, should return [] in both cases
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()

    print (union(linked_list_5,linked_list_6))
    print (intersection(linked_list_5,linked_list_6))