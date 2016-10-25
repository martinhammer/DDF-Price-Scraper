import urllib2
from bs4 import BeautifulSoup

url = "http://online.dubaidutyfree.com/ddf/category/liquor-whisky-single-malt-whisky/_/N-7x7"
page = urllib2.urlopen( url )
soup = BeautifulSoup( page )

print soup
