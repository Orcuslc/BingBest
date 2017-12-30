from unittest.mock import patch
import unittest
import download
import utils

sample_screen_resolution = ['1920', '1080']

class Test(unittest.TestCase):
	@patch('utils.get_screen_resolution', return_value = sample_screen_resolution)
	def test_get(self, mock_get):
		S = download.Downloader()
		S.get()

	def test_resolution(self):
		got = utils.get_screen_resolution()
		true = sample_screen_resolution
		self.assertEqual(got, true)

T = Test()
T.test_get()
T.test_resolution()