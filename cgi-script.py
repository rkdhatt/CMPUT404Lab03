#!/usr/bin/env python

import os, json, cgi

print "Content-type: text/html" # add http header
print # add blank line
print "<html><body><h1>Hello, world!</h1>" #send whatever
print "<form method='POST'><input name='x'></form>" #

# print json.dumps(dict(os.environ), indent=4)

form = cgi.FieldStorage()
 
print "<p>X was: " + cgi.escape(str(form.getvalue('x'))) + "</p>"
# cgi.escape prevents html from being displayed when sent as a value from the form -> provides security.

#print "<p>"+json.dumps(dict(os.environ), indent=4)+"</p>" # look at QUERY_STRING - shows x value(s) being saved

print "</body></html>"
