import json
import redis
import datetime

f = open ('/tmp/big.json')
r = redis.Redis ('localhost')

j = json.load(f)

print (datetime.datetime.now())
r.set ("key", json.dumps(j))
print (datetime.datetime.now())

#2024-03-17 14:45:36.468945
#2024-03-17 14:45:36.756774

s = ''
print (datetime.datetime.now())
for key in r.scan_iter():
    s += str(key)
print (datetime.datetime.now())

#2024-03-17 14:46:23.456653
#2024-03-17 14:46:23.456967