import os
# print(os.getcwd())#it gives current working directory address
# os.mkdir("os module")#createe a folder
# os.mkdir(r"e:\movies2")#change the directory andd createe the folder
# print(os.path.exists("os module"))#check wether the folder exist or not
# if os.path.exists("os module.py"):
#     print("already exists")
# else:
#     os.mkdir("os module")
# open("os_file2","a").close()
# os.mkdir(r"E:\Deepak\songs")#create a folder in another directory
# # print(os.listdir(r"E:\Deepak"))#list of folders
# for list in os.listdir():#finding path cwd folders
#     path=os.path.join(os.getcwd(),list)
#     print(path)
#
# for list in os.listdir(r"e:\deepak"):#finding path another drive folders
#     path=os.path.join("e:\deepak",list)
#     print(path)
# # os.makedirs(r"E:\Deepak\songs\baby\boy")
# for filename,dirname,path in os.walk(r"e:\deepak"):
#     print(f"filename:{filename},dirname:{dirname},path:{path}")
# os.chdir(r"e:\deepak\songs\baby")
# os.rmdir("boy")#if folderr empty it will remove thee folder
import shutil
# os.mkdir(r"e:\os_practice")
# os.chdir(r"e:\os_practice\anil\harika")
# print(os.listdir())
# for path,folder,file in os.walk(r"e:\os_practice"):
#     print(path,folder,file)
# os.rmdir(r"e:\os_practice\anil\harika\deepak")
# os.makedirs("anil/harika/deepak")
# open("anil.txt","a").close()
# import shutil
# shutil.copytree(r"e:\os_practice",r"e:os_practice\anil")
# shutil.rmtree(r"e:\os_practice\anil\harika\anil")
# os.mkdir(r"e:\new")
# shutil.move(r"e:\os_practice\anil\harika",r"e:\new")
# shutil.rmtree(r"e:new")
# os.mkdir(r"e:deepu")
# os.rmdir(r"e:deepu")
# print(dir(os))
# print(os.getcwd())
# os.mkdir("and")
# os.makedirs(r"and\ani\andkjf")
# print(os.listdir())
# for path,fd,file in os.walk(r"e:\and"):
#     print(f"pat:{path},file:{file},fd:{fd}")
# os.rename("anil2.txt","anil")
# print(os.stat("anil"))
# print(os.environ.get(r"e:\anil"))
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
base_dir=os.path.dirname(os.path.abspath(__file__))
temp_dir=os.path.join(base_dir,"templates")
print(base_dir)
print(temp_dir)