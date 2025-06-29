using System;
using System.Collections.Generic;

namespace MoshOops1
{
    internal class SecurityProgram
    {
        public string name;
        public int budget;
        public List<Scope> Scopes; 

        public SecurityProgram()
        {
            Scopes = new List<Scope>();     // Initialize the LIST. Responsibility of class. 
        }

        public SecurityProgram(string name) : this()        // this() keyword provides access to constructor with no arguments. 
        {
            this.name = name;
        }

        public SecurityProgram(string name, int budget) : this(name)    // this(name) gives access to constructor that uses name argument. 
        {
            this.budget = budget;   
        }

        // A static method on the class. 
        public static string Alignment()
        {
            // Return Alignment Framework.
            return "NIST"; 
        }
    }
}
