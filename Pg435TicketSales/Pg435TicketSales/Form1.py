
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self.Name = "Form1"
		self.Text = "Form1"

