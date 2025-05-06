namespace Prog85c
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double ynumber = double.Parse(textBox1.Text);
            double ybirthday = (ynumber - 165) / 100;
            label2.Text = ybirthday.ToString();
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            textBox1.Text = "";
        }
    }
}