# h.py
Basic HTTP/HTTPS client written in Python 2

Usage:

./h.py -rx www.site.com   

This will give http response code (-r) and response headers (-x)

./h.py -srx www.site.com

Add -s for ssl (HTTPS) support

./h.py -b www.site.com 

Use the -b option to display the response body to the screen

note - if only a url is specified the default will be to return just the reponse body

./h.py -o www.site.com 

Use the -o option to save the response body to a file called "output"

./h.py -xr https://www.google.com

http:// or https:// prefixes are supported, https:// negates the need for the -s switch for ssl support

By default the script uses an ie11 user-agent, if you want to specify other agents use:

-i = internet explorer 6.0
-c = chrome on mac
-e = edge browser
-m = mac safari
