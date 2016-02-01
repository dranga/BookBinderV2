import subprocess
import os
import re

class PdfGen:
	#run pdflatex
	@staticmethod
	def GeneratePdf(latexFile_path) :
		#print ">>>>"
		#print 'latexmk -pdf -pdflatex=\"pdflatex -interaction=batchmode\" ' + latexFile_path
		os.chdir(os.path.dirname(latexFile_path))
		subprocess.call('latexmk -pdf -pdflatex=\"pdflatex -interaction=batchmode\" ' + latexFile_path, shell=True);
		subprocess.call('latexmk -pdf -pdflatex=\"pdflatex -interaction=batchmode\" ' + latexFile_path, shell=True);
		return 0

	#compute number of pages in pdf
	@staticmethod
	def CountPdfPages(file_path) :
		output = subprocess.check_output("pdfinfo " + file_path + "", shell=True)
		m = re.search("Pages:\s*(\d+)", output)
		numberPages = m.group(1)
		return numberPages

	#is pdf even
	@staticmethod
	def PdfEven(file_path) :
		evenCnt = (int(PdfGen.CountPdfPages(file_path))%2 == 0)
		return evenCnt
