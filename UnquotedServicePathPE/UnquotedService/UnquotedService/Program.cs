using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.ServiceProcess;
using Microsoft.Win32; 

namespace UnquotedService
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // ServiceController gets us the services available on the system. Inside System.ServiceProcess namespace. 
            ServiceController[] sc;
            sc = ServiceController.GetServices();   // Retrieves all services. 

            // Looping through each service retrieved. 
            foreach (ServiceController s in sc)
            {
                // To extract the path of the BINARY that is being run as the service, you need to use Registry. HKLM hive contains this info.
                // Inside HKLM, you need to look into => System/CurrentControlSet/Services/<service name> 
                RegistryKey rkey = Registry.LocalMachine.OpenSubKey(@"SYSTEM\CurrentControlSet\Services\" + s.ServiceName);
                string path = rkey.GetValue("ImagePath").ToString();    // Gets us the path of the binary for each service.

                // Unquoted Service Path Escalation Checks. 
                // For privilege escalation to be possible 3 conditions should meet. 
                //      1. Service should not contain double quotes or it should be unquoted. 
                //      2. There should be a white space in the path. 
                //      3. The path should be writable. 
                // Below only tests that service name is UNQUOTED. Also, System32 folder is not returned to us as it is mostly non-writable. 
                if (path[0] != '"' && !path.Contains("system32") && !path.Contains("System32"))
                {
                    Console.WriteLine(s.ServiceName + " : " + s.CanShutdown + " : " + path);
                }



            }

        }
    }
}
