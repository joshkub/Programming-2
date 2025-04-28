Console.Write("Enter length: ");
int length = int.Parse(Console.ReadLine());
Console.Write("Enter height: ");
int height = int.Parse(Console.ReadLine());

double hypo = Math.Round(Math.Sqrt(length * length + height * height), 2);
int area = (length * height) / 2;
double peri = Math.Round(hypo + length + height, 2);
Console.WriteLine("Hypotonuse: " + hypo);
Console.WriteLine("Area: " + area);
Console.WriteLine("Perimeter: " + peri);





