#!/usr/bin/python

import httplib, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--headers", help="print the http headers of the http response", action="store_true")
parser.add_argument("-b", "--body", help="print the body of the http response", action="store_true")
parser.add_argument("-r", "--status", help="print the status code of the http response", action="store_true")
parser.add_argument("-s", "--ssl", help="choose if the request is over ssl", action="store_true")
parser.add_argument("-c", "--chrome", help="Use Chrome on Mac User Agent", action="store_true")
parser.add_argument("-i", "--ie6", help="Use Internet Explorer 6.0 User Agent", action="store_true")
parser.add_argument("-m", "--safari", help="Use Mac Safari User Agent", action="store_true")
parser.add_argument("-e", "--edge", help="Use Edge User Agent", action="store_true")
parser.add_argument("URL", help="Enter a url without leading http:// or https://")
args = parser.parse_args()

x=1
filename = ''
host = args.URL.split('/')

for x in range (1, len(host), 1):
        filename = filename+'/'+host[x]
        x=x+1
method = 'GET'
headers = {"Accept": "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-powerpoint, application/vnd.ms-excel, application/msword, application/x-shockwave-flash, */*", "Accept-Language": "en-us", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MANM; rv:11.0) like Gecko", "Connection": "Keep-Alive"}

if args.ie6:
    headers["User-Agent"] = "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"
elif args.chrome:   
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
elif args.safari:
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko)"
elif args.edge:
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"

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
