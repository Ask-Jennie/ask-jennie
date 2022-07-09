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

def ask_to_select(inputs):
    input_arr = []
    for key in inputs:
        input_arr.append(key)

    idx = 1
    print ("Select Subcommand ...")
    for key in input_arr:
        print (str(idx) + ". " + key)
        idx += 1

    try:
        selected = int(input(">>"))
        return inputs[input_arr[selected-1]], input_arr[selected-1]
    except Exception as e:
        print ("Invalid Option try selecting again")
        return ask_to_select(inputs)