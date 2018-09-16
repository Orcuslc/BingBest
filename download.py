import requests
import logging
import os
import json
from utils import *

class Downloader:

	def __init__(self, date = 0, country = 'cn', save_path = 'pic', log_path = 'bingbest.log'):
		'''
		date:
			0: today
			-1: tomorrow
			i>0: i days before today
		'''
		self.bing = 'http://{}.bing.com'.format(country)
		self.url = '{}/HPImageArchive.aspx?format=js&idx={}&n=1'.format(self.bing, date) # The Bing Wallpaper API
		self._headers = {
			'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
			'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15031',
			'Accept-Encoding': 'gzip, deflate, br',
			'Host': 'www.bing.com',
			'Connection': 'Keep-Alive'
		}
		self._save_path = save_path + os.path.sep
		if not os.path.isdir(self._save_path):
			os.makedirs(self._save_path)
		logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level = logging.INFO, filename=log_path)
		self._got_pic = False
		

	def get(self):
		try:
			resp = requests.get(self.url, headers = self._headers).json()
		except requests.exceptions.ConnectionError:
			logging.critical("Network connection failed")
			return
		urlbase = resp['images'][0]['urlbase']
		width, height = get_screen_resolution()
		url = '{}_{}x{}.jpg'.format(self.bing+urlbase, width, height)
		name = url.split('/')[-1]
		pic = requests.get(url, headers = self._headers).content
		with open(self._save_path+name, 'wb') as f:
			f.write(pic)
		logging.info("Get image {}".format(name))
		self._got_pic = True
		self._image = self._save_path + name

	def set(self):
		if not self._got_pic:
			print("Failed to get picture, please check network connection.")
			return
		pic = os.getcwd() + os.path.sep + self._image
		if os.name == 'nt':
			win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, 1+2)
		else:
			# Only support gnome now
			os.system("./gnome_set_wallpaper.sh " + pic)


if __name__ == '__main__':
	d = Downloader()
	d.get()