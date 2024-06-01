
def alignment(list1, list2, list3):
    resultlist = []
    
    # 遍历每个位置的dict
    for i in range(len(list1)):
        dict1, dict2, dict3 = list1[i], list2[i], list3[i]
        
        # 初始化一个临时dict来存储符合条件的分类
        temp_dict = {}
        
        # 检查classification里的三个key
        for key in ["event", "transfer", "solution"]:
            value1, value2, value3 = dict1["classifications"][key], dict2["classifications"][key], dict3["classifications"][key]
            
            # 如果在同一个key上同时存在1和3
            if (value1 == 1 and value2 == 3) or (value1 == 3 and value2 == 1):
                temp_dict[key] = (dict1["classifications"][key], dict2["classifications"][key], dict3["classifications"][key])
        
        # 如果temp_dict非空，说明有符合条件的key
        if temp_dict:
            resultlist.append({
                "content": dict1["content"],
                "metadata": dict1["metadata"],
                "classifications": temp_dict
            })
    
    return resultlist
import json

def write_to_json(resultlist, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(resultlist, f, ensure_ascii=False, indent=4)

