import requests
import os, sys, io
import json
# from screeninfo import get_monitors
import simplejson
from utils import *

date = 0

class spider:
	'''
	date:
		0: today
		-1: tomorrow
		i>0: i days before today
	'''
	def __init__(self, *, date = date, path = 'pic', log = 'log', temp = 'temp'):
		self.bing = 'http://cn.bing.com'
		self.url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(date)+'&n=1' # The Bing Wallpaper API
		self._headers = {
			'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
			'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.8,en-US;q=0.5,en;q=0.3',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15031',
			'Accept-Encoding': 'gzip, deflate, br',
			'Host': 'cn.bing.com',
			'Connection': 'Keep-Alive'
		}
		self._got_pic = False
		self._path = path + os.path.sep
		self._log = log
		self._temp = temp

	def get(self):
		try:
			resp = requests.get(self.url, headers = self._headers).json() # Json format of response
		except simplejson.scanner.JSONDecodeError:
			raise ConnectionError('Network Connection Failed!')
		finally:
			urlbase = resp['images'][0]['urlbase']
			width, height = get_screen_resolution()
			url = '{url}_{width}x{height}.jpg'.format(url = self.bing+urlbase, width = str(width), height = str(height))
			name = url.split('/')[-1]
			print(url)
			pic = requests.get(url, headers = self._headers).content
			if not os.path.isdir(self._path):
				os.makedirs(self._path)
			with open(self._path+name, 'wb') as f:
				f.write(pic)
			with open(self._log, 'a') as f:
				f.write(name+'\n')
			with open(self._temp, 'w') as f:
				f.write(name+'\n')
			self._got_pic = True

	def set(self):
		if not self._got_pic:
			return "Not Done"
		with open(self._temp) as f:
			pic = os.getcwd() + os.path.sep + self._path + f.readline()[:-1]
		if os.name == 'nt':
			win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, 1+2)
		elif os.name == 'posix': # Only support gnome-based desktop here.
			os.system('gsettings set org.gnome.desktop.background picture-uri {pic}'.format(pic = pic))

if __name__ == '__main__':
	S = spider()
	S.get()
	# S.set()