import urllib2
from bs4 import BeautifulSoup
import os
import sys
import re
from Tkinter import Tk, BOTH

#my modules
from noti_db import Noti_db
from ReportFileCreator import ReportFileCreator
from noti_window import Notif_win
from crawler import Crawler 

def extract(text, compiled_pattern): #returns list of extracted text based on neighbouring text algo
    OFFSET = 10
    text_length = len(text)
    pat_iter = compiled_pattern.finditer(text)
    result = []
    for occurence in pat_iter:
        if occurence.start() - OFFSET < 0:
            start = 0
        else: 
            start = occurence.start() - OFFSET       
        end = occurence.end() + OFFSET    
     
        extracted_text = text[start:end]
        result.append(extracted_text)    
    return result
        
def main():
    #-----------------------------------------------------------------------------------------------
    #let's process the watch list
    #-----------------------------------------------------------------------------------------------
    
    u_p_l = Crawler() #allows to submit greasemonkey type wildcard urls e.g. http://www.google.com/*
    url_pattern_list = u_p_l.get_crawled() #Fetch the list of all the Urls that we want to watch

    database = Noti_db('watch.db')
     
    new_url_extracted_tuple_list = []    
    for url_pattern_tuple in url_pattern_list:
        try:
            url_data = urllib2.urlopen(url_pattern_tuple[0]).read()
        except Exception: 
            continue
            
        url_soup = BeautifulSoup(url_data)
        url_text = url_soup.get_text()
        url_length = len(url_text)
        url_hash = hash(url_text)
        
        #see if anything has changed on the url
        if( database.url_info(url_pattern_tuple[0]) == (url_length, url_hash)): #hasn't changed since last
            continue
        else:
            database.update_urlinfo(url_pattern_tuple[0], url_length, url_hash)
        
        pattern = re.compile( url_pattern_tuple[1], re.I ) #add flags as found appropriate
        
        extracted = extract(url_text, pattern) #array of extracted    
        if not extracted: continue    
        
        for x in extracted:
            if database.url_extracted_exists(url_pattern_tuple[0], x):
                continue
            else: 
                database.save_new_extract(url_pattern_tuple[0], x)
                #append to list to generate the report later    
                new_url_extracted_tuple_list.append((url_pattern_tuple[0], x)) 
    
    #-------------------------------------------------------------------------------
    #now we handle the disappearance and change notification 
    #-------------------------------------------------------------------------------
    
    url_disapp_list = []
    url_disapp_cursor = database.get_url_disapp()
    url_disapp_tuple = url_disapp_cursor.fetchone()
    while url_disapp_tuple:
        disapp_pat = re.compile( url_disapp_tuple[1], re.I)
        try:
            url_data = urllib2.urlopen(url_pattern_tuple[0]).read()
        except Exception: 
            continue
            
        url_soup = BeautifulSoup(url_data)
        url_text = url_soup.get_text()
        
        if extract( url_text, disapp_pat):
            continue
        else: #the pattern has disappeared
           new_url_extracted_tuple_list.append((url_disapp_tuple[0], 'The pattern "%s" does not exist anymore.' % url_disapp_tuple[1])) 
           database.remove_url_disapp( url_disapp_tuple[0], url_disapp_tuple[1])
           
        url_disapp_tuple = url_disapp_cursor.fetchone()
        
    
    #-------------------------------------------------------------------------------
    #Display notification if there exists any
    #-------------------------------------------------------------------------------
    if new_url_extracted_tuple_list:
        report_file = ReportFileCreator(new_url_extracted_tuple_list)
        #----------------------------------------------------------------------------
        #window stuff here
        #----------------------------------------------------------------------------
        root = Tk()
        root.geometry("450x80+300+300")
        app = Notif_win(root) #Has a button for viewing reports
        root.mainloop()
    database.con.close()
    sys.exit()
    
if __name__ == '__main__':
        main() 
    
    
