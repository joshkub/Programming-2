using static System.Console;
Write("Enter radius: ");
double rad = int.Parse(ReadLine());

double area = rad * rad * 3.14159;
double circ = 2 * 3.14159 * rad;
WriteLine("Radius: " + rad);
WriteLine("Area: " + Math.Round(area, 2));
WriteLine("Circumference: " + Math.Round(circ, 2));
ReadKey();