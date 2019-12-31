## Problem 6: Union and Intersection 

I used the code structure from the problem definition, and defined `union` and `intersection` functions. Both functions take two linked lists as input and output a sorted Python list.

Finding the union of two sets requires looping through each linked list to find unique values, and then merging the two lists in a single list of unique values. On the face of it this is O(n + m). However, because the input lists are not sorted, at each step through the list, I also check if that value is in the current list containing the intersection of each linked list, because this involves iterating through a list which will grow to n, so this algorithm is worst case O(n * m). The space complexity is O(n + m) as it involves storing each linked list in memory.

By a similar token, calculating the intersection of each list iteratively involves iterating over each element in list O(n), and comparing it to each element in list2 O(n * m) - I then also compare it to the current union list to make sure that value is unique O(n * m * k) where k is the total number of elements in the resulting union. Thus the algorithm as written is worst case O(n^3) if calculating the union of two identical linked lists. As stated above the space complexity is O(n + m).

In `problem_6.py` I've added a section with `if __name__ == '__main__'` that will run if you run the file in the command line. Each print statement is commented with the expected output. I've also added a few `assert` statements that were used in development to ensure correct behavior.