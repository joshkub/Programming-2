namespace WinFormsApp1{
    public partial class Form1 : Form{ 
        public Form1()
    {
        InitializeCompenent();
    }

        private ListBox listBox1;
        private Button button1;
        private Button button2;
    }

    private void button1_click(object sender, EventArgs e)
    {
        Random rand = new Random();
        for (int lcv = 0; lcv < rand.Next(5,11); lcv++)
        {
            double freq = rand.Next(0, 21) + rand.NextDouble();
            string msg = "";
            int stars +(int)Math.Round(freq);
            for (int i = 0; i < stars; i++)
                msg += "*";
            msg += " " + Math.Round(freq, 2);
        }
    }
    

    