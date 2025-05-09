using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSales
{
    public partial class Form3 : Form
    {
        private Form myParent;

        public Form3(Form myParent)
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }
        private void button4_Click(object sender, EventArgs e)
        {
            double tktPrice = 7;
            double tktAmount = int.Parse(textBox2.Text);

            // Calculation
            double tktTax = (tktPrice * tktAmount) * 0.06;
            double total = (tktPrice * tktAmount) + tktTax;

            // Output
            label13.Text = tktAmount.ToString();
            label14.Text = tktTax.ToString();
            label15.Text = total.ToString();
        }
     }
 }