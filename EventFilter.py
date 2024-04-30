import os
import json

# 定义文件夹路径
folder_path= "Merge_IAS2EAS"

if os.path.exists(folder_path):
    for index in range(1,11):
        File_name=f"Merge_IAS2EAS_{index}.json"
        File_path = os.path.join(folder_path, File_name)
        tempData=[]
        with open(File_path, 'r', encoding='utf-8') as f:
            tempData = json.load(f)  # 将 JSON 文件加载到数据变量中
        
        #Filter
        Data=[]
        for pair in tempData:
            '''
            pair:
            {
                "Post":...,
                "Event":...,
                "Transferred_Post":...
            }
            '''
            #1. Post: 不要出现cut out或cut for
            if("cut out" in pair["Post"] or "cut for" in pair["Post"]):
                continue

            #2. Transferred_Post: 不要出现tough, challenging, struggling, profound, difficult
            keywords = ["tough", "challenging", "struggling", "profound", "difficult", "frustrating", "frustrated", "disappointed", "disappointing", "defeated"]

            # 你的字符串
            my_string = pair["Transferred_Post"]

            # 使用简单的循环和in操作符来判断是否包含关键字
            contains_keyword = False
            for keyword in keywords:
                if keyword in my_string:
                    contains_keyword = True
            if contains_keyword:
                continue

            #1、2都符合，加入人工筛选
            Data.append(pair)
                            
        file_name = f"ForFilter_IAS2EAS/Filter_IAS2EAS_{index}.json"
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(Data, f, ensure_ascii=False, indent=4)