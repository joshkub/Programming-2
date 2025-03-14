import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular Shades",
			"Folding Shades",
			"Roman Shades"]))
		self._comboBox1.Location = System.Drawing.Point(12, 12)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(138, 29)
		self._comboBox1.TabIndex = 6
		self._comboBox1.Text = "Select Style..."
		self._comboBox1.SelectedIndexChanged += self.ComboBox1SelectedIndexChanged
		# 
		# comboBox2
		# 
		self._comboBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 in. wide",
			"27 in. wide",
			"32 in. wide",
			"40 in. wide"]))
		self._comboBox2.Location = System.Drawing.Point(170, 12)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(138, 29)
		self._comboBox2.TabIndex = 7
		self._comboBox2.Text = "Select Size..."
		self._comboBox2.SelectedIndexChanged += self.ComboBox2SelectedIndexChanged
		# 
		# comboBox3
		# 
		self._comboBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural",
			"Blue",
			"Teal",
			"Red",
			"Green"]))
		self._comboBox3.Location = System.Drawing.Point(12, 99)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(138, 29)
		self._comboBox3.TabIndex = 8
		self._comboBox3.Text = "Select Color..."
		self._comboBox3.SelectedIndexChanged += self.ComboBox3SelectedIndexChanged
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Location = System.Drawing.Point(208, 101)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 9
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(158, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 10
		self._label2.Text = "Total:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label2.Click += self.Label2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 165)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(138, 84)
		self._button1.TabIndex = 11
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(170, 165)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(138, 84)
		self._button2.TabIndex = 12
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(320, 261)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "Pg485ShadeDesigner-OneForm"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def RadioButton4CheckedChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
	self._label1.Text = ""
	self._comboBox1.Text = "Select Style..."
	self._comboBox2.Text = "Select Size..."
	self._comboBox3.Text = "Select Color..."

	def Button1Click(self, sender, e):
		Total = 0
		if self._comboBox1.Text == "Regular Shades":
			Total += 0
		if self._comboBox1.Text == "Folding Shades":
			Total += 10
		if self._comboBox1.Text == "Roman Shades":
			Total += 15
			
		if self._comboBox2.Text == "25 in. wide":
			Total += 0
		if self._comboBox2.Text == "27 in. wide":
			Total += 2
		if self._comboBox2.Text == "32 in. wide":
			Total += 4
		if self._comboBox2.Text == "40 in. wide":
			Total += 6
			
		if self._comboBox3.Text == "Natural":
			Total += 5
		if self._comboBox3.Text == "Blue":
			Total += 0
		if self._comboBox3.Text == "Teal":
			Total += 0
		if self._comboBox3.Text == "Red":
			Total += 0
		if self._comboBox3.Text == "Green":
			Total += 0
			
		self._label1.Text = str(Total)
			

	def MainFormLoad(self, sender, e):
		pass