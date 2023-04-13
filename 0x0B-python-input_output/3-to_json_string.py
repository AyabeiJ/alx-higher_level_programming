import json

def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: An object to be serialized to JSON.

    Returns:
        A JSON string representing the object.

    """
    return json.dumps(my_obj)
