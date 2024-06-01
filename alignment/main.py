import readDealJson
import alignment
import readOriginJson

pairName=readOriginJson.traverse_and_process_json_files("OriginJson")
for pair in pairName:
    readOriginJson.readJsonOriginal(pair[0], pair[1])


pairs=readDealJson.traverse_and_process_json_files("DealJson")
standard=[]
turui=[]
wangpan=[]
for pair in pairs:
    tempList=readDealJson.read_json_as_list(pair[0],pair[1])
    if(pair[1]=="zhuoran"):
        standard=tempList
    elif(pair[1]=="turui"):
        turui=tempList
    else:
        wangpan=tempList

resultlist=alignment.alignment(standard,turui,turui)
alignment.write_to_json(resultlist,"result.json")
