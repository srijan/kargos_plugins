#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <bitbar.title>Todoist Today</bitbar.title>
# <bitbar.version>v1.0.0</bitbar.version>
# <bitbar.author>K.Kobayashi and Srijan Choudhary</bitbar.author>
# <bitbar.author.github>srijan</bitbar.author.github>
# <bitbar.desc>Today's task in your menu bar!</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.image>http://i.imgur.com/f37VtAg.png</bitbar.image>

import sys
import os
if sys.version_info[0] < 3:
    from urllib2 import urlopen, Request
    from urllib import quote_plus
else:
    from urllib.request import urlopen, Request
    from urllib.parse import quote_plus
import json
import datetime

api_key = os.environ.get('TODOIST_API_KEY')

d = datetime.datetime.today()
today = str(d.day)+d.strftime(" %b")
filter = quote_plus(today + " | today | overdue")

url = 'https://beta.todoist.com/API/v8/tasks?filter=' + filter

if not api_key:
    print("Tasks: ☠")
    print("---")
    print("Please set TODOIST_API_KEY environment variable")
else:
    auth_header = "Bearer " + api_key
    try:
        request = Request(url)
        request.add_header('Authorization', auth_header)
        r = urlopen(request)
        items = json.loads(r.read())
        print("Tasks: %d" % len(items))
        print("---")
        for item in items:
            print("⬜ " + item['content'])
    finally:
        r.close()

print("---")
print("Refresh... | refresh=true")
