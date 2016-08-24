#!/usr/bin/python

import urllib2
import cookielib
import sys

# Your Registered phone Number(Username) without any international
# code and Password
USERNAME = "XXXXXXXXXX"
PASSWORD = "PASSWORD"


def sendSMS(message, number):
    message = "+".join(message.split(' '))

    # Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username=' + USERNAME + '&password=' + PASSWORD + '&Submit=Sign+in'

    # For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/37.0.2062.120 Safari/537.36')]

    try:
        usock = opener.open(url, data)
    except IOError:
        print "Error while logging in."
        sys.exit(1)

    # Parsing of token
    jession_id = str(cj).split('~')[1].split(' ')[0]

    # Creating the url required to send the message
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token=' + jession_id + '&mobile=' + number \
        + '&message=' + message + '&msgLen=136'
    opener.addheaders = [
        ('Referer', 'http://site25.way2sms.com/sendSMS?Token=' + jession_id)]

    # Sending the message
    try:
        sms_sent_page = opener.open(send_sms_url, send_sms_data)
    except IOError:
        print "Error while sending message"
        sys.exit(1)

    print "SMS has been sent."


if __name__ == '__main__':
    receiversNumber = "YYYYYYYYYY"
    sendSMS("The Message to be Send", receiversNumber)
