import shutil
import os

#set where the source of the files are
src = '/Users/miked/Desktop/folderA/'

#set the destination path to folderB
dst = '/Users/miked/Desktop/folderB/'
files = os.listdir(src)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(src+i, dst)
