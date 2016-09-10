#testing git
# coding: utf-8
from markoffchain import MarkovChain
import urllib2
from bs4 import BeautifulSoup

blog = 'http://www.espnfc.us/portugal/story/2910804/portugal-striker-cristiano-ronaldo-forced-off-injured-in-euro-2016-final'
new_blog = urllib2.urlopen(blog)
soup = BeautifulSoup(new_blog)
new_soup = (soup.prettify())
print "=" * 40
print (new_soup)

new_mc = MarkovChain(2)
print "=" * 40
new_mc.add_string(new_soup)
print (new_mc.generate_text())
print "=" * 40
print (new_mc.generate_text())
print "$" * 50
print "probando"




# testin the program
print "*" * 40
