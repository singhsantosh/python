import os

list_of_paths = []


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

    # Base Case
    if len(os.listdir(path)) == 0:
        return list()

    for file_or_dir in sorted(os.listdir(path)):

        file_or_dir = os.path.join(path, file_or_dir)

        if os.path.isdir(file_or_dir):
            find_files(suffix, file_or_dir)
        if os.path.isfile(file_or_dir) and file_or_dir.endswith(suffix):
            print("file = {}".format(file_or_dir))
            list_of_paths.append(file_or_dir)

    return list_of_paths


suffix = ".c"
path = "../testdir/"

actual_output = find_files(suffix, path)
correct_output = ['../testdir/subdir1/a.c', '../testdir/subdir3/subsubdir1/b.c', '../testdir/subdir5/a.c', '../testdir/t1.c']

if actual_output == correct_output:
    print("pass")
else:
    print("fail")