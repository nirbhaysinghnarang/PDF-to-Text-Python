import os
import tempfile
from pdf2image import convert_from_path
class Converter:
	def __init__(self,file_name,target_name):
		self.file_name = file_name
		self.target_name = target_name
	def convert(self):
		os.mkdir(os.getcwd()+"/images/")
		with tempfile.TemporaryDirectory() as path:
			images_from_path = convert_from_path(self.file_name, output_folder=path)
			i = 1
			for image in images_from_path:
				image.save(os.getcwd()+"/images/"+self.target_name + "_pg_" + str(i) + '.jpg', 'JPEG')
				i = i + 1
