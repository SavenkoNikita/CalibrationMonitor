import time

import cv2
import numpy as np
import pyscreenshot as ImageGrab
import pytesseract

filename = 'Image.png'
x = 1
last_time = time.time()

while(True):
    screen = np.array(ImageGrab.grab(bbox=(412, 562, 600, 628)))
    #print('loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    #cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imwrite(filename, screen)
    x = x + 1
    #print(x)
    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img)
    print(str(text))

    #index = text.find("You")
    #print(index)

    #if index == -1:
    #    print("ТАКОГО СЛОВА НЕТЬ!!!")
    #else:
    #    print("Я НАШЕЛЬ ЕНТО СЛОВО!!!")

    if text == str('x222xx77'):
        print('номер обнаружен!')
    else:
        print('ищем номера', sep='', end = '\n')