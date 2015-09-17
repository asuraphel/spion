<h3>SPION</h3>

Spies on webpages or websites(specified in greasemonkey like wildcards) based on user submitted pattern and sends notifications when changes are made according to the pattern submitted.

Cases:

1 A new content is added containing the pattern.
2 Web page no longer contains occurences of the pattern.

<h4>USAGE SCENARIOS</h4>


1 You find a website whose members meet up in different countries and the website tells you to constantly check their website in case they are coming to your country. It is obviously difficult to check a website regulary so you need a software that you can submit to the URL and the keywords/regex(e.g. name of your country) and this application notifies you when that appears.

2 You are a celebrity and you want to quickly find out when your name is published on popular media sites. So you submit your name the site and relax. You don't just submit the page but the base url of the site and wild card( e.g. http://thesun.co.uk/*, 'Lady Gaga' ). You'll immediately receive notification when that name is detected on pages reachable from http://thesun.co.uk.

3 You visit Udacity's website and to check whether grades are out and you find a message that says udacity robots are grading your code and you should check your results later. So instead of checking the site manually you enter the URL of the progress tab and "udacity robots" in the textbox with the label "Enter words or regex patter to watch disappear" and submit. Spion notifies you when the words/regex you submitted is no longer on the webpage. (The * wildcard is not supported for this case because it doesn't make sense)

The same idea can be used to know when a website is no longer "under construction" in which case it does not always suffice to know the site has made changes. That is because modern designs for "under construction" designs may also include server side generated dynamic content such as date.

<h4>Features</h4>

- You will not be notified twice for a keyword that is not newly added. Once you receive a notification for a keyword, you'll only recieve another one when the same keyword is added in a different place on that page.

-Spion will not only watch a single web page but also a website or part of it specified by a wild card as in the above example submitting http://thesun.co.uk/* will make the Spion to inspect sites beginning with http://thesun.com/ such as http://thesun.co.uk/news/index.html too.

-Spion will not save the entire web page to track changes on it. It will only save a few bytes of data related to occurences of patterns you are already notified about.

<h4>Installation</h4>

1) Extract the package
2) On CMD go to the directory where setup.py resides
3) python setup.py install

Note: Currently only Windows is supported and you must install the package to use it correctly.
