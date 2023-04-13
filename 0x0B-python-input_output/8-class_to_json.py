#!/usr/bin/python3
"""
This module contains a function that returns a dictionary description of an object for JSON serialization.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object.

    Args:
        obj: An instance of a class whose attributes are serializable.

    Returns:
        A dictionary containing the attributes of the input object in a serializable format.

    Examples:
        >>> class MyClass:
        ...     def __init__(self):
        ...         self.name = "John"
        ...         self.age = 30
        ...         self.is_alive = True
        ...         self.address = {
        ...             "street": "123 Main St",
        ...             "city": "New York",
        ...             "state": "NY"
        ...         }
        ...         self.phone_numbers = ["123-456-7890", "098-765-4321"]
        ...
        >>> obj = MyClass()
        >>> class_to_json(obj)
        {'name': 'John', 'age': 30, 'is_alive': True, 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}, 'phone_numbers': ['123-456-7890', '098-765-4321']}
    """
    return obj.__dict__
