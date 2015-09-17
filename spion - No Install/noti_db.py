import sqlite3 as lite
class Noti_db:
    def __init__(self, db_name):
        self.con = lite.connect( db_name)
        with self.con:            
            self.cur = self.con.cursor()    
            self.cur.execute('CREATE TABLE IF NOT EXISTS WATCH_TAB(Id INTEGER PRIMARY KEY, Url TEXT, Pattern TEXT )')
            self.cur.execute('CREATE TABLE IF NOT EXISTS URLINFO_TAB(Id INTEGER PRIMARY KEY, Url TEXT, Length TEXT, Hash TEXT)')
            self.cur.execute('CREATE TABLE IF NOT EXISTS NOTI_TAB(Id INTEGER PRIMARY KEY, Url TEXT, Extract TEXT)') #extract contains the pattern plus neighbouring text
            self.cur.execute('CREATE TABLE IF NOT EXISTS DISAPP_TAB(Id INTEGER PRIMARY KEY, Url TEXT, Pattern TEXT)') #contains urls to be watched for disappearance of Pattern
            
    def get_url_pattern( self ): #return cur and caller will fetch data[to avoid multiple calls to exec]
        self.cur.execute( 'SELECT Url, Pattern FROM WATCH_TAB')
        return self.cur
        
    def add_url_pattern(self, url, pattern):
        self.cur.execute('INSERT INTO WATCH_TAB (Url , Pattern) VALUES ( \'%s\', \'%s\' )' % ( url, pattern))
        self.con.commit()
    
    def add_url_disapp( self, url, pattern):
        self.cur.execute('INSERT INTO DISAPP_TAB (Url , Pattern) VALUES ( \'%s\', \'%s\' )' % ( url, pattern))
        self.con.commit()
        
    def get_url_disapp( self ): #return cur and caller will fetch data[to avoid multiple calls to exec]
        self.cur.execute( 'SELECT Url, Pattern FROM DISAPP_TAB')
        return self.cur
        
    def remove_url_disapp( self, url, pattern ): #return cur and caller will fetch data[to avoid multiple calls to exec]
        self.cur.execute( 'DELETE FROM DISAPP_TAB WHERE URL = \'%s\' AND PATTERN = \'%s\'' % (url, pattern))
        self.con.commit()
    
    
    def url_info( self, url ):
        self.cur.execute('SELECT Length, Hash FROM URLINFO_TAB WHERE Url = \'%s\'' % url)
        return self.cur.fetchone()
        
    def save_new_extract(self , url , extract):    
        query = 'INSERT INTO NOTI_TAB( Url, Extract) VALUES( \'%s\', \'%s\' )' % (url, extract)
        self.cur.execute( query ) 
        self.con.commit()
                
    def clear_extracts( self, url): #CONSIDER REMOVING AS NO REASON TO DELETED DETECTED EXTRACTS
        self.cur.execute( 'DELETE FROM NOTI_TAB WHERE Url = \'%s\'' % url )
        self.con.commit()
    
    def remove_from_watch( self, url, pattern):
        self.cur.execute('DELETE FROM WATCH_TAB WHERE Url = \'%s\' AND Pattern = \'%s\'' % (url, pattern) )
        self.con.commit()
        
    def update_urlinfo( self, url, length, hash):
        self.cur.execute('UPDATE URLINFO_TAB SET Url = \'%s\', Length = \'%s\', Hash = \'%s\'' % (url, length, hash))
        self.con.commit()
    
    def url_extracted_exists( self, url, extracted):
        self.cur.execute('SELECT * FROM NOTI_TAB WHERE Url = \'%s\' AND Extract = \'%s\'' % (url, extracted))
        return bool(self.cur.fetchone())
        