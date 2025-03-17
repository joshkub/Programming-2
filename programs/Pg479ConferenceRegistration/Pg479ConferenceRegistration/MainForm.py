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
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._label7 = System.Windows.Forms.Label()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._label8 = System.Windows.Forms.Label()
		self._textBox8 = System.Windows.Forms.TextBox()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(59, 29)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(115, 20)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(-21, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(74, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Name"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(-21, 53)
		self._label2.Name = "label2"
		self._label2.RightToLeft = System.Windows.Forms.RightToLeft.No
		self._label2.Size = System.Drawing.Size(74, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Company"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(59, 55)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(115, 20)
		self._textBox2.TabIndex = 2
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(-21, 79)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(74, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Address"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(59, 81)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(115, 20)
		self._textBox3.TabIndex = 4
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(-21, 105)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(74, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "City"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(59, 107)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(115, 20)
		self._textBox4.TabIndex = 6
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(179, 28)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(74, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Phone"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(259, 30)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(95, 20)
		self._textBox5.TabIndex = 8
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(179, 51)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(74, 23)
		self._label6.TabIndex = 11
		self._label6.Text = "Email"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(259, 53)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(95, 20)
		self._textBox6.TabIndex = 10
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(196, 104)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(39, 23)
		self._label7.TabIndex = 13
		self._label7.Text = "State"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox7
		# 
		self._textBox7.Location = System.Drawing.Point(237, 106)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(45, 20)
		self._textBox7.TabIndex = 12
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(298, 104)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(39, 23)
		self._label8.TabIndex = 15
		self._label8.Text = "Zip"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox8
		# 
		self._textBox8.Location = System.Drawing.Point(339, 106)
		self._textBox8.Name = "textBox8"
		self._textBox8.Size = System.Drawing.Size(45, 20)
		self._textBox8.TabIndex = 14
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(213, 175)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(69, 23)
		self._label9.TabIndex = 16
		self._label9.Text = "Total Cost:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label9.Click += self.Label9Click
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ControlLight
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label10.Location = System.Drawing.Point(284, 175)
		self._label10.Name = "label10"
		self._label10.RightToLeft = System.Windows.Forms.RightToLeft.Yes
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 17
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label10.Click += self.Label10Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(273, 209)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(119, 42)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 209)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(119, 42)
		self._button1.TabIndex = 21
		self._button1.Text = "Select Conference Options"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(142, 209)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(119, 42)
		self._button2.TabIndex = 22
		self._button2.Text = "Reset"
		self._button2.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(404, 261)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._textBox8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._textBox7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Pg479ConferenceRegistration"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()
		
	def Button1Click(self, sender, e):
		pass
		

	