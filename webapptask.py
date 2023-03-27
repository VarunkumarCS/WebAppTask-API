import json
from pprint import pprint as pp

#opening, loading and printing the jsonfile in the python
with open('webapp.json', 'r')as file:
    data = json.load(file)
print()

print("Checking if key exists in the json")
#to check attribute exist in the JSON file
if 'web-app' in data:
    print("Key exist in the JSON data")
    pp(data['web-app'])
else:
    print("Key doesn't exist in JSON data")
print()

print("Checking is the value exist in the JSON file")
#to check the value exit in the JSON file
if (data.get('servlet-mapping')):
    print("value exist in the JSON file")
    print(data.get('servlet-mapping'))
else:
    print("values is not present in the JSON file")
print()

print("Checking if the nested value exist in the JSON file")
#to check the nested value
if 'web-app' in  data['web-app']['servlet']:
    print("The keys and values are")
print(data['web-app']['taglib'])
print()