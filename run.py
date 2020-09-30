import os
import glob

name_list = []
root = 'D:/La Net/Python Django/23. First Clone Project/'

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

root_dir = root_dir.replace('\\','/')
file1 = open("try.txt","a")

for name in glob.glob(root+'*.mp4'):
    name_list.append(name)

#Adding the files to a txt file called try.txt
for i in name_list:
    s=""
    i=i.replace('.mp4','') #Removing the extension
    s = i+"\n"
    file1.write(s)
    print(i.replace(root_dir,''))

file1.close()