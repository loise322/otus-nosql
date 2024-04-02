import json
import redis
import datetime

f = open ('/tmp/big.json')
r = redis.Redis ('localhost')

j = json.load(f)

print (datetime.datetime.now())
for s in j:
    r.hset ('myhset', s['_id'], json.dumps(s))
print (datetime.datetime.now())

#2024-03-17 14:33:46.456342
#2024-03-17 14:33:49.654221

print (datetime.datetime.now())
s = r.hgetall('myhset')
print (datetime.datetime.now())

#2024-03-17 14:35:22.243345
#2024-03-17 14:35:22.634553