using System;
using System.IO;
using System.Reflection;
using Manage_class_Flight;
using Newtonsoft.Json;

namespace edu_practice_2
{
    class Menu<T> where T : Flight, new()
    {
        private static Container<T> pc = new Container<T>();
        private static string tName = typeof(T).Name;
        private static string projectPath = Directory.GetParent(Directory.GetCurrentDirectory()).Parent.Parent.FullName;
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
                catch (JsonException e)
                {
                    Console.WriteLine($"Exception: {e.Message}");
                    break;
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
            Console.Write("Enter filename: ");
            string fn = $"{projectPath}/{Console.ReadLine()}";
            pc.Fn = fn;
            pc.ReadFromFile(fn);
            Console.WriteLine("Collection successfully read!");
        }
        
        static void AddMenu()
        {
            T newObj = new T();
            var typeProperties = typeof(T).GetProperties();

            foreach (var prop in typeProperties)
            {
                Console.Write($"Enter {tName} {prop.Name} ({prop.PropertyType}): ");
                string value = Console.ReadLine();
                var typedValue = Convert.ChangeType(value, prop.PropertyType);
                prop.SetValue(newObj, typedValue);
            }

            pc.Add(newObj);
            Console.WriteLine($"{tName} successfully added!");
        }

        static void RemoveMenu()
        {
            Console.Write("Enter ID: ");
            string id = Console.ReadLine();
            pc.Remove(id);
            Console.WriteLine($"{tName} successfully removed!");
        }

        static void FindMenu()
        {
            Console.Write("Enter search query: ");
            string query = Console.ReadLine();
            Container<T> found = pc.Find(query);
            Console.WriteLine($"Found {tName}s:\n{found?.ToString()}");
        }
        
        static void SortMenu()
        {
            Console.Write("Enter property: ");
            string prop = Console.ReadLine();
            pc.Sort(prop);
            Console.WriteLine("Container successfully sorted!");
        }

        static void EditMenu()
        {
            Console.Write("Enter ID: ");
            string id = Console.ReadLine();
            Console.Write("Enter property: ");
            string prop = Console.ReadLine();
            Console.Write("Enter value: ");
            string val = Console.ReadLine();
            pc.Edit(id, prop, val);
            Console.WriteLine($"{tName} successfully edited!");
        }
        
        static void WriteIntoFileMenu()
        {
            Console.Write("Enter filename: ");
            string fn = $"{projectPath}/{Console.ReadLine()}";
            pc.WriteIntoFile(fn);
            Console.WriteLine("Collection successfully written!");
        }
    }
}
