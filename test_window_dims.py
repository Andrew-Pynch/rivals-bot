import time
import os
import cv2
import numpy as np

from utils import XboxController
from getkeys import key_check
from grabscreen import grab_screen

def main():
    last_time = time.time()
    controller = XboxController()
    while True:
        print(controller.read())
        # This automatically converts the image to grayscale when it is brought in
        screen = grab_screen(region=(0, 40, 1920, 1040))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', screen)
        # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()