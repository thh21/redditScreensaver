# [Thom H (https://github.com/thh21)] Reddit Screensaver
#          https://github.com/thh21/redditScreensaver
#		   Downloads different pictures from the front page of different subreddits
# 		   each day. Subreddits set in json file in same dirrectory
# 		   
# ------------------------------------------------------------------

import urllib2, urllib
import json
import os
import datetime
import sys
import getopt

saveDir = os.environ['HOME'] + '/.redditScreensaver/images'

def internetOn():
    try:
        response=urllib2.urlopen('http://reddit.com',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def clean():
    if os.path.isdir(saveDir):
        for file in os.listdir(saveDir):
            if file.endswith('.jpg'):
                os.remove(saveDir + '/' + file)
    else:
        os.mkdir(saveDir)
        
def getSubreddit():
    day = datetime.datetime.today().weekday()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    conffile = open('subreddits.json', 'r')
    confjson = json.loads(conffile.read())
    conffile.close()
    
    todaysJson = confjson[days[day]]
    subreddit = todaysJson['type'] + '/'
    
    for page in todaysJson['pages']:
        subreddit += page
        subreddit += '+'
        
    return subreddit

def populate(subreddit):
    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'osx:com.gremy0..redditScreensaver:v0.1 (by u/gremy0)')]
    response = opener.open('https://www.reddit.com/'+ subreddit + '.json')
    rawjson = response.read()
    parsedjson = json.loads(rawjson)

    for post in parsedjson["data"]["children"]:
        url = post["data"]["url"]
        if not url.endswith(".jpg") and post['data']['domain'].endswith('imgur.com'):
            url = url + '.jpg'
            
        if url.endswith(".jpg") and not post['data']['over_18']:
            filename = url[url.rindex('/') + 1::]
            # file = open(filename, 'w')
            image = urllib.urlretrieve(url, saveDir + '/' + filename)


def main(argv):
    opts, args = getopt.getopt(argv, 'o:')
    for opt, arg in opts:
        if opt == '-o':
            saveDir = arg
            
    if internetOn():
        clean()
        subreddit = getSubreddit()
        populate(subreddit)

if __name__ == "__main__":
    main(sys.argv[1::])