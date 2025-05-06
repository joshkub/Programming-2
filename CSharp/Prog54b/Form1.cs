namespace Prog54b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double num1 = double.Parse(textBox1.Text);
            double num2 = double.Parse(textBox2.Text);
            double sum = num1 + num2;
            double avg = sum / 2;
            label1.Text = sum.ToString();
            label2.Text = avg.ToString();
        }
    }
}