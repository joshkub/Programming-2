import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._checkedListBox1 = System.Windows.Forms.CheckedListBox()
		self.SuspendLayout()
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(167, 162)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(138, 84)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(9, 162)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(138, 84)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Location = System.Drawing.Point(60, 117)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(78, 23)
		self._label1.TabIndex = 16
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(14, 117)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(78, 23)
		self._label2.TabIndex = 17
		self._label2.Text = "Total:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# comboBox3
		# 
		self._comboBox3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["51 mm",
			"55 mm",
			"58 mm",
			"61 mm"]))
		self._comboBox3.Location = System.Drawing.Point(9, 61)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(138, 29)
		self._comboBox3.TabIndex = 15
		self._comboBox3.Text = "Select Wheel..."
		# 
		# comboBox2
		# 
		self._comboBox2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["7.75 axle",
			"8 axle",
			"8.5 axle"]))
		self._comboBox2.Location = System.Drawing.Point(167, 9)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(138, 29)
		self._comboBox2.TabIndex = 14
		self._comboBox2.Text = "Select Truck..."
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["The Master Thrasher",
			"The Dictator of Grind",
			"The Street King"]))
		self._comboBox1.Location = System.Drawing.Point(9, 9)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(138, 29)
		self._comboBox1.TabIndex = 13
		self._comboBox1.Text = "Select Deck..."
		# 
		# checkedListBox1
		# 
		self._checkedListBox1.FormattingEnabled = True
		self._checkedListBox1.Items.AddRange(System.Array[System.Object](
			["Grip Tape",
			"Bearings",
			"Riser Pads",
			"Nuts & bolts kit",
			"Assembly"]))
		self._checkedListBox1.Location = System.Drawing.Point(167, 61)
		self._checkedListBox1.Name = "checkedListBox1"
		self._checkedListBox1.Size = System.Drawing.Size(138, 79)
		self._checkedListBox1.TabIndex = 20
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(322, 267)
		self.Controls.Add(self._checkedListBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "Pg485SkateboardDesigner"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		total = 0
		if self._comboBox1.Text == "The Master Thrasher":
			total+=60
		if self._comboBox1.Text == "The Dictator of Grind":
			total+=45
		if self._comboBox1.Text == "The Street King":
			total+=50
			
		if self._comboBox2.Text == "7.75 axle":
			total+=35
		if self._comboBox2.Text == "8 axle":
			total+=35
		if self._comboBox2.Text == "8.5 axle":
			total+=35
			
		if self._comboBox3.Text == "51 mm":
			total+=20
		if self._comboBox3.Text == "55 mm":
			total+=22
		if self._comboBox3.Text == "58 mm":
			total+=24
		if self._comboBox3.Text == "61 mm":
			total+=28
		
		for item in self._checkedListBox1.CheckedItems:
			if item == "Grip Tape":
				total+=10
			if item == "Bearings":
				total+=30
			if item == "Riser Pads":
				total+=2
			if item == "Nuts & bolts kit":
				total+=3
			if item == "Assembly":
				total+=10
				
		self._label1.Text = str(total)
				
	def Button2Click(self, sender, e):
		self._comboBox1.Text = "Select Deck..."
		self._comboBox2.Text = "Select Truck..."
		self._comboBox3.Text = "Select Wheel..."
		self._label1.Text = ""