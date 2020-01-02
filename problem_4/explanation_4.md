## Problem 4: Active Directory

To solve this problem, I used a simple application of recursion, first searching the top-level group's users for the provided user and then recursively searching sub-groups with the same method. If a user is found in a sub-group, the function will return True. If the users are not found in the top-level group or any sub-groups, the function will return False.

As explained for the similar recursive solution in problem 2, this process involves iterating through every user in each subgroup, and is therefore O(n). The space complexity should also be O(n) as it involves storing the entire user / group structure in memory. The recursive nature of the algorithm will also use a call stack to track recusion depth, which is O(n) for space complexity as well.

In `problem_4.py` I've added a section with `if __name__ == '__main__'` that will run if you run the file in the command line. Each print statement is commented with the expected output. I've also added a few `assert` statements that were used in development to ensure correct behavior.