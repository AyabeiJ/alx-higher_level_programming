import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file in JSON format.

    Args:
        my_obj: The object to write to the file.
        filename: The name of the file to write to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
