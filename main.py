from time import sleep
import pyautogui as pt
import pyperclip as pc

sleep(2)

def move_to_text_input(message):
    position = pt.locateOnScreen('images/photo.png', confidence=.7)
    pt.moveTo(position[0:2], duration=.5)
    pt.moveRel(-100, 20, duration=.5)
    pt.doubleClick(interval=.3)

    pt.typewrite(message, interval=.01)
    pt.typewrite('\n')

if __name__ == '__main__':
    move_to_text_input('hello')
