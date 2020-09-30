import os
import glob

name_list = []
root = 'D:/La Net/Python Django/23. First Clone Project/' #Change this to the dir name you want to list
# print(lnroot)
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for name in glob.glob(root+'*.mp4'):
    name_list.append(name)

for i in name_list:
    print(i)
