#!/usr/bin/env python
import re
import mechanize
from BeautifulSoup import BeautifulSoup
from array import array
import random
import ctypes
import os
import md5
import pprint
import sys
import subprocess
from time import strftime
from urllib import URLopener
from urllib2 import urlopen
from xml.dom.minidom import parseString

# setup
br = mechanize.Browser()
links = []
random.seed()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Defines source and destination of image
dst_dir = os.path.expanduser('~/Pictures/DeskFeed/')

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
tell application "System Events"
set theDesktops to a reference to every desktop
set picture of item 2 of the Desktops to POSIX file "%s"
end tell
set desktop picture to POSIX file "%s"
end tell
END"""

def set_desktop_background(destination1, destination2):
  subprocess.Popen(SCRIPT%(destination1,destination2), shell=True)

# grab the index page
br.open("http://wallbase.cc/search/nature")

# get a list of links
for link in br.links(url_regex="wallbase.cc/wallpaper/"):
  links.append(link.url)

# grab a random link, also convert list item to string
rndurl = str(random.sample(links, 1)).strip('[]\'')
response = br.open(rndurl)
soup = BeautifulSoup(response.read())
imgurl = soup.find("div", { "id" : "bigwall" }).findNext('img')['src']

# save wallpaper
destination1 = "%s%s.jpg" % (dst_dir, rndurl.split("/")[-1])

if not os.path.exists(destination1):
  URLopener().retrieve(imgurl, destination1)

# grab a random link, also convert list item to string
rndurl = str(random.sample(links, 1)).strip('[]\'')
response = br.open(rndurl)
soup = BeautifulSoup(response.read())
imgurl = soup.find("div", { "id" : "bigwall" }).findNext('img')['src']

# save wallpaper
destination2 = "%s%s.jpg" % (dst_dir, rndurl.split("/")[-1])

if not os.path.exists(destination2):
  URLopener().retrieve(imgurl, destination2)

set_desktop_background(destination1, destination2)