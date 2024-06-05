import os
import json

def classify_and_format_json(readPath):
    # 初始化返回的list
    classified_list = [[], [], []]
    
    # 遍历指定路径下的所有文件
    for filename in os.listdir(readPath):
        if filename.endswith('.json'):
            # 构造文件完整路径
            filepath = os.path.join(readPath, filename)
            
            # 读取json文件内容
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # 提取并格式化需要的字段
                formatted_data = []
                for entry in data:
                    print(entry)
                    formatted_entry = {
                        "Post": entry["Post"],
                        "Transfer_post": entry["Transferred_Post"],
                    }
                    formatted_data.append(formatted_entry)
                
                # 根据文件名中的关键词将数据放入相应的列表
                if "IAS2EAS" in filename:
                    classified_list[0].extend(formatted_data)
                elif "SAS2UAS" in filename:
                    classified_list[1].extend(formatted_data)
                elif "GAS2SPAS" in filename:
                    classified_list[2].extend(formatted_data)
    return classified_list

def classify_and_format_json2(readPath):
    # 初始化返回的list
    classified_list = [[], [], []]
    
    # 遍历指定路径下的所有文件
    for filename in os.listdir(readPath):
        if filename.endswith('.json'):
            # 构造文件完整路径
            filepath = os.path.join(readPath, filename)
            
            # 读取json文件内容
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # 提取并格式化需要的字段
                formatted_data = []
                for entry in data:
                    formatted_entry = {
                        "Post": entry["Post"],
                        "Transfer_post": entry["Transfer_post"],
                    }
                    formatted_data.append(formatted_entry)
                
                # 根据文件名中的关键词将数据放入相应的列表
                if "IAS2EAS" in filename:
                    classified_list[0].extend(formatted_data)
                elif "SAS2UAS" in filename:
                    classified_list[1].extend(formatted_data)
                elif "GAS2SPAS" in filename:
                    classified_list[2].extend(formatted_data)
    
    return classified_list


def update_and_sort_lists(dealList, originList):
    resultList = []

    for i in range(len(dealList)):
        deal_dict = {item["Post"]: item for item in dealList[i]}  # Create a dictionary for quick lookup

        updated_list = []
        for item in originList[i]:
            if item["Post"] in deal_dict:
                updated_list.append(deal_dict[item["Post"]])  # Replace with dealList item
            else:
                updated_list.append(item)  # Keep the original item

        resultList.append(updated_list)

    return resultList

# Example usage:
# dealList = [[{"ID": 1, "Post": "A", "Transfer_post": "B"}], [{"ID": 2, "Post": "C", "Transfer_post": "D"}]]
# originList = [[{"ID": 1, "Post": "X", "Transfer_post": "Y"}, {"ID": 3, "Post": "Z", "Transfer_post": "W"}], [{"ID": 2, "Post": "E", "Transfer_post": "F"}]]
# result = update_and_sort_lists(dealList, originList)
# print(result)


# 示例调用
readPath = 'DealJson'  # 替换为你的实际路径
dealList = classify_and_format_json2(readPath)

readPath = "OriginJson"
originList = classify_and_format_json(readPath)

resultList= update_and_sort_lists(dealList, originList)


import alignment
alignment.write_to_json(resultList[0], "IAS2EAS_Human_1_100_.json")
alignment.write_to_json(resultList[1], "SAS2UAS_Human_1_100_.json")
alignment.write_to_json(resultList[2], "GAS2SPAS_Human_1_100.json")
