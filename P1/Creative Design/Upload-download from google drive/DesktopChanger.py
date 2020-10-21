import ctypes
import os
import time

directory = "F:\\Master\\P1\\CreativeDesign\\project\\Mine\\K\\T\\R\\images"
def changeBG():
    while True:
        for root,dirs,filenames in os.walk(directory):

            for i in filenames:
                    start=time.time()
                    SPI_SETDESKTOPWALLPAPER=20
                    image = directory + "\\" + i
                    print(image)
                    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER,0,image,3)
                    time.sleep(4)
                    
changeBG()