#
# App icon generator for Cocos2d-X projects
# by damianbal
#

import sys
import os
import shutil

#
# To install PIL
# 1. sudo easy_install pip
# 2. sudo pip install pillow
#
from PIL import Image

filename = sys.argv[1] # app icon to be resized

def open_resize_save(f,new_filename,new_width,new_height):
    img = Image.open(f)
    new_img = img.resize((new_width,new_height),Image.ANTIALIAS)
    new_img.save(new_filename,'png')

def genFor_iOS(f):
    open_resize_save(f,'ios/Icon-29.png',29,29)
    open_resize_save(f,'ios/Icon-40.png',40,40)
    open_resize_save(f,'ios/Icon-50.png',50,50)
    open_resize_save(f,'ios/Icon-57.png',57,57)
    open_resize_save(f,'ios/Icon-58.png',58,58)
    open_resize_save(f,'ios/Icon-72.png',72,72)
    open_resize_save(f,'ios/Icon-76.png',76,76)
    open_resize_save(f,'ios/Icon-80.png',80,80)
    open_resize_save(f,'ios/Icon-87.png',87,87)
    open_resize_save(f,'ios/Icon-100.png',100,100)
    open_resize_save(f,'ios/Icon-114.png',114,114)
    open_resize_save(f,'ios/Icon-120.png',120,120)
    open_resize_save(f,'ios/Icon-144.png',144,144)
    open_resize_save(f,'ios/Icon-152.png',152,152)
    open_resize_save(f,'ios/Icon-180.png',180,180)

def genFor_Android(f):
    open_resize_save(f,'android/mipmap-hdpi/ic_launcher.png',72,72)
    open_resize_save(f,'android/mipmap-mdpi/ic_launcher.png',48,48)
    open_resize_save(f,'android/mipmap-xhdpi/ic_launcher.png',96,96)
    open_resize_save(f,'android/mipmap-xxhdpi/ic_launcher.png',144,144)



shutil.rmtree('ios')
shutil.rmtree('android')

os.makedirs('ios')
os.makedirs('android')
os.makedirs('android/mipmap-hdpi')
os.makedirs('android/mipmap-mdpi')
os.makedirs('android/mipmap-xhdpi')
os.makedirs('android/mipmap-xxhdpi')
genFor_iOS(filename)
genFor_Android(filename)
