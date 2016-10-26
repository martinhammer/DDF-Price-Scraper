import urllib2
from bs4 import BeautifulSoup

url = "http://online.dubaidutyfree.com/ddf/category/liquor-whisky-single-malt-whisky/_/N-7x7"
page = urllib2.urlopen( url )
soup = BeautifulSoup( page )

products = soup.find_all( "div", attrs = { 'class':'prod-title' } )

for product in products:
	print( product.div.string )
