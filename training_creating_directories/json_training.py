# JSON Serialization:
#
# Write Python code to serialize a dictionary into a JSON string.
# JSON Deserialization:
#
import json

print('JSON task dumping and loading JSON')
dict = {'Andrew': ['harry potter', 'mcchonahey'],
        'John': ['queen\'s gambit'],
        'Jackson': ['alice in the wonderland'],
        }
json_serialized_data = json.dumps(dict)

print(json_serialized_data, 'json_serialized_data type:' + str(type(json_serialized_data)))

# Write Python code to deserialize a JSON string into a dictionary.
# Working with JSON Files:
#

json_deserialized_data = json.loads(json_serialized_data)
print(json_deserialized_data, 'json_deserialized_data type:' + str(type(json_deserialized_data)))

print()
print('Loading JSON from file task')
# Create a JSON file containing a list of dictionaries, each representing a person's information (name, age, etc.).
#  Write Python code to read and print the data from the JSON file.

with open('file_json.json', 'w') as file:
    file.write(json_serialized_data)

with open('file_json.json', 'r') as file:
    data = json.load(file)
    print(data, 'data type:' + str(type(data)))

print()
print('JSON Validation task')
# JSON Validation:
#
# Define a JSON schema for a configuration file. Write Python code to validate JSON data against this schema using
#  the jsonschema library.

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "email": {"type": "string", "format": "email"},
    },
    "required": ["name", "age"]
}

from jsonschema import validate, ValidationError

# Your JSON data
json_data = '''
{
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}
'''

try:
    # Parse the JSON data
    data = json.loads(json_data)

    # Validate the JSON data against the schema
    validate(instance=data, schema=schema)

    print("JSON data is valid according to the schema.")
except ValidationError as e:
    print(f"JSON validation error: {e}")

print()
print("Custom JSON Encoder task")
# Custom JSON Encoder:
#
# Create a custom JSON encoder that can handle datetime objects. Serialize a dictionary containing datetime objects into
#  a JSON string.

from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data = {
    "event": "meeting",
    "timestamp": datetime.now()
}

# Serialize data using the custom encoder
json_string = json.dumps(data, cls=DateTimeEncoder)
print(json_string)

# Custom JSON Decoder:
#
# Create a custom JSON decoder that can parse JSON data with special formatting (e.g., dates in a custom format).
#  Deserialize a JSON string containing such data.
# Handling Nested JSON:
#
# Create a nested JSON structure representing a family tree. Write Python code to navigate through the JSON data to find
#  specific family members.
# JSON Error Handling:
#
# Write code to handle JSON decoding errors gracefully, providing helpful error messages.
# JSON Performance:
#
# Generate a large JSON dataset (e.g., a list of random numbers) and measure the time it takes to serialize and
# deserialize it using the standard json module. Then, try a faster JSON library like ujson and compare the performance.
# API Interaction:
#
# Interact with a public JSON-based API (e.g., a weather API or a RESTful service). Write Python code to make HTTP
# requests, retrieve JSON data, and process it.
# Security Considerations:
#
# Research and implement security measures to protect against JSON injection attacks when receiving and processing JSON
# data from untrusted sources.
# Logging JSON Data:
#
# Extend an existing Python application to log specific data in JSON format. Use the logging module to achieve this.
# Unicode Handling:
#
# Create a JSON document containing Unicode characters and practice encoding and decoding it properly in Python.
# Data Transformation:
#
# Write Python code to transform JSON data from one format to another. For example, convert a list of JSON objects into a
#  dictionary with unique keys.
# Documentation:
#
# Document the structure and usage of a JSON dataset you're working with. Imagine you're providing this documentation to
# a colleague who needs to understand the data.
