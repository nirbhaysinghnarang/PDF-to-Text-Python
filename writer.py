import os
class Writer:
	def __init__(self,filename,text):
		self.filename = filename
		self.text = text
	def write(self):
		os.mkdir(os.getcwd()+"/texts/")
		f = open(os.getcwd()+"/texts/"+self.filename, "w")
		f.write(self.text)
		f.close()
		print("Text file saved in {}".format(os.getcwd()+"/texts/"))
