from unittest.mock import patch
import unittest
import spider

sample_screen_resolution = (3840, 2160)

class Test(unittest.TestCase):
	@patch('spider.get_screen_resolution', return_value = sample_screen_resolution)
	def test_set(self, mock_get):
		S = spider.spider()
		S.get()
		S.set()

if __name__ == '__main__':
	T = Test()
	T.test_set()