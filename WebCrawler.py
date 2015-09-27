# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:35:38 2015

@author: Abdul.Jaber
"""

#from urllib import urlopen
from bs4 import BeautifulSoup
import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
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
        print visitedLinks
        print "---------"
        for links in newLinks:
            traverseInternet(links)
            
def getFeatures(url):
    source_code = requests.get(url)
    markup = source_code.text
    soup = BeautifulSoup(markup, "lxml")
    print soup
    #author = soup.findAll("a", { "rel" : "author" })[0].string
    #print author
    #fb = soup.findAll("li",{"class":"facebook"})
    slidernumber = soup.findAll("h5", {"class":"total-shares-count"})
    print slidernumber[1]
    
    
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
    
def urlliby(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    fbshares = tree.xpath('//*[@id="social-share"]/li[1]/h5')
    print 'Buyers: ', fbshares
    
def sele():
    b = connect('htmlunit')                                                                                                                                      
    b.get('http://google.com')                                                                                                                                   
    q = b.find_element_by_name('q')                                                                                                                              
    q.send_keys('selenium')                                                                                                                                      
    q.submit()  
    
def main():
    traverseInternet('http://www.aljazeera.com/news/default.html')
    #mtl_blog2("http://www.wired.com/") 
    #getFeatures("http://techcrunch.com/2015/09/26/augmented-reality-has-an-image-problem/")
    #urlliby('http://techcrunch.com/2015/09/26/augmented-reality-has-an-image-problem/')
    #sele()
main()