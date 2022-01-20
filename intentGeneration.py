import csv

my_name = input()
target_Name = input()
#Laura  Munhoz ⚓ Miguel

flag = 0
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
        else:
            flag = 1
            listTargetwords.append(text)

            #tokens = nltk.word_tokenize("And now for something completely different")
            #tagged_sent = nltk.pos_tag(tokens)
            #simplified = [(word, simplify_wsj_tag(tag)) for word, tag in tagged_sent]
            #print(simplified)

            print(text + "&")


