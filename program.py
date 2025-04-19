import os,sys

dir=os.path.dirname(__file__)

address=dir.replace("\\","/")

addressData=address+"/Data/"

print (os.listdir(addressData))

ste=os.listdir(addressData)

os.chdir( addressData )
size0=0
video=""
audio=""
for i in ste:
    file=open(addressData+i,"r")
    size=os.path.getsize(addressData+i)
    file.close()
    if size > size0:
        size0=size
        video=i

ste=os.listdir(addressData)
for i in ste:
    if i != video:
        auido=i

os.rename(addressData+video,addressData+"video.m4s")
os.rename(addressData+auido,addressData+"audio.m4s")


address+="/"

name=input("Enter the name of the video file: ")

property=address+"ffmpeg/bin/ffmpeg.exe -i "+address+"Data/video.m4s -i "+address+"Data/audio.m4s -codec copy "+address+name+".mp4"



os.system(property)

os.remove(address+"Data/video.m4s")
os.remove(address+"Data/audio.m4s")
