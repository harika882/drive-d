"""for install any packages in pycharm goto
file-settings-project name-project interpreter-search and add package"""
from PIL import Image,ImageEnhance
import os
import shutil
# print(os.getcwd())
# os.chdir(r"e:\python practice")
# img1=Image.open(r"E:\python practice\dog.jpg")
# # img.save("dog.png")
# # shutil.rmtree(r"E:\python practice\dog")
# # img.show("dog.png")
# maxsize=(500,500)
# img1.thumbnail(maxsize)
# img1.save(r"E:\python practice\dog3.jpg")
# for item in os.listdir(os.getcwd()):
#     if item.endswith(".jpg"):
#         fileName,exension=os.path.splitext(item)
#         img=Image.open(item)
#         enhancer=ImageEnhance.Color(img)
#         enhancer.enhance(5).save( f"{fileName}.jpg" )
#         max_size = (250,250)
#         img.thumbnail ( max_size )
#         img.save ( f"{fileName}.jpg" )

os.chdir(r"E:\balu")
print(os.getcwd())
videos_ext=("mp4","mkv","flv","mpeg")
audioes_ext=("mp3","m4a",".wav","flac","mp5")
doc_ext=("ppt","doc","pdf","txt","vpn")
# os.mkdir("audioes")
# os.mkdir('videos')
list=["audioes","vedioes","documents"]
for item in list:
    if os.path.exists(item):
        print(f"{item} is already exists")
    else:
        os.mkdir(item)
# shutil.move(r"e:\balu\documents\anil.jpg",r"e:\balu")
list1=[]
for filename,dirname,path in os.walk(r"e:\balu"):
    for item in dirname:
         list1.append(item)
print(list1)
folder_path=input("enter folder path")
def file_founder(folder_path,file_extensions):
    l=[]
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                l.append(file)

    return l
pic_ext=("jpg","png",)
doc=file_founder(folder_path,videos_ext)
print(doc)
# for file in doc:
#     shutil.move(file,r"E:\balu\audioes\vidioes")
# shutil.rmtree(r"e:\balu\audioes\file")



