import json 

class Cert:
    # Pass the response to CRT.SH as a string
    def __init__(self, crtdata):
        self.data = crtdata 
        self.domains = []
        self.id = []
    
    def extractDomains(self):
        # The below is a tricky line of code. It is a LIST COMPREHENSION. 
        # It appends to domains list a domain that is not already present. Note, we use JSON.LOADS to convert string into python structure. 
        [self.domains.append(x['name_value']) for x in json.loads(self.data) if x['name_value'] not in self.domains]
        self.writeToFile("domain-list.txt", self.domains) 
        
        [self.id.append(x['id']) for x in json.loads(self.data) if x['id'] not in self.id]
        self.writeToFile('crt-id.txt', self.id) 

        return self.domains 
    
    def writeToFile(self,fname,listObj): 
        with open(fname,"w") as f:
            for item in listObj:
                if type(item) != 'str':
                    f.write(str(item))
                    f.write('\n')
                else: 
                    f.write(item.strip())
                    f.write('\n')

    def getcrtid(self): 
        return self.id 