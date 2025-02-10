import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(111, 30)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(161, 27)
		self._textBox1.TabIndex = 12
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(162, 165)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 59)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(27, 165)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 59)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(111, 110)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(161, 27)
		self._label4.TabIndex = 9
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(12, 110)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 8
		self._label2.Text = "Anagrams"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 34)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "Enter text 1:"
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(111, 69)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(161, 27)
		self._textBox2.TabIndex = 14
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 73)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 13
		self._label3.Text = "Enter text 2:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightSeaGreen
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "strint2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label4.Text = ""
		word1 = self._textBox1.Text.lower()
		word2 = self._textBox2.Text.lower()
		
		if len(word1) != len(word2):
			self._label4.Text = "False"
			return
		else:
			for lcv in range(len(word1)):
				c = word1[lcv]
				index = word2.find(c)
				if index == -1:
					self._label4.Text = "False"
				else:
					word2 = word2[0:index] + word2[index+1:]
		self._label4.Text = str(len(word2) == 0)
		pass
					