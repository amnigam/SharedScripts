using System;
using System.Threading.Tasks;
using System.Threading.Tasks.Extensions; 
using System.Net.Http;
using System.Text.Json;



namespace ShodanConnect
{
    internal class Program
    {
        public static string file = @"C:\Users\Amit Nigam\OneDrive\Penetration Testing\SharedScripts\UnquotedServicePathPE\ShodanConnect\ShodanConnect\output.txt";
        // 40.132.188.215  System.Threading.Tasks.Extensions
        static async Task Main(string[] args)
        {
            Console.WriteLine("Enter IP address: ");
            string ip = Console.ReadLine();
            string url = "https://internetdb.shodan.io/"; 

            var client = new HttpClient();
            var result = await client.GetStringAsync(url+ip);
            Console.WriteLine(result.GetType().Name);       // Tells us that the output is in String format. 

            // To prettify the JSON String we use System.Text.Json 

            var options = new JsonSerializerOptions()
            {
                WriteIndented = true
            };

            var outResult = JsonSerializer.Serialize(result, options);
            Console.WriteLine(outResult); 

        }
    }
}
