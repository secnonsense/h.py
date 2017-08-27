#!/usr/bin/python

import httplib, argparse, ssl

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--headers", help="print the http headers of the http response", action="store_true")
parser.add_argument("-b", "--body", help="print the body of the http response", action="store_true")
parser.add_argument("-r", "--status", help="print the status code of the http response", action="store_true")

parser.add_argument("-s", "--ssl", help="choose if the request is over ssl", action="store_true")

parser.add_argument("-c", "--chrome", help="Use Chrome on Mac User Agent", action="store_true")
parser.add_argument("-i", "--ie6", help="Use Internet Explorer 6.0 User Agent", action="store_true")
parser.add_argument("-m", "--safari", help="Use Mac Safari User Agent", action="store_true")
parser.add_argument("-e", "--edge", help="Use Edge User Agent", action="store_true")

parser.add_argument("-v", "--malware", help="Use known bad User Agent malware", action="store_true")
parser.add_argument("-o", "--openvas", help="Use known bad User Agent OpenVAS", action="store_true")
parser.add_argument("-z", "--meterpreter", help="Use known hacking tool User Agent Meterpreter", action="store_true")

parser.add_argument("-f", "--save", help="Save the body to a file", action="store_true")
parser.add_argument("-p", "--proxy", help="Specify the IP address and port of proxy - 127.0.0.1:8080", action="store", dest="proxy")
parser.add_argument("-u", "--uagent", help="Specify a custom user-agent in quotes", action="store", dest="uagent")

parser.add_argument("URL", help="Enter a url with or without leading http:// or https://")
args = parser.parse_args()

if not args.headers and not args.body and not args.status:
    args.body = True

x = 1
filename = ''
host = args.URL.split('/')

if "http" in host[0]:
    if host[0] == "https:":
        args.ssl = True
    host = host[2:]

for x in range(1, len(host), 1):
    filename = filename+'/'+host[x]
    x = x+1
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
elif args.meterpreter:
    headers["User-Agent"] = "Meterpreter"
elif args.malware:
    headers["User-Agent"] = "malware"
elif args.openvas:
    headers["User-Agent"] = "OpenVAS"
elif args.uagent:
    headers["User-Agent"] = args.uagent

if args.proxy:
    if args.ssl or "https://" in args.URL:
        print "\nproxy is not supported for SSL at this time\n"
        quit()
    host[0] = args.proxy
    if "http://" not in args.URL: 
        filename = "http://" + args.URL
    else:
        filename = args.URL    
    print "proxy: " + host[0]
    print "URL: " + filename

if args.ssl:
    conn = httplib.HTTPSConnection(host[0], context=ssl._create_unverified_context())
else:
    conn = httplib.HTTPConnection(host[0])
conn.request(method, filename, None, headers)

httpResponse = conn.getresponse()
if args.status:
    print "\nRESPONSE CODE: ", (httpResponse.status)
if args.headers:
    print "\n========= HEADERS ==========\n", httpResponse.msg
if args.body and not args.status and not args.headers and not args.save:
    print httpResponse.read()
elif args.save:
    print filename
    output = open("output",'w')
    output.write(httpResponse.read())
    output.close()
elif args.body:
    print "============ BODY =============\n", httpResponse.read()
conn.close()
