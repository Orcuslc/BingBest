from unittest.mock import patch
import unittest
import BingWall
import utils

sample_screen_resolution = (1920, 1080)

class Test(unittest.TestCase):
	@patch('BingWall.get_screen_resolution', return_value = sample_screen_resolution)
	def test_get(self, mock_get):
		S = BingWall.spider()
		S.get()

if __name__ == '__main__':
	T = Test()
	T.test_get()