from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class GUI(QWidget):
	"""
	GUI for BingBest
	"""
	def __init__(self):
		super().__init__()
		self.style = """
		QPushButton{background-color:grey}