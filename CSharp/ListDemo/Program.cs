//List<string> text = [];
List<string> lines = new List<string>();
// List<int> nums = [1, 2, 3, 4 ];
List<int> nums = new List<int>() { 1, 2, 3, 4, 15 };

nums.Add(4);
nums.Add(5);
nums.Add(6);
nums.Add(7);
nums.RemoveAt(5);
nums.Remove(7);
Console.WriteLine("Length: " + nums.Count);
Console.WriteLine(string.Join(", ", nums));

foreach (int n in nums)
    Console.WriteLine(n);

// Look at C# documentation on MSON for all list methods