import os
if os.name == 'nt':
	import win32gui, win32api, win32con
import ctypes
import subprocess

def get_screen_resolution():
	if os.name == 'nt':
		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
	else:
		p = subprocess.Popen('xrandr', stdout = subprocess.PIPE)
		p2 = subprocess.Popen(['grep', '*'], stdin = p.stdout, stdout = subprocess.PIPE)
		p.stdout.close()
		r, _ = p2.communicate()
		resolution = str(r.split()[0], encoding = 'utf-8')
		return resolution.split('x')