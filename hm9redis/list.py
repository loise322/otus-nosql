import json
import redis
import datetime

f = open ('/tmp/big.json')
r = redis.Redis ('localhost')

j = json.load(f)

print (datetime.datetime.now())
for s in j:
    r.rpush ('list', json.dumps(s))
print (datetime.datetime.now())

#2024-03-17 14:40:43.544567
#2024-03-17 14:40:47.456742

print (datetime.datetime.now())
s = r.lrange('list', 0, -1)
print (datetime.datetime.now())

#2024-03-17 14:42:41.356889
#2024-03-17 14:42:41.467888

