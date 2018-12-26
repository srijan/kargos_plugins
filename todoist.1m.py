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
    from urllib import urlencode
else:
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
import json
import datetime

api_key = os.environ.get('TODOIST_API_KEY')

if not api_key:
    print("Tasks: ☠")
    print("---")
    print("Please set TODOIST_API_KEY environment variable")

else:
    url = 'https://todoist.com/API/v7/sync'
    value = { 'token': api_key, 'resource_types': '["items"]', 'seq_no': 0 }
    data = urlencode(value).encode('utf-8')

    d = datetime.datetime.today()
    today = str(d.day)+d.strftime(" %b")
    today_y = str(d.day)+d.strftime(" %b ")+str(d.year)

    try:
        request = Request(url, data)
        r = urlopen(request)
        j = json.loads(r.read())
        items = j['items']
        today_items = []
        for item in items:
            due = item['date_string'] # due date of a task
            if (due == today) or (due == today_y):
                today_items.append(item)
        print("Tasks: %d" % len(today_items))
        print("---")
        for item in today_items:
            print("⬜ " + item['content'])
    finally:
        r.close()

print("---")
print("Refresh... | refresh=true")
