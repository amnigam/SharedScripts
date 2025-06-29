
using System.Collections;

namespace MoshOops1
{
    internal class Scope
    {
        public string name;
        public ArrayList tools;    

        // Initialize the ArraList as part of its null argument constructor.
        public Scope()
        {
            tools = new ArrayList();
        }

        // Method to load tools. 
        public void AddTools(params string[] tools)     // using params to add any number of tools.
        {
            foreach (string tool in tools)
            {
                this.tools.Add(tool);
            }
        }
    }
}
