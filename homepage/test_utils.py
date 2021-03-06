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
    }
}


def mockedIsDir(filepath):
    """
    A mock of os.isdir. Checks if the path provided is a directory of the
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
