import json, os

def write_json_file(filepath, content):
    with open(filepath, 'w') as f:
        json.dump(content, f, indent=2)
    return True

def read_json_file(filepath):
    jsonInfo = None
    try:
        jsonInfo = json.loads(open(filepath).read())
    except Exception as e:
        print ("Error reading json file", filepath)
    return jsonInfo

def check_if_file_exits(path):
    isFile = os.path.isfile(path)