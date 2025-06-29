using System;

namespace MoshOops1
{
    internal class Employee
    {
        // Normal display of Property. Public accessibility with a getter & setter. 
        public string Team { get; set; }
        public string Name { get; set; }

        // BirthDate has to be set only once when the constructor runs. And can't be modified after that. 
        public DateTime BirthDate { get; private set; }

        // Age can only be retrieved and not set.
        public int Age
        {
            get
            {
                var timeSpan = DateTime.Today - BirthDate;
                int years = timeSpan.Days / 365;
                return years;
            }
        }
        // Base Constructor
        public Employee(DateTime BirthDate)
        {
            this.BirthDate = BirthDate;
        }

        public Employee(string Name, DateTime BirthDate)  
        {
            this.Name = Name;
            this.BirthDate = BirthDate;
        }
        
    }
}
