# For python 2.7
# This is program to extract a tutorial from the website tutorialpoint.com
# First a HTML is created and then a corresponding pdf. Both the files are available.
# Changing the mainURL can lead to extraction of any tutorial.
# Single Beep confirms Generation of HTML file and Double Beep confirms Generation of PDF

import winsound
import pdfcrowd
import urllib
import os
from bs4 import BeautifulSoup

# username and api-key. Insert your own. It is free for a limited amout go to the website.
USERNAME = 'randomperson'
API_KEY = '31f30faae08a14a3d27563b31b7cbcf5'


# mainURL
mainURL = urllib.urlopen('http://www.tutorialspoint.com/automata_theory/')
tempOut = mainURL.read()
tempAccessHTML = open('tempAccessHTML.html', 'w')
tempAccessHTML.write( tempOut)
tempAccessHTML.close()

# making soup of the tempAccessHTML
tempAccessHTML = open('tempAccessHTML.html', 'r')
mainSoup = BeautifulSoup(tempAccessHTML, 'html.parser')
tempAccessHTML.close()

nameOfSubject = mainSoup.title.string
print '<><><> ' +  nameOfSubject + ' <><><>'


# getting all the required links
linkList = []
linksPortion = mainSoup.find('aside')
mainSoup.find( attrs={'class': ['special']}).extract()
for link in linksPortion.find_all('a'):
        linkList.append(link['href'])

# 2nd last page is not important so removing it - this depends on your personal choice
linkList.pop(-2)

# The Ouptut file is the required file
htmlResult = open( nameOfSubject + '.html', 'w')
# This writes the <head> part of the html. Bootstrap and padding is adding for better html design.
htmlResult.write('<!DOCTYPE html>\n<html>\n\t<head>\n \
\t\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" \
integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous"> \
\n\t\t<title>' + nameOfSubject + '</title>\n\t\t<style>\n\t\t\thtml { padding: 0 10%;}\n\t\t</style>\n\t</head>\n<body>\n')

# The FIRST page had problems with the html so beautiful couldn't do well. Again first page isn't the requirement.
# Accessing each page. except FIRST Page
for link in linkList[1:]:
        currLink = 'http://www.tutorialspoint.com' + str(link)
        print '-> -> Opening: ' + currLink
        url = urllib.urlopen( 'http://www.tutorialspoint.com' + str(link))

        tempPage = url.read()
        tempAccessHTML = open('tempAccessHTML.html', 'w')
        tempAccessHTML.write( tempPage)
        tempAccessHTML.close()
        tempAccessHTML = open('tempAccessHTML.html', 'r')
        soup = BeautifulSoup(tempAccessHTML, 'html.parser')
        tempAccessHTML.close()

        # removing all the forms in the html
        for form in soup.find_all('form'):
                form.extract()

        # removing script tags
        for tag in soup.find_all('script'):
                tag.extract()

        # removing advertising and buttons
        for tag in soup.find_all(attrs={'class': ['bottomgooglead', 'bottomadtag', 'topgooglead', 'pre-btn', 'nxt-btn', 'print-btn', 'pdf-btn']}):
                tag.extract()

        # removing the 1st and last horizontal line <hr> tag
        soup.find_all('hr')[0].extract()
        soup.find_all('hr')[-1].extract()

        # making the image sources from realtive style to absolute style
        for img in soup.find_all('img'):
            img['src'] = 'http://www.tutorialspoint.com' + img['src']

        # changing the main div class 'col-md-7 middle-col' to an arbitary otherwise bootstrap can give problem
        soup.find(class_='col-md-7 middle-col')['class'] = 'theportion'
        selectedPortion = soup.find('div', attrs={'class': 'theportion'})
        
        print '>> >> Writing: ' + currLink
        # Writing the acquired part
        htmlResult.write(str(selectedPortion.prettify().encode('utf-8')))

# Closing the html and the file
htmlResult.write('</body></html>')
htmlResult.close()
print '<><><> HTML created <><><>'
winsound.Beep(2500, 100)

# Removing the temporary file
os.remove('tempAccessHTML.html')

# This part converts the OUTPUT html into a PDF using pdfcrowd.com's API
# you need a free pdfcrowd.com account. Use the given username and apikey

print '<><><> Going for conversion of HTML to PDF <><><>'
try:
    # create an API client instance
    client = pdfcrowd.Client(USERNAME,API_KEY)

    # convert an HTML file
    output_file = open(nameOfSubject + '.pdf', 'wb')
    client.convertFile(str(nameOfSubject + '.html'), output_file)
    output_file.close()
    print '<><><> Conversion Completed <><><>'

except pdfcrowd.Error, why:
    print('Failed: {}'.format(why))

# Beep soung to indicate the completion
winsound.Beep(2500, 100)
winsound.Beep(2500, 100)
