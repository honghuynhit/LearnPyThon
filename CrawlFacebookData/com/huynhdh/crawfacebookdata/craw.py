'''
Created on Dec 13, 2018

@author: huynhdh
'''
import urllib.request

def getIdFacebook(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()  
    html = str(html);
    indexOfString = html.find("entity_id")
    string1 = html[indexOfString:indexOfString+25].replace("entity_id=","");
    print(string1);