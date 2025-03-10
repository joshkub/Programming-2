
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._panel1 = System.Windows.Forms.Panel()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(82, 144)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(64, 27)
		self._button2.TabIndex = 7
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 144)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(64, 27)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# panel1
		# 
		self._panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel1.Controls.Add(self._label8)
		self._panel1.Controls.Add(self._label7)
		self._panel1.Controls.Add(self._label6)
		self._panel1.Controls.Add(self._label5)
		self._panel1.Controls.Add(self._label4)
		self._panel1.Controls.Add(self._label3)
		self._panel1.Controls.Add(self._textBox1)
		self._panel1.Controls.Add(self._label2)
		self._panel1.Location = System.Drawing.Point(12, 12)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(131, 126)
		self._panel1.TabIndex = 8
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(80, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(35, 20)
		self._textBox1.TabIndex = 6
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(15, 21)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(69, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "# of Tickets:"
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(66, 100)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(49, 23)
		self._label8.TabIndex = 12
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(66, 75)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(49, 23)
		self._label7.TabIndex = 11
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(66, 51)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(49, 23)
		self._label6.TabIndex = 10
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(17, 100)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(49, 23)
		self._label5.TabIndex = 9
		self._label5.Text = "Total"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(17, 75)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(49, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Tax:"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(15, 51)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(51, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Tickets:"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(19, 7)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(89, 23)
		self._label1.TabIndex = 13
		self._label1.Text = "Student Section:"
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(158, 176)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._panel1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "Form2"
		self.Text = "Form2"
		self._panel1.ResumeLayout(False)
		self._panel1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		tickets = int(self._textBox1.Text)
		self._textBox1.Text = str(tickets)
		ticketprice = 7
		ticketcost = ticketprice * tickets
		tax = ticketcost * 0.06
		total = ticketcost + tax
		self._label6.Text = str(tickets)
		self._label7.Text = str(tax)
		self._label8.Text = str(total)