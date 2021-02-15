using System;
using System.Linq;
using System.Text.RegularExpressions;

namespace edu_practice_1
{
    public static class Validation
    {
        public static string ValidateName(string value)
        {
            if (value.All(c => Char.IsLetter(c) || c == ' '))
            {
                return value;
            }
            throw new FormatException($"String value must be a string consisting only letters and spaces, {value} was given");
        }

        public static string ValidateUrl(string value)
        {
            string pattern = @"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)";
            if (Regex.IsMatch(value, pattern))
            {
                return value;
            }
            throw new FormatException($"String value must be a URL, {value} was given");
        }

        public static double ValidatePrice(double value)
        {
            if (value > 0.0)
            {
                return value;
            }

            throw new ArgumentOutOfRangeException("Price", $"Float value must be positive, {value} was given");
        }

        public static DateTime ValidateDate(DateTime value, DateTime other = new DateTime())
        {
            if (value < DateTime.Now && (other == DateTime.MinValue || value >= other))
            {
                return value;
            }
            throw new ArgumentOutOfRangeException("UpdatedAt", $"DateTime value must be from past (less or equal than CreatedAt), {value} was given");
        }
        
        public static string ValidateFileName(string value)
        {
            if (value.EndsWith(".json") || value.EndsWith(".txt"))
            {
                return value;
            }
            throw new FormatException($"String value must be .json ot .txt format, {value} was given");
        }
    }
}