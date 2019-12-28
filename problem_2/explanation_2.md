## Problem 2: File Recursion

To solve this problem, I used a simple application of recursion, first creating a list of local files that matched the provided `suffix` and then recursively searching sub-directories with the same method. If files that match that pattern are found in subdirectories, they are added to the list of file matches.

In `problem_2.py` I've added a section with `if __name__ == '__main__'` that will run if you run the file in the command line. This section tests `find_files` against the example directory structure provided in the problem description. Expected output is detailed in the comments.