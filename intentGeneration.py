import csv
import json

my_name = "Miguel"#input()
target_Name = "Laura  Munhoz ⚓"#input()
#Laura  Munhoz ⚓ Miguel

flag = 0
count = 0
dictAuxFile = {}
listDict = []

with open('dataset.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        text = row['messages__content']
        if text == "":
            continue

        listTargetwords = []
        listResponses = []
        if(row['messages__sender_name'] == my_name):
            print(text)
            if flag == 1:
                listResponses.append(text)
                flag = 2
        else:
            if(flag > 1):
                flag = 0
                count += 1
                dictAuxFile["tag"] = str(count)
                dictAuxFile["patterns"] = listTargetwords
                dictAuxFile["responses"] = listResponses
                listDict.append(dictAuxFile)
            else:
                flag = 1
                listTargetwords.append(text)
                print(text)



fileIntent = {"intents":listDict}

# Serializing json
json_object = json.dumps(fileIntent, indent=1)

# Writing to sample.json
with open("intentExample.json", "w") as outfile:
    outfile.write(json_object)