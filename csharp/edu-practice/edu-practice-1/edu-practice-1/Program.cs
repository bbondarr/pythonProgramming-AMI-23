using System;
using System.Collections.Generic;

namespace edu_practice_1
{
    class Menu
    {
        private static ProductContainer pc = new ProductContainer();
        static void Main()
        {
            Console.WriteLine("WELCOME TO PRODUCTS MENU");
            Console.WriteLine();
            while (true)
            {
                try
                {
                    ReadFromFileMenu();
                    break;
                }
                catch (Exception e)
                {
                    Console.WriteLine(e.Message);
                }
            }

            bool menuState = true;
            while (menuState)
            {
                Console.WriteLine("Choose one of the following operations:\n"+
                                  "1 - Print all products\n"+
                                  "2 - Add a product from input\n"+
                                  "3 - Delete product by ID\n"+
                                  "4 - Find product\n"+
                                  "5 - Sort the container\n"+
                                  "6 - Edit product\n"+
                                  "7 - Write into file\n"+
                                  "8 - Exit");
                string menuChoice = Console.ReadLine();
                try
                {
                    switch (menuChoice)
                    {
                        case "1": Console.WriteLine(pc.ToString());
                            break;
                        case "2": AddMenu();
                            break;
                        case "3": RemoveMenu();
                            break;
                        case "4": FindMenu();
                            break;
                        case "5": SortMenu();
                            break;
                        case "6": EditMenu();
                            break;
                        case "7": WriteIntoFileMenu();
                            break;
                        case "8": menuState = false;
                            break;
                        default: Console.WriteLine("Bad value");
                            break;
                    }
                }
                catch (Exception e)
                {
                    Console.WriteLine($"Exception: {e.Message}");
                    if (e.InnerException != null)
                    {
                        Console.WriteLine($"Inner Exception: {e.InnerException.Message}");
                    }
                }
            }
        }

        static void ReadFromFileMenu()
        {
            Console.WriteLine("Enter filename: ");
            string fn = Console.ReadLine();
            pc.Fn = fn;
            pc.ReadFromFile(fn);
            Console.WriteLine("Collection successfully read!");
        }
        
        static void AddMenu()
        {
            Console.WriteLine("Enter Product title (str): ");
            string t = Console.ReadLine();
            Console.WriteLine("Enter Product image URL (url str): ");
            string i = Console.ReadLine();
            Console.WriteLine("Enter Product price (float): ");
            double p = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Enter Product creation date (date str): ");
            DateTime c = Convert.ToDateTime(Console.ReadLine());
            Console.WriteLine("Enter Product update date (date str): ");
            DateTime u = Convert.ToDateTime(Console.ReadLine());
            Console.WriteLine("Enter Product description (str): ");
            string d = Console.ReadLine();
            
            pc.Add(new Product(t, d, i, p, c, u));
            Console.WriteLine("Product successfully added!");
        }

        static void RemoveMenu()
        {
            Console.WriteLine("Enter ID: ");
            Guid id = Guid.Parse(Console.ReadLine());
            pc.Remove(id);
            Console.WriteLine("Product successfully removed!");
        }

        static void FindMenu()
        {
            Console.WriteLine("Enter search query: ");
            string query = Console.ReadLine();
            ProductContainer found = pc.Find(query);
            Console.WriteLine($"Found products:\n{found.ToString()}");
        }
        
        static void SortMenu()
        {
            Console.WriteLine("Enter property: ");
            string prop = Console.ReadLine();
            pc.Sort(prop);
            Console.WriteLine("Container successfully sorted!");
        }

        static void EditMenu()
        {
            Console.WriteLine("Enter ID: ");
            Guid id = Guid.Parse(Console.ReadLine());
            Console.WriteLine("Enter property: ");
            string prop = Console.ReadLine();
            Console.WriteLine("Enter value: ");
            string val = Console.ReadLine();
            pc.Edit(id, prop, val);
            Console.WriteLine("Product successfully edited!");
        }
        
        static void WriteIntoFileMenu()
        {
            Console.WriteLine("Enter filename: ");
            string fn = Console.ReadLine();
            pc.WriteIntoFile(fn);
            Console.WriteLine("Collection successfully written!");
        }
    }
}