import ctypes
import os
import time

#add the directory to the folder containing the images you want to sweep between as desktop wallpaper
directory = "E:\\images\\Backgrounds" 
def changeBG():
    while True:
        for root,dirs,filenames in os.walk(directory):

            for i in filenames:
                    start=time.time()
                    SPI_SETDESKTOPWALLPAPER=20
                    image = directory + "\\" + i
                    #print the directory to the image to be displayed 
                    print(image)
                    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER,0,image,3)
                    #time interval between each desktop wallpaper change
                    time.sleep(10)
                    
changeBG()
