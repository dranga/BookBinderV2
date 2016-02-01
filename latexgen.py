from pdfgen import PdfGen

class LatexGen:
	#generate latex code
	@staticmethod
	def GenerateLatex(covers, bookOptions, sections) :
		latexCode = ""
		latexCode = latexCode + LatexGen.NewHeader(covers[0], bookOptions['margins'], bookOptions['toc'], bookOptions['blankAfterFrontCover'])
		
		for section in sections:
			latexCode = latexCode + LatexGen.NewSection(section['filepath'], section['sectionName'], section['makeEven'])
			
		latexCode = latexCode + LatexGen.NewFooter(covers[1], bookOptions['blankBeforeBackCover'])
		
		return latexCode
		
	#new section
	@staticmethod
	def NewSection(file_path, sectionName, makeSectionEven = True):
		sectionCode = "\\addcontentsline{toc}{section}{" + sectionName + "}\n" + \
					"\\includepdf[pages=-, pagecommand={}]{" + file_path + "}\n"
		
		if makeSectionEven and not PdfGen.PdfEven(file_path) :
			sectionCode = sectionCode + LatexGen.AddEmptyPage()
		
		sectionCode = sectionCode + "\n"
		return sectionCode	

	#new header
	@staticmethod
	def NewHeader(frontCover_path, margins, toc, pageAfterCover) :
		headerCode = "\\documentclass[twoside, letterpaper]{article}\n" + \
				"\\usepackage{pdfpages}\n" + \
				"\\usepackage{tocloft}\n" + \
				"\\usepackage{geometry}\n\n" + \
				"\\usepackage{fancyhdr}\n" + \
				"\\pagestyle{fancy}\n" + \
				"\\lhead{}\\chead{}\\rhead{}\n" + \
				"\\cfoot{}\n" + \
				"\\fancyfoot[LE,RO]{\\thepage} \n\n" + \
				"\\renewcommand{\\headrulewidth}{0pt}\n" + \
				"\\renewcommand\\cftsecleader{\\cftdotfill{\\cftdotsep}} \n" + \
				"\\setlength\cftaftertoctitleskip{2cm}\n\n" + \
				"\\renewcommand{\\contentsname}{\\sffamily Contents}\n\n" + \
				"\\begin{document}\n\n"

		headerCode = headerCode + "\\includepdf{" + frontCover_path + "}\n"; #coverpage
		
		if pageAfterCover :
			headerCode = headerCode + LatexGen.AddEmptyPage()

		if toc :
			headerCode = headerCode + \
			"\\newgeometry{top=2in,bottom=1in,right=1.5in,left=1.5in}\n" + \
			"{\\large\\sffamily\\tableofcontents}\n\n" #special TOC margins
			
			headerCode = headerCode + LatexGen.AddEmptyPage() + LatexGen.AddEmptyPage()

		headerCode = headerCode + \
		"\\newgeometry{top={" + str(margins['top'])  + "}in,bottom={" + str(margins['bottom']) + \
		"}in,right={" + str(margins['right']) + "}in,left={" + str(margins['left']) + "}in}\n\n" #return to normal margins
		
		return headerCode

	#new footer
	@staticmethod
	def NewFooter(backCover_path, pageBeforeCover) :
		footerCode = ""
		
		if pageBeforeCover :
			footerCode = LatexGen.AddEmptyPage()
		
		footerCode = footerCode + "\\includepdf[pages=-, pagecommand={}]{" + backCover_path + "}\n" + \
				"\\end{document}\n"
		
		return footerCode

	#add empty page
	@staticmethod
	def AddEmptyPage() :
		return "\\null\\newpage\n"

	#save latex
	@staticmethod
	def LatexWrite(filename, latexCode) :
		with open(filename, 'w') as latexFile:
			latexFile.write(latexCode)
