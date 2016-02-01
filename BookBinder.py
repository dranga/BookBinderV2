from latexgen import LatexGen
from pdfgen import PdfGen

import os

def BookBinder(covers, bookOptions, sections, makeBookEven, generatePdf, latexFile_path) :
	pdfFile_path = os.path.splitext(latexFile_path)[0] + ".pdf"
	latexCode = LatexGen.GenerateLatex(covers, bookOptions, sections)
	LatexGen.LatexWrite(latexFile_path, latexCode)
	
	if generatePdf :
		PdfGen.GeneratePdf(latexFile_path)
	
		if ((makeBookEven == True) and not PdfGen.PdfEven(pdfFile_path)) :
			bookOptions['blankBeforeBackCover'] = True
			latexCode = LatexGen.GenerateLatex(covers, bookOptions, sections)
			LatexGen.LatexWrite(latexFile_path, latexCode)
			PdfGen.GeneratePdf(latexFile_path)
	
	if generatePdf :
		return pdfFile_path
	else :
		return latexFile_path
	
	

if __name__ == "__main__" :
	
	covers = []
	covers.append("cover.pdf")
	covers.append("BACK.pdf")
	
	margins = {}
	margins['top'] = 1
	margins['bottom'] = 0.75
	margins['left'] = 2
	margins['right'] = 0.25
	
	bookOptions = {}
	bookOptions['toc'] = True
	bookOptions['blankBeforeBackCover'] = False # if makeEven is True and Pdf is not even toggle this
	bookOptions['blankAfterFrontCover'] = True
	bookOptions['margins'] = margins
	
	sections = []
	sections.append({'sectionName' : "Section1", 'filepath' : "sec1.pdf", 'makeEven' : True})
	sections.append({'sectionName' : "Section2", 'filepath' : "sec2.pdf", 'makeEven' : True})
	sections.append({'sectionName' : "Section3", 'filepath' : "sec3.pdf", 'makeEven' : True})
	
	makeBookEven = False
	generatePdf = True
	
	latexFile_path = "tmpBook.tex"
	
	print BookBinder(covers, bookOptions, sections, makeBookEven, generatePdf, latexFile_path)
