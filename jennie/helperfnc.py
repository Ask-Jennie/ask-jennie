import json

def write_json_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)