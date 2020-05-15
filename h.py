#!/usr/bin/python

import urllib
import sys, socket
x=1
filename = ''
host = "https://www.google.com".split('/')
for x in range (1, len(host), 1):
        filename = filename+'/'+host[x]
        x=x+1
method = 'GET'
headers = {"Accept": "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-powerpoint, application/vnd.ms-excel, application/msword, application/x-shockwave-flash, */*", "Accept-Language": "en-us", "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Connection": "Keep-Alive"}
conn = urllib.HTTPConnection(host[0])
conn.request(method, filename, None, headers)
httpResponse = conn.getresponse() 
print ("status: ", httpResponse.status) 
print ("message: ", httpResponse.msg)  
conn.close()
