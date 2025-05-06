namespace Pg266
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a = int.Parse(textBox1.Text);
            int b = int.Parse(textBox2.Text);
            if (a < b)
            {
                label1.Text = "B is greater than value A";
            }
            else if (a > b)
            {
                label1.Text = "A is greater than value B";
            }
            else
            {
                label1.Text = "Equal values";
            }
        }
    }
}