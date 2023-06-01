#imports
from tkinter import *
from pygame import mixer
import os

#if you don't have it type pip install the imports used above in command line
#this is in case you forgot like i did lol


# song option code
def playsong():
    currentsong = playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()
def pausesong():
    mixer.music.pause()
def stopsong():
    mixer.music.stop()
def resumesong():
    mixer.music.unpause()

# The UI & song Directory
root = Tk()
root.title("Simple Music Player")
mixer.init()

playlist = Listbox(root,selectmode=SINGLE,bg = "blue")
playlist.grid(columnspan = 5)
os.chdir('/Users/novel/Documents/songs')
song = os.listdir()
for s in song:
    playlist.insert(END,s)
Button(root,text = "Play",command = playsong).grid(row = 1, column =0)
Button(root,text = "Pause",command = pausesong).grid(row = 1, column =1)
Button(root,text = "Resume",command = resumesong).grid(row = 1, column =2)
Button(root,text = "Stop",command = stopsong).grid(row = 1, column =3)
mainloop()




