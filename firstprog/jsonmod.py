import json
data='{"var1":"harry","var2":56}'
print(data)
parsed=json.loads(data)

print(parsed)
print(parsed['var1'])
print(type(parsed))

data2 ={
    "channel_name":"code with harry",
    "cars":['dzire','bmw'],
    "isbad":False
    }
jscomp=json.dumps(data2)
print(jscomp)

#json.load
#what is sort_keys parameter in dumps
