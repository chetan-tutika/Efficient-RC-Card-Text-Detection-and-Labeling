from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
from PIL import Image
import pytesseract
import os
import itertools

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image")
args = vars(ap.parse_args())

def trans(image):
	rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
	sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
	tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, rectKernel)
	gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0,ksize=-1)
	gradX = np.absolute(gradX)
	(minVal, maxVal) = (np.min(gradX), np.max(gradX))
	gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
	gradX = gradX.astype("uint8")
	gradX = cv2.morphologyEx(gradX, cv2.MORPH_DILATE, rectKernel)
	thresh = cv2.threshold(gradX, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	rectKernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 5))
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, rectKernel1)
	rectKernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (27, 5))
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, rectKernel2)
	return thresh
image = cv2.imread(args["image"])
image2=image.copy()
image3=image.copy()
h,w=image.shape[:2]
print(w,h)
image=image[85:h,185:int(w/2)-12]
image2=image2[85:h,int(w/2):650]
image = imutils.resize(image, width=300,height=402)
image2 = imutils.resize(image2, width=300)
image = cv2.resize(image, (300, 402)) 
gray1 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image2.shape[:2])
print(image.shape[:2])
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
thresh=trans(gray)
thresh1=trans(gray1)
thresh = cv2.resize(thresh, (300, 402)) 
x1=[]
y1=[]
w1=[]
h1=[]
x2=[]
y2=[]
w2=[]
h2=[]
print(thresh1.shape[:2])
print(thresh.shape[:2])
cv2.imshow("th1",thresh)
cv2.imshow("th2",thresh1)
image1=image.copy()
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = contours.sort_contours(cnts,method="top-to-bottom")[0]
locs = []
cnts1 = cv2.findContours(thresh1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts1 = cnts1[0] if imutils.is_cv2() else cnts1[1]
cnts1= contours.sort_contours(cnts1,method="top-to-bottom")[0]
locs1 = []
for (i, c) in enumerate(cnts):	
	(x, y, w, h) = cv2.boundingRect(c)
	locs.append((x, y, w, h))
	x1.append(x)
	y1.append(y)
	w1.append(w)
	h1.append(h)
for (i, c) in enumerate(cnts1):
	(x, y, w, h) = cv2.boundingRect(c)
	locs1.append((x, y, w, h))
	x2.append(x)
	y2.append(y)
	w2.append(w)
	h2.append(h)
for (x,y,w,h) in locs:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
info=[]
info1=[]
print(len(locs))
output = []
cv2.imshow("ims",image)
for (i, (gX, gY, gW, gH)) in enumerate(locs):
	groupOutput = []
	#print("i",i)
	group = gray[gY-5 :gY + gH, gX:gX + gW-10]
	#group = cv2.GaussianBlur(group, (5,5),0)
	group = cv2.threshold(group, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	kernel = np.ones((2,1),np.uint8)
	group = cv2.erode(group,kernel,iterations = 1)
	filename1 = "{}.jpg".format(os.getpid())
	cv2.imwrite(filename1, group)
	text1 = pytesseract.image_to_string(Image.open(filename1))
	os.remove(filename1)
	info1.append(text1)
cv2.imshow("gr",gray1)
x1=list(x1)
y1=list(y1)
w1=list(w1)
h1=list(h1)
print(x1[0])
x2=list(x2)
y2=list(y2)
w2=list(w2)
h2=list(h2)
for i in range(8):
	#print(i)
	if i<7:
		group = gray1[y1[i]-5 :y1[i+1]-5, x2[i]+5:x2[i] + w2[i]+13]
		#group = cv2.GaussianBlur(group, (5,5),0)
		group = cv2.threshold(group, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		cv2.rectangle(image2,(x2[i]+5,y1[i]-5),(x2[i]+w2[i]+40,y1[i+1]-5),(0,255,0),2)
	else:
		group = gray1[y1[i]-5 :y1[i] + h1[i]+5, x2[i]-10:x2[i] + w2[i]+10]
		group = cv2.threshold(group, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
		cv2.rectangle(image2,(x2[i]-10,y1[i]),(x2[i]+w2[i]+10,y1[i]+h1[i]+5),(0,255,0),2)
	group = cv2.GaussianBlur(group, (3,3),0.7)
	kernel = np.ones((2,1),np.uint8)
	group = cv2.dilate(group,kernel,iterations = 2)
	kernel = np.ones((3,1),np.uint8)
	group = cv2.erode(group,kernel,iterations = 1)
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, group)
	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)
	info.append(text)
info = [i.replace('\n',' ') for i in info]
info = [i.replace('','') for i in info]
print(info)
print(info1)
dicts={}
dicts=dict(zip(info1, info))
print(dicts)
cv2.imshow("ims1",image2)
cv2.waitKey(0)
