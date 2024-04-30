import os
import json

# 定义文件夹路径
folder_path= "ForFilter_IAS2EAS"

Data=[]

if os.path.exists(folder_path):
    for index in range(1,11):
        File_name=f"Filter_IAS2EAS_{index}.json"
        File_path = os.path.join(folder_path, File_name)
        with open(File_path, 'r', encoding='utf-8') as f:
            tempData = json.load(f)  # 将 JSON 文件加载到数据变量中
            for data in tempData:
                Data.append(data)

    print(Data)
    file_name = f"IAS2EAS.json"
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(Data, f, ensure_ascii=False, indent=4)