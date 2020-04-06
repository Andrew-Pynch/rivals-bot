import numpy as np
from grabscreen import grab_screen
import cv2
import time
import os


def process_img(image):
    processed_img = image

    processed_img = processed_img.astype(np.float32)
    processed_img /= 255.0
    # confirm the normalization
    # print('Min: %.3f, Max: %.3f' % (processed_img.min(), processed_img.max()))
    return processed_img


def main():
    last_time = time.time()
    while True:
        # This automatically converts the image to grayscale when it is brought in
        screen = grab_screen(region=(0, 0, 1920, 1080))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
