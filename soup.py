# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:15:11 2018

@author: Pratik Prabhakar
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#URL of the website
myurl_qoocam= 'https://www.kickstarter.com/projects/473370515/qoocam-worlds-first-interchangeable-4k-360-and-3d/comments'
myurl_firststraw= 'https://www.kickstarter.com/projects/908228738/finalstraw-the-worlds-first-collapsible-reusable-s/comments'


uClient = uReq(myurl_firststraw)
page_html = uClient.read()
uClient.close()
#Find the id from the page and inspect
page_soup = soup(page_html, "html.parser")
    
container= page_soup.findAll("ol", {"class":"comments"})
for c in container:
    div_container = c.findAll("div", {"class":"main clearfix pl3 ml3"})
    for d in div_container:
        print(d.p.text)