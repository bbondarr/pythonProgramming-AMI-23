using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using Newtonsoft.Json;

namespace edu_practice_2
{
    /*
     * Works perfectly with classes that:
     * - have id property
     * - are json-serializable
     */
        public class Container<T>
    {
        private List<T> _tlist;
        private readonly Type _type = typeof(T);
        
        private string _fn;
        
        public Container(string fn = null, List<T> list = null)
        {
            _fn = fn;
            _tlist = list != null ? new List<T>(list) : new List<T>();
        }

        public int Length => _tlist.Count;

        public string Fn
        {
            get => _fn;
            set => _fn = Validation.ValidateFileName(value);
        }

        // actually ToJson() ¯\_(ツ)_/¯
        public override string ToString()
        {
            string str = "";
            foreach (var obj in _tlist)
            {
                str += $"{JsonConvert.SerializeObject(obj, Formatting.Indented)},\n";
            }

            return str;
        }

        
        public void Sort(string property)
        {
            property = char.ToUpper(property[0]) + property.Substring(1);
            property = Validation.ValidateProperty(property, _type);
            
            PropertyInfo propInfo = _type.GetProperty(property);
            _tlist = _tlist.OrderBy(o => propInfo.GetValue(o)).ToList();
            
            WriteIntoFile(_fn);
        }

        
        public Container<T> Find(string keyword)
        {
            keyword = keyword.ToLower();
            List<T> results = new List<T>();
            var props = _type.GetProperties(
                BindingFlags.Instance | BindingFlags.Public).ToList();
            
            props.ForEach(p => 
                results.AddRange(_tlist.FindAll(o =>
                    Convert.ToString(p.GetValue(o)).ToLower().Contains(keyword))));

            return results.Count == 0 ? null : new Container<T>(list: results.Distinct().ToList());
        }

        
        public void Add(T obj)
        {
            _tlist.Add(obj); 
            
            WriteIntoFile(_fn);
        }
        
        
        public T Remove(Guid id)
        {
            var idProperty = _type.GetProperties()
                .ToList()
                .Find(p => p.Name.ToLower() == "id");
            
            // Other possible realisation, a bit more narrow-minded
            //var idProperty = _type.GetProperty("Id");

            T obj = _tlist.Find(o => 
                idProperty.GetValue(o).ToString() == id.ToString()); 
            _tlist.Remove(obj);
                
            WriteIntoFile(_fn);
            return obj;
        }

        
        public void Edit(Guid id, string property, string value)
        { 
            property = char.ToUpper(property[0]) + property.Substring(1);
            property = Validation.ValidateProperty(property, _type);
            PropertyInfo propInfo = _type.GetProperty(property);

            var typedValue = Convert.ChangeType(value, propInfo.PropertyType);
            
            var idProperty = _type.GetProperties()
                .ToList()
                .Find(p => p.Name.ToLower() == "id");

            T obj = _tlist.Find(o => 
                idProperty.GetValue(o).ToString() == id.ToString());
            propInfo.SetValue(obj, typedValue);

            WriteIntoFile(_fn);
        }


        public void ReadFromFile(string fn)
        {
            fn = Validation.ValidateFileName(fn);
            
            StreamReader sr = new StreamReader(fn);
            string json = sr.ReadToEnd();
            var list = JsonConvert.DeserializeObject<List<Dictionary<String, String>>>(json);
            string errorMessage = "";
            foreach (var dict in list)
            {
                try
                {
                    T obj = JsonConvert.DeserializeObject<T>(JsonConvert.SerializeObject(dict));
                    _tlist.Add(obj);
                }
                catch (Exception e)
                {
                    errorMessage += $"Exception: {e.Message}\n";
                }
            }
            if (errorMessage != "") throw new JsonException(errorMessage);
            
            sr.Close();
        }

        
        public void WriteIntoFile(string fn)
        {
            fn = Validation.ValidateFileName(fn);
            string listJson = JsonConvert.SerializeObject(_tlist, Formatting.Indented);
            File.WriteAllText(fn, listJson);
        }
    }
}