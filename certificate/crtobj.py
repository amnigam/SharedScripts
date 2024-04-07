import json 
import os 

class Cert:
    # Pass the response to CRT.SH as a string
    def __init__(self, crtdata, outfile):
        self.data = crtdata 
        self.domains = []
        self.id = []
        self.outfile = outfile
    
    def extractDomains(self):
        # The below is a tricky line of code. It is a LIST COMPREHENSION. 
        # It appends to domains list a domain that is not already present. Note, we use JSON.LOADS to convert string into python structure. 
        [self.domains.append(x['name_value']) for x in json.loads(self.data) if x['name_value'] not in self.domains]
        self.writeToFile(self.outfile, self.domains) 
        
        [self.id.append(x['id']) for x in json.loads(self.data) if x['id'] not in self.id]
        self.writeToFile('crt-id.txt', self.id)     # Hard coded value for Cert ID File name. 

        return self.domains 
    
    def writeToFile(self,fname,listObj): 
        basedir = os.path.abspath(os.path.dirname(__file__)) 
        newFolder = 'CRT-Output'
        path = os.path.join(basedir,newFolder) 
        
        isExists = os.path.exists(path) 
        if not isExists:
            try:
                os.mkdir(path,0o700)   
            except Exception as e:
                print(f'Error creating the CRT output folder. {e}') 

        path = os.path.join(path,fname)     # Get final path to output file. 

        with open(path,"w") as f:
            for item in listObj:
                if type(item) != 'str':
                    f.write(str(item))
                    f.write('\n')
                else: 
                    f.write(item.strip())
                    f.write('\n')

    def getcrtid(self): 
        return self.id 