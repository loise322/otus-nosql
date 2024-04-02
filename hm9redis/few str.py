import json
import redis
import datetime

f = open ('/tmp/big.json')
r = redis.Redis ('localhost')

j = json.load(f)

print (datetime.datetime.now())
for s in j:
    r.set (s['_id'], json.dumps(s))
print (datetime.datetime.now())

#2024-03-17 14:23:33.360645
#2024-03-17 14:24:36.725234

s = ''
print (datetime.datetime.now())
for key in r.scan_iter():
    s += str(key)
print (datetime.datetime.now())

#2024-03-17 14:24:55.356226
#2024-03-17 14:24:55.634553