from convert import Converter
from reader import Reader
from writer import Writer
from PyPDF2 import PdfFileReader
import os
import sys

class pdf_to_txt():
	def __init__(self,file_name,target_name):
		self.file_name = file_name
		self.target_name = target_name
		try:
			reader = PdfFileReader(open(file_name+".pdf",'rb'))
			self.pg_count = reader.getNumPages()
		except:
			raise ValueError("Could not find the file named {} in {}.".format(self.file_name,os.getcwd()))
			sys.exit()

	def convert_to_text(self):
		converter = Converter(self.file_name+".pdf",self.target_name)
		converter.convert()
		reader = Reader(self.target_name,self.pg_count)
		extracted_text = reader.get_text()
		extracted_text = os.linesep.join([s for s in extracted_text.splitlines() if s])
		writer = Writer((self.target_name+".txt"),extracted_text)
		writer.write()
