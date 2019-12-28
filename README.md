## Udacity Project 1: Show me the Data Structures
Nathan Brasher 12.27.19  

My solutions to each problem in the project are stored in files named `problem_1.py` through `problem_6.py`

For problem 6, my run-time analysis is below:

#### Problem 6 run-time analysis
Finding the union of two sets requires looping through each linked list to find unique values, and then merging the two lists in a single list of unique values. On the face of it this is O(n). However, because the input lists are not sorted, at each step through the list, I also check if that value is in the current list containing the intersection of each linked list, because this involves iterating through a list which will grow to n, so this algorithm is worst case O(n^2).

By a similar token, calculating the intersection of each list iteratively involves iterating over each element in list O(n), and comparing it to each element in list2 O(n^2) - I then also compare it to the current union list to make sure that value is unique O(n^3). Thus the algorithm as written is worst case O(n^3).
