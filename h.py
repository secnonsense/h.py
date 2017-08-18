#!/usr/bin/python

import httplib, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--headers", help="print the http headers of the http response", action="store_true")
parser.add_argument("-b", "--body", help="print the body of the http response", action="store_true")
parser.add_argument("-r", "--status", help="print the status code of the http response", action="store_true")
parser.add_argument("-s", "--ssl", help="choose if the request is over ssl", action="store_true")
parser.add_argument("URL", help="Enter a url without leading http:// or https://")
args = parser.parse_args()

x=1
filename = ''
host = args.URL.split('/')

for x in range (1, len(host), 1):
        filename = filename+'/'+host[x]
        x=x+1
method = 'GET'
headers = {"Accept": "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-powerpoint, application/vnd.ms-excel, application/msword, application/x-shockwave-flash, */*", "Accept-Language": "en-us", "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)", "Connection": "Keep-Alive"}

if args.ssl:
    conn = httplib.HTTPSConnection(host[0])
else:
    conn = httplib.HTTPConnection(host[0])	
conn.request(method, filename, None, headers)

httpResponse = conn.getresponse() 
if args.status:
    print "status: ", httpResponse.status 
if args.headers:
    print "message: ", httpResponse.msg  
if args.body:
    print "body: ", httpResponse.read()
conn.close()
