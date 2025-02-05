# utils/data_loader.py

import json

def load_titles(json_file):
    """
    Load titles from a JSON file.
    
    The JSON file is assumed to be a list of dictionaries with keys 'id' and 'title'.
    
    Args:
        json_file (str): Path to the JSON file.
    
    Returns:
        list: A list of dictionaries, each representing a record.
    """
    with open(json_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    return data
