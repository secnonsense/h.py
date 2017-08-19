# h.py
Basic HTTP/HTTPS client written in Python 2

Usage:

./h.py -rx www.site.com   

This will give http response code (-r) and response headers (-x)

./h.py -srx www.site.com

Add -s for ssl (HTTPS) support

./h.py -b www.site.com > test.html

Use the response body only requests (-b) with file redirection to save the web page locally
