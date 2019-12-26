'''
Show me the data structures
Problem 2: File Recursion
'''
import os


def find_files(suffix, path):
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

    return file_list


if __name__ == '__main__':
    file_list = find_files('.c', os.path.join(os.path.dirname(__file__), 
                                              'testdir'))
    
    if file_list:
        for f in file_list:
            print(f)
    else:
        print('No files found')
