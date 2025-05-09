namespace Pg498
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        const int intMAX_EMPLOYEES = 5;
        const decimal decHOURLY_PAY_RATE = 6.0m;
        private void button1_Click(object sender, EventArgs e)
        {
            // calc and display gross pay earned by employees
            int[] intHours = new int[intMAX_EMPLOYEES]; // An array
            // <type>[] varName = new<type>[capacity];
            int Count = 0;
            int EmpHours = 0;
            decimal EmpPay = 0;

            for (Count = -; Count < intMAX_EMPLOYEES; Count++)
            {
                while (int.TryParse(
                    Interaction.InputBox("Enter # of hours worked by employee #") +
                    (Count+1).ToString(), "need Hours worked"),
                    out EmpHours) == false) {
                MessageBox.Show("Please enter an ineger for hours worked");
            }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }
}