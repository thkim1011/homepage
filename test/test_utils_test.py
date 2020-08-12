import unittest

from homepage.test_utils import *


class TestUtilsTest(unittest.TestCase):
    def test_mocked_isdir(self):
        # Check root
        self.assertTrue(mockedIsDir('/'))
        # Check files are not dirs
        self.assertFalse(mockedIsDir('/index.html'))
        self.assertFalse(mockedIsDir('/blog.html'))
        self.assertFalse(mockedIsDir('/subDir/test.html'))
        self.assertFalse(mockedIsDir('/subDir/test2.html'))
        # Check dirs are dirs
        self.assertTrue(mockedIsDir('/subDir'))
        self.assertTrue(mockedIsDir('/subDir/'))
        self.assertTrue(mockedIsDir('/subDir/anotherSubDir'))
        # Check the nonexistent files are not dir
        self.assertFalse(mockedIsDir('/nonexistent-dir'))

    def test_mocked_listdir(self):
        # Check root dir
        self.assertEqual(
            mockedListDir('/'),
            ['index.html', 'blog.html', 'subDir']
        )
        self.assertEqual(mockedListDir('/subDir'),
                         ['test.html', 'test2.html', 'anotherSubDir'])

    def test_mocked_mkdir(self):
        mockedMakeDir('/subDir/newdir')
        self.assertTrue(mockedIsDir('/subDir/newdir'))


if __name__ == '__main__':
    unittest.main()
