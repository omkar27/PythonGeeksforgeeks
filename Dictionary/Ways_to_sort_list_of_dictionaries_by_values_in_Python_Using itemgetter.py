from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]



print sorted(lis,key = lambda i:i["name"])

print sorted(lis,key = itemgetter('age','name',reverse=True))