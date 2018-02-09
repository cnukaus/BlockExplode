#https://stackoverflow.com/questions/6386308/http-requests-and-json-parsing-in-python
#https://www.dataquest.io/blog/python-json-tutorial/

import json,requests
import ijson
import ast

r = requests.get('https://api.github.com/users/cnukaus')
print (r.json()['created_at'])
print(type(r.json()))
#print (requests.get('https://api.github.com/users/cnukaus/repos').json())#print (json.loads(r.text))
for item in r.json():
		print (item,r.json()[item])

r = requests.get('https://api.github.com/users/cnukaus/repos')

#print (requests.get('https://api.github.com/users/cnukaus/repos').json())#print (json.loads(r.text))
i=0
_max
original_cnt=0
for item in r.json():
		print (item['created_at'])
		print(requests.get(item[contributors_url]))
		if item['fork']='false' then:
			original_cnt=original_cnt+1


		i=i+1


filename='test\example.json'
with open(filename, 'r') as f:

	#print(f.read().strip())
	print(ast.literal_eval(requests.get('http://maps.googleapis.com/maps/api/directions/json').text))
	#print(ast.literal_eval(requests.get('https://api.github.com/users/benadaba').text))
	#print(ast.literal_eval(requests.get('https://github.com/timeline.json').text))
	for jsonobject in requests.get('https://api.github.com/users/cnukaus/repos').text:#ast.literal_eval(f.read()):

		#"[{1,\n2}]".strip()
		pass#print (jsonobject) 

	'''objects = ijson.items(f, 'private')
	print (f.read())
	columns = list(objects)'''
	#print (columns[0])
   		 #for c in item['created_at']:
   		 #    print(c['site_admin'])
 #"fork": false