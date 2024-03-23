import pyautogui as pag
import time
from PIL import Image,ImageGrab

def c0llide_checker(data):
    for i in range(462,522):
        for j in range(300,336):
            if (data[i,j]<100):
                return 1
            elif (data[i,j-38]<100):
                return 2
    return 0

if __name__ == "__main__":

    time.sleep(3)
    pag.press('up')

    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load() 

        if (c0llide_checker(data)==1):
            pag.press('up')
        elif (c0llide_checker(data)==2):
            pag.press('down')



# time.sleep(3)
# image = ImageGrab.grab().convert("L")
# data = image.load() 

# for i in range(482,542):
#     for j in range(300,336):
#         data [i,j] = 0
#         data [i,j-38] = 0
        
# image.show()