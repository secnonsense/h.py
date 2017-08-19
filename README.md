# h.py
Basic HTTP/HTTPS client written in Python 2

Usage:

./h.py -rx www.site.com   

This will give http response code (-r) and response headers (-x)

./h.py -srx www.site.com

Add -s for ssl (HTTPS) support

./h.py -b www.site.com > test.html

Use the response body only requests (-b) with file redirection to save the web page locally

By default the script uses an ie11 user-agent, if you want to specify other agents use:

-i = internet explorer 6.0
-c = chrome on mac
-e = edge browser
-m = mac safari
