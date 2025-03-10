
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.myparent = parent
	
	def InitializeComponent(self):
		self._panel1 = System.Windows.Forms.Panel()
		self._panel2 = System.Windows.Forms.Panel()
		self._panel3 = System.Windows.Forms.Panel()
		self._panel4 = System.Windows.Forms.Panel()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._panel1.SuspendLayout()
		self._panel2.SuspendLayout()
		self._panel4.SuspendLayout()
		self.SuspendLayout()
		# 
		# panel1
		# 
		self._panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel1.Controls.Add(self._textBox1)
		self._panel1.Controls.Add(self._label2)
		self._panel1.Controls.Add(self._panel3)
		self._panel1.Location = System.Drawing.Point(12, 12)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(260, 76)
		self._panel1.TabIndex = 0
		# 
		# panel2
		# 
		self._panel2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel2.Controls.Add(self._radioButton3)
		self._panel2.Controls.Add(self._radioButton2)
		self._panel2.Controls.Add(self._radioButton1)
		self._panel2.Location = System.Drawing.Point(12, 94)
		self._panel2.Name = "panel2"
		self._panel2.Size = System.Drawing.Size(99, 116)
		self._panel2.TabIndex = 1
		# 
		# panel3
		# 
		self._panel3.Location = System.Drawing.Point(105, 82)
		self._panel3.Name = "panel3"
		self._panel3.Size = System.Drawing.Size(155, 116)
		self._panel3.TabIndex = 2
		# 
		# panel4
		# 
		self._panel4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel4.Controls.Add(self._label8)
		self._panel4.Controls.Add(self._label7)
		self._panel4.Controls.Add(self._label6)
		self._panel4.Controls.Add(self._label5)
		self._panel4.Controls.Add(self._label4)
		self._panel4.Controls.Add(self._label3)
		self._panel4.Location = System.Drawing.Point(120, 94)
		self._panel4.Name = "panel4"
		self._panel4.Size = System.Drawing.Size(152, 116)
		self._panel4.TabIndex = 2
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(26, 6)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(102, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "How many Tickets?"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(3, 14)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Section 1"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(3, 44)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Section 2"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(3, 74)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Section 3"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(23, 20)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(51, 23)
		self._label3.TabIndex = 0
		self._label3.Text = "Tickets:"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(25, 44)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(49, 23)
		self._label4.TabIndex = 1
		self._label4.Text = "Tax:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(25, 69)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(49, 23)
		self._label5.TabIndex = 2
		self._label5.Text = "Total"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(55, 215)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(73, 27)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(149, 215)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(73, 27)
		self._button2.TabIndex = 5
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = True
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(74, 20)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(49, 23)
		self._label6.TabIndex = 3
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(74, 44)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(49, 23)
		self._label7.TabIndex = 4
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(74, 69)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(49, 23)
		self._label8.TabIndex = 5
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(105, 51)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(69, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "# of Tickets:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(170, 48)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(61, 20)
		self._textBox1.TabIndex = 4
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(284, 245)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._panel4)
		self.Controls.Add(self._panel2)
		self.Controls.Add(self._panel1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._panel1.ResumeLayout(False)
		self._panel1.PerformLayout()
		self._panel2.ResumeLayout(False)
		self._panel4.ResumeLayout(False)
		self.ResumeLayout(False)

	def Button1Click(self, sender, e):
		tickets = int(self._textBox1.Text)
		self._textBox1.Text = str(tickets)
		if self._radioButton1.Checked:
			ticketprice = 20
		elif self._radioButton2.Checked:
			ticketprice = 15
		elif self._radioButton3.Checked:
			ticketprice = 10
		ticketcost = ticketprice * tickets
		tax = ticketcost * 0.06
		total = ticketcost + tax
		self._label6.Text = str(tickets)
		self._label7.Text = str(tax)
		self._label8.Text = str(total)
		

