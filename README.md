# InstaTalk

## Train a Neural network with your personality in Instagram, then use it as a chatbot.

![InstaTalk](https://github.com/mquinaz/InstaTalk/blob/main/images/instagramPhoto.png)

### Instructions

- First under settings in instagram we can export all data. This will generate a Json that can be converted into a CSV (https://data.page/json/csv) that we rename to dataset.csv.

- Run **python3 intentGeneration.py** to create a intents.json file with patterns and responses. 

- Then we train a Neural network with this intents.json file running **python3 training.py**.

- Finally run the main program **python3 main.py**.

Note that we have to leave an instagram direct message open with our target user so that pythonautogui works properly. Defining quicker response times and probability confidences is also possible(as this values may depend on the dataset).
