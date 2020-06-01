import os
class Writer:
	def __init__(self,filename,text,path):
		self.filename = filename
		self.text = text
		self.path = path
	def write(self):
		os.mkdir(self.path+"/texts/")
		f = open(self.path+"/texts/"+self.filename, "w")
		f.write(self.text)
		f.close()
		print("Text file saved in {}".format(self.path+"/texts/"))
