import csv
import json

my_name = "Miguel"#input()
target_Name = "Laura  Munhoz ⚓"#input()
#Laura  Munhoz ⚓ Miguel

flag = 0
count = 0
listDict = []
dictAuxFile = {}
listTargetwords = []
listResponses = []

with open('dataset.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        text = row['messages__content']
        if text == "":
            continue

        if(row['messages__sender_name'] == my_name):
            if flag >= 1:
                listResponses.append(text)
                flag = 2
        else:
            if(flag > 1):
                flag = 0
                count += 1
                dictAuxFile = {}
                dictAuxFile["tag"] = str(count)
                dictAuxFile["patterns"] = listTargetwords
                dictAuxFile["responses"] = listResponses
                listTargetwords = []
                listResponses = []

                print("################")
                listDict.append(dictAuxFile)
                print(dictAuxFile)
            if(flag <= 1):
                flag = 1
                listTargetwords.append(text)



print(listDict)

fileIntent = {"intents":listDict}
print(fileIntent)
# Serializing json
json_object = json.dumps(fileIntent, indent=1)

# Writing to sample.json
with open("intents.json", "w") as outfile:
    outfile.write(json_object)
