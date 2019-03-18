import sys
import urllib
from bs4 import BeautifulSoup, SoupStrainer
import requests

kw_file = sys.argv[1]
url = "http://google.com/complete/search?output=toolbar&q="

try:
    with open(kw_file, 'r') as fp:
        keywords = fp.read().splitlines()
        
except IOError:
    print(f"File not found in the desired location: {kw_file}") 

try:
    with open('auto_suggest_result.txt', 'w') as fp:                

        for kw in keywords:
            query = urllib.parse.quote(kw)

            res = requests.get(url + query)
            content = res.text

            print (kw)
            
            strainer = SoupStrainer("suggestion")
            soup = BeautifulSoup( content, parse_only = strainer, features='html.parser')
            
            fp.write(kw + ":\n")
            for s in [s['data'] for s in soup]:
                fp.write("\t" + s + "\n" )
            fp.write("\n\n")

except IOError:
    print("Could not write to file")
