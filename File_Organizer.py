import os
import datetime
import shutil
import json


# logic
def logic(dir):
    with open("data.json","r") as data:
        folders=json.load(data)
    fileDict={value:key for key in folders for value in folders[key]}
    
    #######

    for z in os.listdir(dir):
        name, ext = os.path.splitext(z)
        ext = ext.lower()
        if ext in fileDict.keys():
            if fileDict[ext] not in os.listdir(dir):
                os.mkdir(dir+f"/{fileDict[ext]}")
                print(f"{fileDict[ext]} folder created.")
            try:
                shutil.move(os.path.join(dir, z), dir+f"/{fileDict[ext]}")
            except:
                FileExistsError
                date = datetime.datetime.now()
                date = date.strftime("%Y-%m-%d-%H-%M-%S")
                os.rename(dir+"/"+z, dir+"/"+name+date+ext)
                logic(dir)


# main function
def main():
    default_path = f"C:/Users/{os.getlogin()}/Downloads"
    source_dir = default_path
    user_inp = input(
        "Enter file path or press [1] for default folder(default is download folder)\n-->")
    if user_inp != "1":
        user_inp = user_inp.replace("\\", "/")
        source_dir = user_inp
    logic(source_dir)


if __name__ == "__main__":
    main()
