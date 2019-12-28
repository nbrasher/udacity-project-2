'''
Show me the data structures
Problem 2: File Recursion
'''
import os


def find_files(suffix: str, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    assert isinstance(suffix, str), 'Input suffix should be a string'
    assert isinstance(path, str), 'Input suffix should be a string or filepath object'

    file_list = list()

    if os.path.isdir(path):
        # Loop through all files and directories
        for f in os.listdir(path):

            # If item is a file, check if ends with suffix
            if os.path.isfile(os.path.join(path,f)):
                if f.endswith(suffix):
                    file_list.append(os.path.join(path,f))

            # If item is a sub-directory, continue search recursively
            elif os.path.isdir(os.path.join(path,f)):
                file_list.extend(find_files(suffix, 
                                            os.path.join(path, f)))
    else:
        print('Invalid file path')
        return

    return file_list


if __name__ == '__main__':
    file_list = find_files('.c', os.path.join(os.path.dirname(__file__), 
                                              'testdir'))
    
    # The following should print the full file paths of t1.c as well as
    # subdir1/a.c, subdir5/a.c and subdir3/subsubdir1/b.c
    if file_list:
        for f in file_list:
            print(f)
    print('\n')

    # Should print a statement that the folder does not exist
    file_list = find_files('.c', 'not-a-directory')
    print('\n')

    # Should raise an error that the filepath is not a string or file object
    file_list = find_files('.c', None)
