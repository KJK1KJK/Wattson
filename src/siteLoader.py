import requests
import json

"""
This file is responsible for loading the site list into the program, as well 
as checking wether the picked URLs are viable.
The results of checking will be stored in a JSON file viableURLs.json
From JSON it will be easy to convert the text file into spreadsheets/databases if needed.
"""

#Load all of URL's from the text file
def loadFile(path):
    with open(path, "r") as file:
        URLs = file.readlines()
    #Strip the URLs from serial number as well as the new line sign
    URLs = [url[3:].strip() for url in URLs if url[0]!="#"]
    #Instead of doing the whole class for only one property (avaliable), just make it a dictionary
    URLs = {url:False for url in URLs}
    return URLs

#Filter all of URLs that don't exist
def filterAvaliableSites(URLs):
    for url in URLs:
        #send the request to every singular URL
        try:
            req = requests.get(url)
        except:
            #If the requested site doesn't exist, just go to the next element.
            continue
        """
        Set the "avaliable" value to true if the URL is up,
        or if it's not redirected (sites often redirect to "user not found" page.)
        """
        if(req.status_code==200 and len(req.history)<=1):
            URLs[url] = True
    return {url for url in URLs if URLs[url]}




if (__name__=="__main__"):
    urls_to_be_checked = loadFile("testSites.txt")
    filtered_urls = filterAvaliableSites(urls_to_be_checked)
    print(filtered_urls)