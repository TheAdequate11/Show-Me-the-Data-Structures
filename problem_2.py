import os
import os.path

"""
-------------------------------------------------------------------------------
                            Defining Functions
-------------------------------------------------------------------------------
"""

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
    path_list = []
    if suffix == None or path == None:
        return 'Null values are not permitted'
    if os.path.isdir(path):
        for dir in os.listdir(path):
            path_list.extend(find_files(suffix,os.path.join(path,dir)))
    elif os.path.isfile(path):
        if path[-1*len(suffix):-1] + path[-1] == suffix:
            path_list.append(path)
    return path_list

"""
-------------------------------------------------------------------------------
                            Test Case #1
------------------------------------------------------------------------------
"""
print("Test Run #1:")
print()
file = 'testdir_problem_2'
suffix = '.c'

print(find_files(suffix,file))

#Expected: [testdir_problem_2\t1.c, testdir_problem_2\subdir1\a.c, testdir_problem_2\subdir3\subsubdir1\b.c, testdir_problem_2\subdir5\a.c]
print('_______________________________________________________________________')


"""
-------------------------------------------------------------------------------
                            Test Case #2
-------------------------------------------------------------------------------
"""
print("Test Run #2:")
print()
file = 'testdir_problem_2\subdir3'
suffix = '.h'

print(find_files(suffix,file))

#Expected: [testdir_problem_2\subdir3\subsubdir1\b.h]
print('_______________________________________________________________________')

"""
-------------------------------------------------------------------------------
                            Test Case #3
-------------------------------------------------------------------------------
"""
print("Test Run #3:")
print()
file = 'testdir_problem_2'
suffix = '.'

print(find_files(suffix,file))
#Expected: []
print('_______________________________________________________________________')

"""
-------------------------------------------------------------------------------
                            Test Case #4
-------------------------------------------------------------------------------
"""
print("Test Run #4:")
print()
file = 'testdir_problem_2'
suffix = ''

print(find_files(suffix,file))
#Expected: []
print('_______________________________________________________________________')

"""
-------------------------------------------------------------------------------
                            Test Case #5
-------------------------------------------------------------------------------
"""
print("Test Run #5:")
print()
file = 'testdir_problem_2'
suffix = None

print(find_files(suffix,file))
#Expected: 'Null values are not permitted'
