# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:35:38 2015

@author: Abdul.Jaber
"""

#from urllib import urlopen
from bs4 import BeautifulSoup
import requests

#page = 1

visitedLinks = []

def mtl_blog(max_pages):
    page = 1
    while page<=max_pages:
        url = 'http://www.aljazeera.com/news/default.html'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a'):           
            href = link.get('href')
            print href           
            page += 1  
            
def mtl_blog2(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    count = 0
    for link in soup.findAll('a', href=True):
        # skip useless links
        if not link['href'] == '' and not link['href'].startswith('#'):
            print link['href']
            count+=1
    print count
 
def traverseInternet(url):    
    global visitedLinks
    newLinks = getLinks(url)
    if (url in visitedLinks):
        return
    elif (url not in visitedLinks):
        visitedLinks.append(url)
        getFeatures(url)
        print visitedLinks
        print "---------"
        for links in newLinks:
            traverseInternet(links)
            
def getFeatures(url):
    source_code = requests.get(url)
    markup = source_code.text
    soup = BeautifulSoup(markup, "lxml")
    print soup
    author = soup.findAll("a", { "rel" : "author" })[0].string
    print author
    section = soup.findAll("span", {"role":"presentation"},{"itemprop":"articleSection"})[0].string
    section = section.strip()
    print section
    
    
def getLinks(url):
    baseURL = 'http://www.aljazeera.com'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    count = 0
    links = []
    for link in soup.findAll('a', href=True):
        # skip useless links
        if link['href'].endswith('html') and link['href'].startswith('/news/'):
            formattedURL = baseURL + link['href']          
            links.append(formattedURL)
    return links
    
def main():
    #traverseInternet('http://www.aljazeera.com/news/default.html')
    #mtl_blog2("http://www.wired.com/") 
    getFeatures("http://www.wired.com/2015/09/new-iphone-cases-for-iphone6s/")
    
main()