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
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCoral
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 239)
		self._button1.Name = "button1"
		self._button1.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._button1.Size = System.Drawing.Size(124, 53)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCoral
		self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(163, 239)
		self._button2.Name = "button2"
		self._button2.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._button2.Size = System.Drawing.Size(124, 53)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCoral
		self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(317, 239)
		self._button3.Name = "button3"
		self._button3.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._button3.Size = System.Drawing.Size(124, 53)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightCoral
		self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label1.Location = System.Drawing.Point(12, 31)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(429, 187)
		self._label1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 64, 64)
		self.ClientSize = System.Drawing.Size(452, 304)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Hello"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Hello, World!"

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()