import json

def read_json_as_list(file_path, outputName):
    """
    Reads a JSON file and returns its content as a list.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    list: The content of the JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                raise ValueError("JSON content is not a list")
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

import os
def traverse_and_process_json_files(directory):
    """
    Traverse all JSON files in the specified directory and process them.

    Parameters:
    directory (str): The directory to traverse.

    Returns:
    None
    """
    pairName=[]
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                outputName=""
                if("zhuoran" in file):
                    outputName = "zhuoran"
                elif("turui" in file):
                    outputName = "turui"
                else:
                    outputName = "wangpan"
                pairName.append([file_path, outputName])
    return  pairName  
# Example usage:
# json_list = read_json_as_list('path_to_your_json_file.json')
# print(json_list)
