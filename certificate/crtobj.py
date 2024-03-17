import json 

class Cert:
    # Pass the response to CRT.SH as a string
    def __init__(self, crtdata):
        self.data = crtdata 
    
    def extractDomains(self):
        domains = []
        # The below is a tricky line of code. It is a LIST COMPREHENSION. 
        # It appends to domains list a domain that is not already present. Note, we use JSON.LOADS to convert string into python structure. 
        [domains.append(x['name_value']) for x in json.loads(self.data) if x['name_value'] not in domains]
        return domains 
    