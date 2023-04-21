import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file

    Args:
        filename (str): The name of the file to load

    Returns:
        object: The Python object represented by the JSON file

    """
    with open(filename, 'r') as f:
        return json.load(f)
