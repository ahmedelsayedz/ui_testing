import json


def load_json_file(file_path):
    with open(file_path) as f:
        return json.load(f)
