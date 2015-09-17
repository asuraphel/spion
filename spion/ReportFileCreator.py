class ReportFileCreator:
    html = '''<DOCTYPE html5>
        <head>
            <title>Notifications - Spion</title>
            <link rel="stylesheet" href="style.css" />
        </head>
        <body>
        %s
        </body>
    </html>'''
    
    para = '''<div class="notification">
        <h3><a href="%s">%s</a></h3>
        <div class="excerpt">%s</div>
    </div>'''
    
    
    def __init__(self, new_url_extracted_tuple_list):
        html = '''<html>
            <head>
                <title></title>
                <link rel="stylesheet" href="style.css" />
            </head>
            <body>
            %s
            </body>
        </html>'''
        
        para = '''<div class="notification">
            <h3>@ <a href="%s">%s</a></h3>
            <div class="excerpt">%s</div>
        </div>'''
        report_html = ''
        for tuple in new_url_extracted_tuple_list:
            report_html = report_html + (para % (tuple[0], tuple[0], tuple[1]))
        report = ''
        html = html % report_html
        self.f = open('C:\\Python26\\Lib\\site-packages\\Spion\\report.html', 'w') 
        self.f.write(html)
        self.f.close()
    
    
    