import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._panel1 = System.Windows.Forms.Panel()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# panel1
		# 
		self._panel1.Controls.Add(self._label3)
		self._panel1.Controls.Add(self._label2)
		self._panel1.Controls.Add(self._button2)
		self._panel1.Controls.Add(self._button1)
		self._panel1.Location = System.Drawing.Point(12, 12)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(260, 152)
		self._panel1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(152, 24)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 50)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(152, 99)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 50)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(28, 5)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Select Ticket Type:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(16, 24)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(130, 50)
		self._label2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(16, 99)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(130, 50)
		self._label3.TabIndex = 4
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(164, 170)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 29)
		self._button3.TabIndex = 5
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 201)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._panel1)
		self.Name = "MainForm"
		self.Text = "Pg435"
		self._panel1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from pubticket import*
		pubticket.show()
		self.Hide()