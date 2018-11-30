import praw, urllib.request, ctypes, getpass, sys, os

#Gets top hot post url from /r/earthporn as a string
def getUrl(postNum):
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit("earthporn") #Change this to set different subreddit
    for submission in subreddit.hot(limit=postNum): 
        link = reddit.submission(submission)
    linkstring = str(link.url)
    return linkstring

#If the url isn't in image format, sets it
def setImageUrl(url):   
    if not(url.endswith('.jpg')) and not(url.endswith('.jpeg')) and not(url.endswith('.png')):
        url = url + '.jpg'
    return url

#Checks to make sure the link url is an actual picture and if not gets next post
def checkUrl(url):
    checkCount = 2
    while 'imgur' not in url and 'i.redd.it' not in url:
        url = getUrl(checkCount)  
        checkCount += 1
    return url

#Gets and formats the Url from /r/earthporn
print("Acquiring Url from Reddit.")
linkstring = getUrl(1)
linkstring = checkUrl(linkstring)
linkstring = setImageUrl(linkstring)

#Saves file to computer in same directory as this .py file
print("Saving file to computer.")
urllib.request.urlretrieve(linkstring, 'earthImage.jpg')

#Sets desktop as the saved file
print("Setting desktop as file.")
User = str(getpass.getuser())
SPI_SETDESKWALLPAPER = 20 
print(str(os.path.join(os.path.dirname(os.path.realpath(__file__)), "earthImage")))
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), "earthImage.jpg")) , 0)

