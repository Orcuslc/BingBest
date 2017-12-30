import win32gui, win32api, win32con
import ctypes

def get_screen_resolution():
	user32 = ctypes.windll.user32
	user32.SetProcessDPIAware()
	return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

