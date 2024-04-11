import os 
import argparse 
from urllib.parse import urlparse
from pprint import pprint as pp 
import sys 
# googlesearch is available in PYPI's google package. Allows to script search queries through python.
try:
    from googlesearch import search as srch
except ImportError:
    print('Could not import module google.')

# Library of basic dorks. Keys contain areas while values contain a LIST of dorks.
library = {
    "domains": ['site:*.DOM -www.DOM'],         # This dork covers all subdomains. 
    "files": ['site:*.DOM filetype:pdf',
              'site:*.DOM filetype:xlsx',
              'site:*.DOM filetype:docx',
              'site:*.DOM filetype:txt',
              'site:*.DOM filetype:md',
              'site:*.DOM filetype:pptx'] 
}
ua = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'

# Setting up the script's options. 
parser = argparse.ArgumentParser(description='Script to automate Google Dorks for finding subdomains, filetypes and other items.') 
parser.add_argument('-d', '--domain', type=str, help='Enter the domain for which to list subdomains on Google.')
parser.add_argument('-f', '--files', type=str,  help='Finding different file types in a domain.')   
parser.add_argument('-q', '--query', type=str, help='Provide the dork you wish to search for.') 
parser.add_argument('-o', '--output', type=str, default='domain-list.txt', help='Output File Name to capture domain list.')
args = parser.parse_args()

def makeSearch(searchItem,netloc=True):
    search_results = [] 
    try:
        out_list = list(srch(searchItem, tld="co.in", num=10, stop=None, pause=25.0, user_agent=ua)) 
        if netloc:
            for url in out_list:
                search_results.append(urlparse(url).netloc) 
        else:
            for url in out_list:
                search_results.append(url) 
        search_results = list(set(search_results))  # Get Unique results. 
        return search_results
    except Exception as e:
        print(f'The query {searchItem} did not yield any results. {e}') 

def getQuery(*qry, **libqry):
    # If user specifes a DORK, search it. 
    queryList = []
    if qry:
        for q in qry:
            queryList.append(q) 
        return queryList
    
    # If user requests dork from our library, use that one. 
    libKey = []         # LIST to hold keys passed. 
    for x in libqry.values():   # Extract the value of the keyword passed.
        libKey.append(x) 
    
    dorkList = []       # Holder to create the final set of dorks to query. 
    for key in libKey:  
        for dork in library[key]:
            dorkList.append(dork) 
    
    for i,dork in enumerate(dorkList):
        dorkList[i] = dork.replace('DOM', args.domain)     # Replace all instances of DOM with passed domain.
    return dorkList
    # print(dorkList)
    # getQuery(libqry='domains') 

def writeToFile(search_result, fname='output.txt'):
    basedir = os.path.abspath(os.path.dirname(__file__)) 
    newFolder = 'Output'
    path = os.path.join(basedir,newFolder) 
    
    isExists = os.path.exists(path) 
    if not isExists:
        try:
            os.mkdir(path,0o700)   
        except Exception as e:
            print(f'Error creating the Output folder. {e}') 

    path = os.path.join(path,fname) 
    with open(path,"w") as f:
        for r in search_result:
            f.write(r+'\n') 

if args.query:
    print('[+] Searching for provided dork....')
    ql = getQuery(args.query)
    for q in ql:
        # print(q) 
        r = makeSearch(q) 
    print('[+] Search Complete. Writing to File.')
    print('[+] Printing results to STDOUT for reference.')
    for result in r:
        print(result) 
    writeToFile(r,args.output)

if args.domain:
    print('[+] Retrieving Dorks from Library....')
    ql = getQuery(libqry='domains')
    print('[+] Searching for provided dorks....')
    results = []
    for q in ql:
        r = makeSearch(q) 
        try:
            for i in r:
                results.append(i) 
        except TypeError:
            pass 
        except Exception as e:
            print(f'Error occurred in fetching results. {e}') 
    print('[+] Search Complete. Writing to File.')
    print('[+] Printing results to STDOUT for reference.')
    for result in results:
        print(result) 
    writeToFile(results,args.output)

if args.files:
    args.domain = args.files    # Set the domain flag to be same as files.
    print('[+] Retrieving Dorks from Library....')
    ql = getQuery(libqry='files')
    print('[+] Searching for provided dorks....')
    results = []
    for q in ql:
        r = makeSearch(q,False)     # File search requires full URL in return.
        try:
            for i in r:
                results.append(i) 
            if len(r) > 0:
                print(f'[+] Found results for {q}')
        except TypeError:           # If no result, then r will NoneType and non-iterable. 
            pass 
        except Exception as e:
            print(f'Error occurred in fetching results. {e}') 

    print('[+] Search Complete. Writing to File.')
    print('[+] Printing results to STDOUT for reference.')
    for result in results:
        print(result) 
    writeToFile(results,args.output)
