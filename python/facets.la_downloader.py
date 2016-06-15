#-------------------------------------------------------------------------------
# Name:     facetsDownloader
# Purpose:  To download all possible wallpapers from website facets.la
#-------------------------------------------------------------------------------

import urllib2
import os
import atexit
import string
import winsound
from bs4 import BeautifulSoup

# For handling the incomplete file created due to an interuption( CTRL + C, program close)
##def killingLastIncompleteFile(fileToBeDeleted):
##    print "here"
##    os.mkdir('jaimatadi')
##    os.remove(fileToBeDeleted)
##filePath = ''
##atexit.register(killingLastIncompleteFile, filePath)

# Main Url and its Soup
mainUrl = urllib2.urlopen('http://www.facets.la/wallpapers/')
mainSoup = BeautifulSoup(mainUrl, 'html5lib')

# Getting all the possible links
allPartialLinks = mainSoup.find_all(attrs={'class': 'thumb'})
allImageShowcaseLinks = []

# Filtering out the image showcase link
for thumb in allPartialLinks:
    temp = thumb.next_element.next_element.next_element.get('href')
    allImageShowcaseLinks.append(temp)

# Making a folder for saving image files
directory = os.path.dirname(os.path.abspath(__file__))
facetsdir = directory + '\\Facets - Wallpapers'
if not os.path.exists(facetsdir):
    os.makedirs(facetsdir)

print 'There are ' + str(len(allImageShowcaseLinks)) + ' images available for downloading.'
i = 1
exclude = list(string.punctuation)
for link in allImageShowcaseLinks:
    # Making soup of the link
    linkUrl = urllib2.urlopen(link)
    linkSoup = BeautifulSoup(linkUrl, 'html.parser')

    # Making out File Number
    temp = linkSoup.find(attrs={'class': 'size13'})
    filename = temp.next_element.string + ' - '

    # Making out the Filname
    temp = linkSoup.find(attrs={'class': 'size15'})
    temp1 = temp.next_element.next_element.string
    # removing punctuation from filename since punctuations are not allowed in file names.
    temp = ''.join(ch for ch in temp1 if ch not in exclude)
    filename = filename + temp

    print str(i) + '. Downloading: ' + filename
    i += 1

    # Making out the ImageLink
    temp = linkSoup.find(id='facet-wallpaper')
    imgLink = temp.next_element.get('src')

    # Download of a image if it aint exist in the folder
    filePath = facetsdir + '\\' + filename + '.jpg'
    if not os.path.isfile(filePath):
        imgFile = urllib2.urlopen(imgLink)
        with open(filePath, 'wb') as image:
            image.write(imgFile.read())

print '<><><> Download Completed <><><>'
winsound.Beep(2500, 100)
winsound.Beep(2500, 100)







        
