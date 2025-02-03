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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 255)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 64)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(208, 255)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 64)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(115, 255)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(91, 64)
		self._button3.TabIndex = 2
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(88, 34)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(78, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 31)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(70, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "Radius:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 104)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(194, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Radius:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 149)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(194, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Area:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 191)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(194, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "Circumference:"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(321, 331)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		area = 3.14159 * (num1 ** 2)	
		circum = 2 * 3.14159 * num1
		self._label2.Text = "Raidus: " + str(num1)
		self._label3.Text = "Area: " + str(area)
		self._label4.Text = "Circumference: " + str(circum)
		
	def Button3Click(self, sender, e):
		self._label2.Text = "Raidus: "
		self._label3.Text = "Area: "
		self._label4.Text = "Circumference: " 
	
	def Button2Click(self, sender, e):
		application.exit()