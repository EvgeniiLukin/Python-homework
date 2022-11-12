# /* Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
# 0, 7, 8, -2, -2 -> 2
# 1, -7, 567, 89, 223-> 3*/

# int Count(int num)
# {
#     int i = 1;
#     int count = 0;
#     while (num > 0)
#     {
#         Console.Write($"Введите {i} число: ");
#         int n = Convert.ToInt32(Console.ReadLine());
#         if (n > 0) count++;
#         num--;
#         i++;
#     }
#     return count;
# }

# Console.Clear();
# Console.Write("Введите сколько будет чисел: ");
# int n = Convert.ToInt32(Console.ReadLine());
# Console.Write($"Положительных чисел {Count(n)}");

# // Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
# //b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)


# Console.Clear();
# Console.Write("Введите значение b1: ");
# double b1 = Convert.ToInt32(Console.ReadLine());
# Console.Write("Введите значение k1: ");
# double k1 = Convert.ToInt32(Console.ReadLine());
# Console.Write("Введите значение b2: ");
# double b2 = Convert.ToInt32(Console.ReadLine());
# Console.Write("Введите значение k2: ");
# double k2 = Convert.ToInt32(Console.ReadLine());

# double x = (b1 - b2) / (k2 - k1);

# double y = (k2 * b1 - k1 * b2) / (k2 - k1);
# Console.WriteLine($"Точки пересечение двух примых X={x}, Y={y}");



# // Напишите программу, которая найдёт точку пересечения двух прямых, 
# // заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
# // b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)

# void IntersectionPoint(double a1, double c1, double a2, double c2)
# {
#     double x = (a2 - a1) / (c1 - c2);
#     double y = c1 * (a2 - a1) / (c1 - c2) + a1;
#     if(a1 == a2)
#         Console.WriteLine($"точки пересечения параллельны");
#     else
#         Console.WriteLine($"точки пересечения ({x}, {y})");

# }


# Console.Write("input coordinate b1: ");
# double b1 = Convert.ToInt32(Console.ReadLine());
# Console.Write("input coordinate k1: ");
# double k1 = Convert.ToInt32(Console.ReadLine());
# Console.Write("input coordinate b2: ");
# double b2 = Convert.ToInt32(Console.ReadLine());
# Console.Write("input coordinate k2: ");
# double k2 = Convert.ToInt32(Console.ReadLine());

# IntersectionPoint(b1, k1, b2, k2);



# // Console.Write("input coordinate b1: ");
# // double b1 = Convert.ToInt32(Console.ReadLine());
# // Console.Write("input coordinate k1: ");
# // double k1 = Convert.ToInt32(Console.ReadLine());
# // Console.Write("input coordinate b2: ");
# // double b2 = Convert.ToInt32(Console.ReadLine());
# // Console.Write("input coordinate k2: ");
# // double k2 = Convert.ToInt32(Console.ReadLine());

# // double x = (b2 - b1) / (k1 - k2);
# // double y = k1 * (b2 - b1) / (k1 - k2) + b1;

# // Console.WriteLine($"точки пересечения ({x}, {y})");