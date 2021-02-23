using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text.Json;
using Newtonsoft.Json;
using JsonSerializer = Newtonsoft.Json.JsonSerializer;

namespace edu_practice_1
{
    public class ProductContainer
    {
        private List<Product> _products;
        private readonly Type _typeP = typeof(Product);
        private string _fn;
        
        public ProductContainer(string fn = null, List<Product> list = null)
        {
            _fn = fn;
            _products = list != null ? new List<Product>(list) : new List<Product>();
        }

        public int Length => _products.Count;

        public string Fn
        {
            get => _fn;
            set => _fn = Validation.ValidateFileName(value);
        }

        public override string ToString()
        {
            string str = "";
            foreach (var p in _products)
            {
                str += $"{p.ToString()}\n\n";
            }

            return str;
        }

        
        public void Sort(string property)
        {
            property = char.ToUpper(property[0]) + property.Substring(1);
            property = Validation.ValidateProperty(property, _typeP);
            
            PropertyInfo prop = _typeP.GetProperty(property);
            _products = _products.OrderBy(
                p => prop.GetValue(p)
                ).ToList();
            
            WriteIntoFile(_fn);
        }

        
        public ProductContainer Find(string keyword)
        {
            keyword = keyword.ToLower();
            List<Product> results = new List<Product>();
            PropertyInfo[] props = _typeP.GetProperties(
                BindingFlags.Instance | BindingFlags.Public);

            foreach (var prop in props)
            {
                List<Product> found = _products.FindAll(p =>
                    Convert.ToString(prop.GetValue(p)).ToLower().Contains(keyword));
                
                if (found.Count != 0)
                {
                    foreach (var product in found)
                    {
                        results.Add(product);
                    }
                }
            }

            return results.Count == 0 ? null : new ProductContainer(list: results.Distinct().ToList());
        }

        
        public void Add(Product product)
        {
            _products.Add(product); 
            
            WriteIntoFile(_fn);
        }
        
        
        public Product Remove(Guid id)
        {
            Product product = _products.Find(p => p.ID == id);
            _products.Remove(product);
                        
            WriteIntoFile(_fn);
            return product;
        }

        
        public void Edit(Guid id, string property, string value)
        { 
            property = char.ToUpper(property[0]) + property.Substring(1);
            property = Validation.ValidateProperty(property, _typeP);
            PropertyInfo prop = _typeP.GetProperty(property);

            var typedValue = Convert.ChangeType(value, prop.PropertyType);
            Product product = _products.Find(p => p.ID == id);
            prop.SetValue(product, typedValue);

            WriteIntoFile(_fn);
        }


        public void ReadFromFile(string fn)
        {
            fn = Validation.ValidateFileName(fn);
            
            StreamReader sr = new StreamReader(fn);
            string json = sr.ReadToEnd();
            var list = JsonConvert.DeserializeObject<List<Dictionary<String, String>>>(json);
            foreach (var dict in list)
            {
                try
                {
                    Product p = JsonConvert.DeserializeObject<Product>(JsonConvert.SerializeObject(dict));
                    _products.Add(p);
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
            sr.Close();
        }

        
        public void WriteIntoFile(string fn)
        {
            fn = Validation.ValidateFileName(fn);
            string productsJson = JsonConvert.SerializeObject(_products, Formatting.Indented);
            File.WriteAllText(fn, productsJson);
        }
    }
}