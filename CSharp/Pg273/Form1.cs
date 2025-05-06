namespace Pg273
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int book = int.Parse(textBox1.Text);
            if (book <= 0)
            {
                label3.Text = "0";
            }
            else if (book == 1)
            {
                label3.Text = "5";
            }
            else if (book == 2)
            {
                label3.Text = "15";
            }
            else if (book == 3)
            {
                label3.Text = "30";
            }
            else label3.Text = "60";
        }
    }
}