from utils import *
from matplotlib import pyplot as plt
import subprocess
from gtts import gTTS
import tkinter
from tkinter import filedialog
from tkinter import *
max_val = 5
max_pt = -1
max_kp = 0
orb = cv2.ORB_create()
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/home/Desktop/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print(root.filename)
test_img = read_img(root.filename)
root.destroy()
original = resize_img(test_img, 0.4)
(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set = ['files/20.jpg', 
		'files/50.jpg', 
		'files/100.jpg', 
		'files/500.jpg']

print("Starting Training : \n")

for i in range(0, len(training_set)):
	train_img = cv2.imread(training_set[i])
	(kp2, des2) = orb.detectAndCompute(train_img, None)
	bf = cv2.BFMatcher()
	all_matches = bf.knnMatch(des1, des2, k=2)
	good = []
	for (m, n) in all_matches:
		if m.distance < 0.8 * n.distance:
			good.append([m])
	for a in good:
		print(a)
	if len(good) > max_val:
		max_val = len(good)
		max_pt = i
		max_kp = kp2

	print(i, ' ', training_set[i], ' ', len(good))

print("Training end\n")

if max_val != 5:
	print(training_set[max_pt])
	print('good matches ', max_val)
	train_img = cv2.imread(training_set[max_pt])
	img3 = cv2.drawMatchesKnn(test_img, kp1, train_img, max_kp, good, 4)
	sample= str(training_set[max_pt])
	note = str(training_set[max_pt])[6:-4]
	print('\nDetected denomination: Rs.', note)
	(plt.imshow(img3), plt.show())
else:
	print('No Matches')

print("outside")

