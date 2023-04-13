import json

def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): JSON string to convert.

    Returns:
        The Python object represented by the JSON string.
    """
    return json.loads(my_str)
