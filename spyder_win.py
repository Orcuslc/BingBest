# /usr/bin/python3

import requests
from datetime import datetime
import re
import os 
import sys
import win32gui, win32con, win32api
# import commands

class Spyder:
	'''
	The main spyder of http://cngsetting.bing.com
	'''
	def __init__(self):
		self.url = 'http://cn.bing.com'
		self.headers = {
			# GET / HTTP/1.1
			# Host: cn.bing.com
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			# 'Accept-Encoding': 'gzip, deflate',
			'Cookie': 'SRCHD=AF=NOFORM; SRCHUSR=AUTOREDIR=0&GEOVAR=&DOB=20151012; _EDGE_V=1; MUID=0CE7C23214D167F31B81CA0C1570667F; SRCHHPGUSR=LUT=1449746523786&IPMH=85776a66&IPMID=1449750765366&CW=1376&CH=707&DPR=1.3953487873077393; KievRPSAuth=FABSARRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACDtIXF0yFG%2BpEAG02TLa02%2B3hs4BDIazbk7j/RXpZ8D/GNB3i7i39tt0V5r%2B8Im6zlY1YykKJHvwgGbjsN3AZzASPz1i8KFOSPw1fzz02w0O3s9vUwwn8EyeEzsExybmA8cz0ZpCgyzeQd%2BxS1XqhPAoCF7jUokSLV9KcHUe/B5EJP4k0%2Bh7AQBYxDWyLkBkluGYHrPseQtM/U8QhuiBimDyEBtXBGl7LdAIgLUuZ3cEI7lgUM92ajEt5mT13zU9%2BxAuWgQU3gYufH7vGmWZIlqv/AezQ5S6nc1egNCL1NJ0A7Eackvsaju3KVFJb7mQxxITvzrNWSYe47ZEIZJXvtBPN%2B7MzvjCCWoIWz2Hsv%2BL9bqGVyqh8Jl6NRQAtN2HAi6pc/qbO1CEOCXzoA/KcAg%3D; PPLState=1; ANON=A=C3E80C0DFD9C27AB9E93D8E6FFFFFFFF&E=1216&W=1; NAP=V=1.9&E=11bc&C=eF9fuBH3_MxysfzlmrQlvLFAmZtlU3MjmdgpEQjRYRLQM9c2qxy91g&W=1; MUIDB=0CE7C23214D167F31B81CA0C1570667F; SRCHUID=V=2&GUID=30F59CFE6A7D4857BFF43171FAEC59C5; WLID=9FA805Gvny+qAFUD+7Ii1PvIAq3picp8F/GsTKd3M+m5ZyqLhlcjPWxwKw899gq7g1YYlLfpanArFDhbXNTxYLy+QZ7x8MTNnlDVOXVoH0o=; _U=1pfGUt9-GvTGl1G9qpdsQBVsTLhglylPIVd_MwQ9S7Y8sfRLLxiRd64TVoT_N_9oQE065Dl8dPVmzHLC_mgBMUm569254A77UiRoT9wcEKFpFljjq1x0aqB9VhErDBjlP; HPSHRLAN=CLOSE=1; _SS=SID=381CBB6DEAA364323233B38FEB026557&bIm=308772&HV=1458817829; _EDGE_S=SID=381CBB6DEAA364323233B38FEB026557; SCRHDN=ASD=0&DURL=#',
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
		}
		self.save_route = '.\\saved\\'
		self.pic_route = None
		self.dir = None

	def get_page(self):
		try:
			page = requests.get(url = self.url, headers = self.headers)
		finally:
			# print(page.text)
			pic = re.findall(r'url\(http.*\.jpg\)', page.text)
			print(pic)
			pic_url = pic[0][4:-1]
			# print(pic_url)
			pic = requests.get(url = pic_url, headers = self.headers)
			pic_name = re.findall(r'/.*?\.jpg', pic_url)[0]
			pic_name = pic_name.split('/')[-1]
			self.pic_route = self.save_route + pic_name
			try:
				f = open(self.pic_route, 'wb')
			except FileNotFoundError:
				os.mkdir(self.save_route)
			finally:
				f = open(self.pic_route, 'wb')
			f.write(pic.content)
			f.close()

	def setWallpaperFromBMP(self):
		k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
		win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "2") #2拉伸适应桌面,0桌面居中
		win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
		win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,self.pic_route, 1+2)
 
	def setWallPaper(self):
		"""
		Given a path to an image, convert it to bmp and set it as wallpaper
		"""
		bmpImage = Image.open(self.pic_route)
		newPath = StoreFolder + '\\%c.bmp'%()
		bmpImage.save(newPath, "BMP")
		setWallpaperFromBMP(newPath)


	def get_dir(self):
		self.dir = sys.path[0]
		print(self.dir)

	def run(self):
		self.get_page()
		self.set_background()

if __name__ == '__main__':
	spyder = Spyder()
	spyder.run()