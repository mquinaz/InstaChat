from time import sleep
import pyautogui as pt
import pyperclip as pc

import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

#Moves cursor to text input box to respond
def move_to_text_input(message):
    position = pt.locateOnScreen('images/photo.png', confidence=.7)
    pt.moveTo(position[0:2], duration=.5)
    pt.moveRel(-100, 20, duration=.5)
    pt.doubleClick(interval=.3)

    pt.typewrite(message, interval=.01)
    pt.typewrite('\n')

#Handles message retrieval
def get_messages():
    position = pt.locateOnScreen('images/smile.png', confidence=.9)
    pt.moveTo(position[0:2], duration=.5)
    pt.moveRel(50, -50, duration=.5)
    pt.click()

    #Click triple dots
    position = pt.locateOnScreen('images/options.png', confidence=.9)
    pt.moveTo(position[0:2], duration=.5)
    pt.click()

    #Click on copy message
    sleep(.5)
    position = pt.locateOnScreen('images/copy.png', confidence=.8)
    pt.moveTo(position[0] + 10, position[1] + 15, duration=.5)
    pt.click()

    user_text = pc.paste()
    return user_text

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intents': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb') )
classes = pickle.load(open('classes.pkl', 'rb') )
model = load_model('chatbot_model.model')

last_message, last_response = '', ''

if __name__ == '__main__':
    sleep(2)
    global last_message, last_response
    while True:
        try:
            current_message = get_messages()
            print(current_message)

            if current_message != last_message:
                last_message = current_message
                print(f'Last copied message: {current_message}')

                # Bot response
                if current_message != last_response:
                    response_Class = predict_class(current_message)
                    response = get_response(response_Class, intents)
                    last_response = response
                    print(f'Bot: {response}')
                    move_to_text_input(response)
            else:
                print('No new messages ')
            sleep(8)
        except Exception as e:
            print(f'Exception {e}')
            sleep(8)