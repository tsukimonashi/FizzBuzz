__author__ = 'tsukinashi'

import requests

a = input()

r = requests.get('http://connpass.com/api/v1/event/?keyword=%s'% a)

print(r.status_code, r.headers['content-type'])
f = open('save_events.txt' , 'w')

for event in r.json()['events']:
    print(event['event_id'], event['title'])
    f.write(str(event['event_id'])+'\n')