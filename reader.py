import cv2
import pytesseract as pt
import os
class Reader:
	def __init__(self,img_name,pg_count):
		self.img_name = img_name
		self.pg_count = pg_count
	def get_text(self):
		txt = ""
		for i in range(self.pg_count):
			txt += pt.image_to_string(cv2.imread(os.getcwd()+"/images/"+self.img_name+"_pg_"+str(i+1)+".jpg"))
		return txt
