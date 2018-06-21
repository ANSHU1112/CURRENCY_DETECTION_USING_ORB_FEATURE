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
(keypoint1, des1) = orb.detectAndCompute(test_img, None)

All_directories=['10','20','50','100','200','500','2000']

print("Starting Training : \n")
useful=[]
for i in range(0,len(All_directories)):
	directory_name=All_directories[i]
	print(directory_name)
	for j in range(1,4):
		image_name=str(directory_name+'/'+str(j)+'.jpg')
		print('Training ',image_name,' : ')
		train_img=cv2.imread(image_name,0)
		(keypoint2, des2) = orb.detectAndCompute(train_img, None)
		bf = cv2.BFMatcher()
		all_matches = bf.knnMatch(des1, des2, k=2)
		matched_satisfied = []

		for (m, n) in all_matches:
			if m.distance < 0.8 * n.distance:
				matched_satisfied.append([m])

		for address in matched_satisfied:
			print(address)

		if len(matched_satisfied) > max_val:
			max_val=len(matched_satisfied)
			max_directory=i
			file_in_dec=j
			useful=matched_satisfied
			max_kp=keypoint2
		print(j,' ',image_name,' ',len(matched_satisfied))

print("Training end\n")

if max_val >= 5:
	print(All_directories[max_directory])
	print(file_in_dec)
	print('matched_satisfied matches ', max_val)
	image_name=str('/'+All_directories[max_directory]+'/'+str(file_in_dec)+'.jpg')
	train_img = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
	note = str(All_directories[max_directory])
	print('\nDetected denomination: Rs.', note)
else:
	print('No Matches')

print("outside")


