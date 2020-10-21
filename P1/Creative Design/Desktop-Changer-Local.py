import ctypes
import os
import time

directory = "E:\\images\\Backgrounds"
def changeBG():
    while True:
        for root,dirs,filenames in os.walk(directory):

            for i in filenames:
                    start=time.time()
                    SPI_SETDESKTOPWALLPAPER=20
                    image = directory + "\\" + i
                    print(image)
                    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER,0,image,3)
                    time.sleep(10)
                    
changeBG()
