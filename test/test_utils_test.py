import unittest

from homepage.test_utils import *


class TestUtilsTest(unittest.TestCase):
    def testMockedIsDir(self):
        # Check root
        self.assertTrue(mockedIsDir('/'))
        # Check files are not dirs
        self.assertFalse(mockedIsDir('/index.html'))
        self.assertFalse(mockedIsDir('/blog.html'))
        self.assertFalse(mockedIsDir('/subdir/test.html'))
        self.assertFalse(mockedIsDir('/subdir/test2.html'))
        # Check dirs are dirs
        self.assertTrue(mockedIsDir('/subDir'))
        self.assertTrue(mockedIsDir('/subDir/'))
        # Check the nonexistent files are not dir
        self.assertFalse(mockedIsDir('/nonexistent-dir'))

    def testMockedListDir(self):
        # Check root dir
        self.assertEqual(
            mockedListDir('/'),
            ['index.html', 'blog.html', 'subDir']
        )
        self.assertEqual(mockedListDir('/subDir'), ['test.html', 'test2.html'])


if __name__ == '__main__':
    unittest.main()
