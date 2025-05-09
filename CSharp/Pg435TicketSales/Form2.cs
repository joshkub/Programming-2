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
    public partial class Form2 : Form
    {
        private Form myParent;
        public Form2(Form myParent)
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            // Input
            double tktPrice = 0;
            double tktAmount = int.Parse(textBox1.Text);

            // Section Selector
            if (radioButton1.Checked)
            {
                tktPrice = 20;
            }
            else if (radioButton2.Checked)
            {
                tktPrice = 15;
            }
            else if (radioButton3.Checked)
            {
                tktPrice = 10;
            }
            else
            {
                MessageBox.Show ("No Section Selected");
                
            };

            // Calculation
            double tktTax = (tktPrice * tktAmount) * 0.06;
            double total = (tktPrice * tktAmount) + tktTax;

            // Output
            label5.Text = tktAmount.ToString();
            label6.Text = tktTax.ToString();
            label7.Text = total.ToString();
        } 
            
        

    }
}
