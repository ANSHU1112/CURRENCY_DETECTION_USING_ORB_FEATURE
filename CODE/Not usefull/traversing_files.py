from utils import *
from matplotlib import pyplot as plt
import subprocess
from gtts import gTTS
import tkinter
from tkinter import filedialog
import PIL.Image
from tkinter import *
training_set=['testing']
for i in range(0,len(training_set)):
	directory_name=training_set[i]
	print(directory_name)
	for j in range(1,3):
		print(j)
		image_name=str(directory_name+'/'+str(j)+'.jpg')
		print(image_name,' ------ \n')
		fp=open(image_name,"rb")
		imagee=PIL.Image.open(image_name)
		imagee.show()
