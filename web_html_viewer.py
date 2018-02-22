import urllib2
file = urllib2.urlopen(raw_input('Enter url: '))
message = file.read()
print message