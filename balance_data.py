import os
import sys
import cv2
import numpy as np 
import pandas as pd 
from collections import Counter 

# arg parse for wether or not we want to view data
VIEW = False
try:
    arg = sys.argv[1]
    if arg == 'v' or arg == 'V':
        VIEW = True
except:
    print("Try running again with 'v' flag to view\npython balance_data.py v")



dataset = os.listdir('data/')

def view_dataset(dataset, view=False):
    if view:
        for file in dataset:
            print("FILE = ", file)
            train_data = np.load(f'data/{file}', allow_pickle=True)
            for data in train_data:
                img = data[0]
                choice = data[1]

                cv2.imshow('test', img)
                print(choice)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break    

view_dataset(dataset, VIEW)
