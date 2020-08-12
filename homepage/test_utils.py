"""
Collection of mocked functions which can be used in tests.
"""

import os

fileSystem = {
    'index.html': None,
    'blog.html': None,
    'subDir': {
        'test.html': None,
        'test2.html': None,
        'anotherSubDir': {},
    }
}


def mockedIsDir(filepath):
    """
    A mock of os.path.isdir. Checks if the path provided is a directory of the
    fake fileSystem.
    """
    assert filepath[0] == "/"
    if filepath == "/":
        return True
    root = fileSystem
    normpath = os.path.normpath(filepath)
    split = normpath.split(os.sep)[1:]
    for filename in split:
        if filename not in root or not isinstance(root[filename], dict):
            return False
        root = root[filename]
    return True


def mockedListDir(filepath):
    """
    A mock of os.listdir. Returns a list of files in the path provided.
    """
    assert filepath[0] == "/"
    if filepath == "/":
        return list(fileSystem.keys())
    root = fileSystem
    normpath = os.path.normpath(filepath)
    split = normpath.split(os.sep)[1:]
    listdir = list(fileSystem.keys())
    for filename in split:
        if filename not in root or not isinstance(root[filename], dict):
            raise ValueError("invalid filepath given")
        root = root[filename]
        listdir = list(root)
    return listdir


def mockedMakeDir(filepath):
    """
    A mock of os.mkdir. Creates the directory in our mock filesystem and exist.
    """
    if mockedIsDir(filepath):
        raise FileExistsError(
            "[Mock] [Errno 17] File exists: '{0}'".format(filepath))
    if not mockedIsDir(os.path.dirname(filepath)):
        raise FileNotFoundError("[Mock] [Errno 2] No such file or directory: '{0}'".format(
            os.path.dirname(filepath)))
    else:
        split = os.path.normpath(filepath).split(os.sep)
        root = fileSystem
        for filename in split[1:-1]:
            root = root[filename]
        root[split[-1]] = {}


mos = object()
mos.path = object()
mos.mkdir = mockedMakeDir
mos.listdir = mockedListDir
mos.path.isdir = mockedIsDir
mos.path.join = os.path.join
