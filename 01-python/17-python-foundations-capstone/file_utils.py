import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns its contents as a Python object.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The contents of the JSON file as a Python dictionary.
    """
    with open(file_path, 'r') as f:
        return json.load(f)