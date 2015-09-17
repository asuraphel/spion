from bs4 import BeautifulSoup
from noti_db import Noti_db

import re
import urllib2
from urlparse import urljoin

class Crawler:
    '''Constructs List of pairs of Url and Pattern 
        from the expressions on WATCH_TAB 
    '''
    def __init__(self):
        self.db = Noti_db('watch.db')
        self.crawled = []
        url_pat_cur = self.db.get_url_pattern()
        url_pattern_pair = url_pat_cur.fetchone()
        while url_pattern_pair:
            if url_pattern_pair[0][-1] != '*':
                self.crawled.append(url_pattern_pair)
            else:
                base_url = url_pattern_pair[0][:-1] #strip the asterisk
                url_pattern = re.compile( base_url + '.*', re.I ) #convert to standard regex
                self.crawled.append(( base_url, url_pattern_pair[1])) #the base url should be added too
                self.crawled.extend( map( lambda x: (x ,url_pattern_pair[1] ),crawl_url( base_url, url_pattern)))
            url_pattern_pair = url_pat_cur.fetchone()
        
        #remove duplicates here -----
        temp = self.crawled
        self.crawled = []
        for x in temp:
            if x not in self.crawled:
                self.crawled.append(x)
        #-----------------------------

    def get_crawled(self):
        return self.crawled

def get_all_links( url, pattern ): #never return pages that do not match the pattern
    try:
        url_data = urllib2.urlopen(url).read()
    except Exception: 
        return []            
    url_soup = BeautifulSoup(url_data)
    url_links = url_soup.find_all('a')
    result = []
    for link in url_links:
        if pattern.match(urljoin( url, link.get('href')), re.I):
            result.append(urljoin( url, link.get('href')))
    return result

def crawl_url(start, pattern):
    tocrawl = [start]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            crawled.append( page )
            union( tocrawl , get_all_links( page, pattern ) )
    return crawled

#utility methods for crawler    
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

