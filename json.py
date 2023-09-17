import json

# JSON string
employee ='{"name": "Nitin", "department":"Finance",\
"company":"GFG"}'

# Convert string to Python dict
employee_dict = json.loads(employee)
print("Data after conversion")
print(employee_dict)
print(employee_dict['department'])

print("\nType of data")
print(type(employee_dict))


# Data to be written
dictionary = {
    "name": "sunil",
    "department": "HR",
    "Company": 'GFG'
}

# Serializing json
json_object = json.dumps(dictionary)
print(json_object)

# Data to be written
dictionary ={
    "name" : "Nisha",
    "rollno" : 420,
    "cgpa" : 10.10,
    "phonenumber" : "1234567890"
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)


# Initialize JSON data
json_data = '[ {"studentid": 1, "name": "Nikhil", "subjects":\
["Python", "Data Structures"], "company":"GFG"},\
{"studentid": 2, "name": "Nisha", "subjects":\
["Java", "C++", "R Lang"], "company":"GFG"} ]'

# Create Python object from JSON string
# data
data = json.loads(json_data)

# Pretty Print JSON
json_formatted_str = json.dumps(data, indent=4, sort_keys=True)
print(json_formatted_str)