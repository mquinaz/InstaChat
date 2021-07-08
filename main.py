from time import sleep
import pyautogui as pt
import pyperclip as pc

sleep(2)

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

#Process message
def process_message(message):
    msg = str(message).lower()

    if msg == 'oi':
        return 'Tudo bem linda'
    elif msg == 'bebezinho':
        return 'bebezinha'
    elif msg == 'hellooo':
        return 'Agora me falas em ingles sua vadia e o espanhol?'
    elif msg == 'hahahahha':
        return 'nao te rias de mim pfv'
    elif msg == 'eu ein':
        return 'eu o carago'
    elif msg == 'pode ir':
        return 'Para onde princesa?'
    elif msg == 'dr susana':
        return 'A tua chefe e um exemplo de profissional..ela faz cirurgia com talento'
    elif msg == 'to com fome':
        return 'Posso cozinhar para ti imensos pratos deliciosos, queres experimentar?'
    elif msg == 'nope':
        return 'yap'
    elif msg == 'então':
        return 'ent eu gosto disso mas tu nao o que queres?'
    else:
        return 'conta-me uma historia please'

last_message, last_response = '', ''

def chat_Box():
    global last_message, last_response

    current_message = get_messages()
    print(current_message)

    if current_message != last_message:
        last_message = current_message
        print(f'Last copied message: {current_message}')

        # Bot response
        if current_message != last_response:
            response = process_message(current_message)
            last_response = response
            print(f'Bot: {response}')
            move_to_text_input(response)

    else:
        print('No new messages ')

if __name__ == '__main__':
    while True:
        try:
            chat_Box()
            sleep(10)
        except Exception as e:
            print(f'Exception {e}')
            sleep(10)