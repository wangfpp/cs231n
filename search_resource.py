# -*- coding: utf-8 -*-
# @Author: wang
# @Date:   2018-01-09 16:18:55
# @Last Modified by:   wang
# @Last Modified time: 2018-01-09 16:18:58
import urllib
import urllib2
url = 'http://www.someserver.com/cgi-bin/register.cgi'
#user_agent = 'Mozilla/5.0 (X11; Linux x86_64)'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
#headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
print req
response = urllib2.urlopen(req)
the_page = response.read()
print the_page