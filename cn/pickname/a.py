#coding=utf-8
import os


def rename():
    path=input("请输入路径(例如D:\\\\Jason)：")
    name=input("请输入开头名:")
    startNumber=input("请输入开始数:")
    fileType=input("请输入后缀名（如 .jpg、.txt等等）:")
    endSplit = input("请输入分隔符(如 佛系小吴_01_  01 _.ext)  :  ")
    print("正在生成以"+name+startNumber+fileType+"迭代的文件名")
    count=0
    filelist=os.listdir(path)
    for files in filelist:
        Olddir=os.path.join(path,files)
        if os.path.isdir(Olddir) or not files.endswith(fileType):
            continue
        Newdir=os.path.join(path,name+str(count+int(startNumber))+endSplit+fileType)
        os.rename(Olddir,Newdir)
        count+=1

    print("一共修改了"+str(count)+"个文件")


if __name__ == '__main__':
    rename()