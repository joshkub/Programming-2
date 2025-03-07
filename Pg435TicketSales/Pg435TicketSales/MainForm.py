import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._panel1 = System.Windows.Forms.Panel()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(174, 3)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(81, 40)
		self._button1.TabIndex = 0
		self._button1.Text = "General Sales"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(174, 55)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(81, 40)
		self._button2.TabIndex = 1
		self._button2.Text = "Student Sales"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# panel1
		# 
		self._panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel1.Controls.Add(self._button1)
		self._panel1.Controls.Add(self._button2)
		self._panel1.Location = System.Drawing.Point(12, 12)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(260, 100)
		self._panel1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(23, 7)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(98, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Select the Type of Ticket Sales"
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(185, 130)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(81, 25)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 167)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._panel1)
		self.Name = "MainForm"
		self.Text = "Pg435TicketSales"
		self._panel1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import*
		form1 = Form1(self)
		form1.Show()
		self.Hide()
		
	def Button2Click(self, sender, e):
		from Form2 import*
		form2 = Form2(self)
		form2.Show()
		self.Hide()
