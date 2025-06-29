using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MoshOops1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var a = new SecurityProgram();      // Using a null constructor
            a.name = "Vulnerability Management";
            a.budget = 100000;
            Console.WriteLine($"This is the object's name: {a.name}");
            Console.WriteLine($"This is the object's budget: {a.budget}");
            Console.WriteLine($"The program is aligned with: {SecurityProgram.Alignment()}");
            var s1 = new Scope();
            s1.name = "Vulnerability Management";
            s1.AddTools("Nessus", "Qualys", "Greenbone", "Azure Native Tools");

            var s2 = new Scope();
            s2.name = "Threat Hunting";
            s2.AddTools("Zeek", "Rita", "Splunk"); 

            a.Scopes.Add(s1);
            a.Scopes.Add(s2);   
            // Print out the scope object.
            for (int i=0; i<a.Scopes.Count; i++)
            {
                Console.WriteLine(a.Scopes[i].name);
                for (int j=0; j<a.Scopes[i].tools.Count; j++)
                {
                    Console.WriteLine(a.Scopes[i].tools[j]);
                }
                Console.WriteLine(String.Concat(Enumerable.Repeat("-", 50)));       // This is what you have to do, to draw freaking line.
            }

            // Property Testing
            var tom = new Employee(new DateTime(1980, 4, 30));  // Using Base Constructor
            tom.Name = "Tom";
            tom.Team = "Vulnerability Management";
            Console.WriteLine($"The name of employee is {tom.Name} and the team is {tom.Team} and age = {tom.Age}");

            var alice = new Employee("Alice", new DateTime(1990, 12, 31));   // Using second constructor
            alice.Team = "Reporting";
            Console.WriteLine($"The name of employee is {alice.Name} and the team is {alice.Team} and age = {alice.Age}");

        }
    }
}
