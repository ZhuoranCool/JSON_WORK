import json

def readJsonOriginal(readpath, writepath):
    # 读取JSON文件
    with open(readpath, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    # 准备处理后的数据
    processed_data = []

    for example in data['examples']:
        # 获取元数据
        metadata = example['metadata']
        
        # 初始化新的 classifications 结构
        new_classifications = {
            "event": None,
            "transfer": None,
            "solution": None
        }
        
        # 遍历原有的 classifications 并放入新的结构
        for classification in example['classifications']:
            classname = classification['classname']
            if "Event" in classname:
                new_classifications["event"] = int(classname[-1])
            elif "Transfer" in classname:
                new_classifications["transfer"] = int(classname[-1])
            elif "Solution" in classname:
                new_classifications["solution"] = int(classname[-1])

        # 构建新的数据结构
        new_example = {
            "content": example['content'],
            "metadata": metadata,
            "classifications": new_classifications
        }
        
        # 添加到处理后的数据列表中
        processed_data.append(new_example)

    # 写入新的JSON文件
    with open(writepath, 'w', encoding='utf-8') as outfile:
        json.dump(processed_data, outfile, ensure_ascii=False, indent=4)

# 示例用法
import os
import json

def traverse_and_process_json_files(directory):
    """
    Traverse all JSON files in the specified directory and process them.

    Parameters:
    directory (str): The directory to traverse.

    Returns:
    None
    """
    pairName=[]
    writeRoot="DealJson"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                output_path=writeRoot
                if("zhuoran" in file):
                    output_path = os.path.join(writeRoot, "zhuoran.json")
                elif("turui" in file):
                    output_path = os.path.join(writeRoot, "turui.json")
                else:
                    output_path = os.path.join(writeRoot, "wangpan.json")
                pairName.append([file_path, output_path])
    return  pairName  


pairName=traverse_and_process_json_files("OriginJson")
for pair in pairName:
    readJsonOriginal(pair[0], pair[1])
