import json
import redis
import datetime

f = open ('/tmp/big.json')
r = redis.Redis ('localhost')

j = json.load(f)
i = 0
print (datetime.datetime.now())
for s in j:
    i += 1
    r.zadd ('zadd', {json.dumps(s) : i})
print (datetime.datetime.now())

#2024-03-17 14:50:34.478365
#2024-03-17 14:50:39.345318

print (datetime.datetime.now())
s = r.zrange('zadd', 0, -1)
print (datetime.datetime.now())

#2024-03-17 14:52:12.745772
#2024-03-17 14:52:12.907456