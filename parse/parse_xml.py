import urllib2

response = urllib2.urlopen('http://www.malwaredomainlist.com/hostslist/mdl.xml')
data = response.read()
print data
