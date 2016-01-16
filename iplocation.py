#!/usr/bin/python
######################
# 1 urlopen get html
# 2 transcoding to chinese
# 3 regex
######################
import urllib2
import requests
import re
import sys


def ip(ip):
    ipaddr = ip
    url = "http://ip138.com/ips138.asp?ip=" + ipaddr + "&action=2"
    response = urllib2.urlopen(url)
    text = response.read()
    tran_text = text.decode('gbk').encode('utf-8')
    com = re.compile('<li>.*</li>')
    tran_text_regex = re.findall(com, tran_text)
    print(tran_text_regex[0])


def num(num):
    ire = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    com = re.compile(ire)
    num_regex = re.findall(com, num)
    return num_regex
for i in sys.argv:
    if num(i):
        # print '\033[1;33m'
        sys.stdout.write('\033[1;33m')
        print(i)
        # print '\033[0m'
        # print '\033[1;31m'
        sys.stdout.write('\033[0m')
        sys.stdout.write('\033[1;31m')
        ip(i)
        # print '\033[0m'
        sys.stdout.write('\033[0m')
