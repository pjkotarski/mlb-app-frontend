from ohmysportsfeedspy import MySportsFeeds
import simplejson

msf = MySportsFeeds(version="2.0", verbose = True)
print(msf.authenticate("0c83cfaa-63a0-4cc2-9300-3ab9dd", 'MYSPORTSFEEDS'))
print('at least we get this far')
