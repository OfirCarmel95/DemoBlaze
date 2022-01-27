import json
def read_data(file_path):
    output = []
    f = open(file_path)
    data = json.load(f)
    for obj in data:
        output.append(tuple(obj.values()))
    return output
