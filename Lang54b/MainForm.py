import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(18, 42)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(52, 20)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(76, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(23, 30)
		self._label1.TabIndex = 4
		self._label1.Text = "+"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(12, 120)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(62, 20)
		self._label4.TabIndex = 7
		self._label4.Text = "Sum:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(80, 120)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(73, 20)
		self._label5.TabIndex = 8
		self._label5.Text = "Avg:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(105, 42)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(52, 20)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(18, 91)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(52, 20)
		self._textBox3.TabIndex = 11
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(77, 85)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(23, 30)
		self._label3.TabIndex = 12
		self._label3.Text = "+"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(105, 91)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(52, 20)
		self._textBox4.TabIndex = 13
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(109, 20)
		self._label2.TabIndex = 14
		self._label2.Text = "Sum Calculator:"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(1, 143)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(54, 31)
		self._button1.TabIndex = 15
		self._button1.Text = "Calc."
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(61, 143)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(54, 31)
		self._button2.TabIndex = 16
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(121, 143)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(54, 31)
		self._button3.TabIndex = 17
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(175, 186)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang54b"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		sum = num1 + num2 + num3 + num4
		avg = sum / 4
		self._label4.Text = "sum: " + str(sum)
		self._label5.Text = "avg: " + str(avg)
		

	def Button2Click(self, sender, e):
		self._label4.Text = "sum:"
		self._label5.Text = "avg:"