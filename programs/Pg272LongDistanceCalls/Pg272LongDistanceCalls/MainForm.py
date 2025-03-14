import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["AM",
			"PM"]))
		self._comboBox1.Location = System.Drawing.Point(124, 24)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(55, 29)
		self._comboBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(62, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Time:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(61, 24)
		self._textBox1.MaxLength = 2
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(26, 29)
		self._textBox1.TabIndex = 2
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(4, 70)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Length:"
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(93, 24)
		self._textBox2.MaxLength = 2
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(25, 29)
		self._textBox2.TabIndex = 4
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(124, 70)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "(minutes)"
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(71, 67)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(47, 29)
		self._textBox3.TabIndex = 6
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(84, 27)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(16, 23)
		self._label4.TabIndex = 7
		self._label4.Text = ":"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(32, 116)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(137, 55)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(230, 27)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(114, 23)
		self._label5.TabIndex = 9
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(230, 70)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(81, 23)
		self._label6.TabIndex = 10
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(181, 27)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(73, 23)
		self._label7.TabIndex = 11
		self._label7.Text = "Time:"
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(183, 70)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(73, 23)
		self._label8.TabIndex = 12
		self._label8.Text = "Cost:"
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft YaHei UI", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(199, 116)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(137, 55)
		self._button2.TabIndex = 13
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.MenuHighlight
		self.ClientSize = System.Drawing.Size(370, 189)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label3)
		self.Name = "MainForm"
		self.Text = "Pg272LongDistanceCalls"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		hour = int(self._textBox1.Text)
		minute = int(self._textBox2.Text)
		length = int(self._textBox3.Text)
		num = 0
		if self._comboBox1.Text == "PM":
			num += (hour * 60) + (12 * 60)
		if self._comboBox1.Text == "AM":
			num += hour * 60
		total = num + minute
		self._label5.Text = str(total)
		if total >= 360 and total <= 1079:
			self._label5.Text = "Day Time"
			self._label6.Text = "$" + str(float(length * 0.07))
		if total >= 1080 and total <= 1439:
			self._label5.Text = "Evening"
			self._label6.Text = "$" + str(float(length * 0.12))
		if total >= 1440 or total <= 359:
			self._label5.Text = "Off-Peak"
			self._label6.Text = "$" + str(float(length * 0.05))
		else:
			MessageBox.Show("Invalid Input")
			
		
			