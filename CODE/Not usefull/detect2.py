from utils import *
from matplotlib import pyplot as plt
import subprocess
from gtts import gTTS
import tkinter
from tkinter import filedialog
from tkinter import *
max_val = 5
max_directory = -1
file_in_dec=-1
max_kp = 0
orb = cv2.ORB_create()
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/home/Desktop/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print(root.filename)
test_img = read_img(root.filename)
root.destroy()
original = resize_img(test_img, 0.4)
(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set=['10','20','50','100','200','500','2000']

print("Starting Training : \n")
useful=[]
for i in range(0,len(training_set)):
	directory_name=training_set[i]
	print(directory_name)
	for j in range(1,4):
		image_name=str(directory_name+'/'+str(j)+'.jpg')
		print('Training ',image_name,' : ')
		train_img=cv2.imread(image_name,0)
		(kp2, des2) = orb.detectAndCompute(train_img, None)
		bf = cv2.BFMatcher()
		all_matches = bf.knnMatch(des1, des2, k=2)
		good = []
		for (m, n) in all_matches:
			if m.distance < 0.8 * n.distance:
				good.append([m])
		for address in good:
			print(address)
		if len(good) > max_val:
			max_val=len(good)
			max_directory=i
			file_in_dec=j
			useful=good
			max_kp=kp2
		print(j,' ',image_name,' ',len(good))

print("Training end\n")

if max_val >= 5:
	print(training_set[max_directory])
	print(file_in_dec)
	print('good matches ', max_val)
	image_name=str('/'+training_set[max_directory]+'/'+str(file_in_dec)+'.jpg')
	train_img = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
	note = str(training_set[max_directory])
	print('\nDetected denomination: Rs.', note)
else:
	print('No Matches')

print("\nFinished\n")


