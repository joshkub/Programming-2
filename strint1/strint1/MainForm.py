import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter text:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(12, 89)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Duplicates:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(111, 89)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(161, 27)
		self._label4.TabIndex = 3
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(27, 141)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 59)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(162, 141)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 59)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(111, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(161, 27)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Teal
		self.ClientSize = System.Drawing.Size(300, 212)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "strint1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label4.Text = ""
		myStr = self._textBox1.Text.lower()
		for lcv in range(len(myStr)):
			for lcv2 in range(lcv+1, len(myStr)):
				ltr1 = myStr[lcv]
				ltr2 = myStr[lcv2]
				if ltr1 == ltr2:
					self._label4.Text += ltr2 + " "

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text = ""