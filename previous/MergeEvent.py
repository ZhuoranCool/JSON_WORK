# 首先确保 os 和 json 模块已导入
import os
import json

# 定义两个文件夹路径
folder1_path = "1_event_filtered_all" #event
folder2_path = "IAS2EAS_fewshot_llama3" #transfer_post

# 从 folder1 读取10个 JSON 文件
if os.path.exists(folder1_path) and os.path.exists(folder2_path):
    cont=0
    for index in range(1,11):
        EventFile_name=f"output_chunk_{index}_event_filter.json"
        PostFile_name=f"output_chunk_{index}_event_filter_IAS_IAS2EAS.json"
        EventFile_path = os.path.join(folder1_path, EventFile_name)
        PostFile_path = os.path.join(folder2_path, PostFile_name)
        Event_data=[]
        Post_data=[]
        with open(EventFile_path, 'r', encoding='utf-8') as f:
            Event_data = json.load(f)  # 将 JSON 文件加载到数据变量中
        with open(PostFile_path, 'r', encoding='utf-8') as f:
            Post_data = json.load(f)

        # 对于每个对应的元素合并
        merged_list = []
        for j in range(len(Event_data)):
            merged_dict = {
                "Post": Post_data[j]["Post"],
                "Event": Event_data[j]["Event"],
                "Transferred_Post": Post_data[j]["Transferred_Post"],
            }
            merged_list.append(merged_dict)

        # 写入新的JSON文件
        file_name = f"Merge_IAS2EAS/Merge_IAS2EAS_{index}.json"
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(merged_list, f, ensure_ascii=False, indent=4)
