from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import os
import shutil

import BookBinder

UPLOAD_FOLDER = '/tmp/bookbinderfiles'

DEFAULT_LATEX_FILENAME = "tempBook.tex"
DEFAULT_PDF_FILENAME = "tempBook.pdf"

app = Flask(__name__)

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/about")
def about():
    return render_template('about.html')
    
@app.route("/newBook" , methods=['POST'])
def newBook():
	#get Post request arguments
	#and files
	#config into Bookbinder arguments
	
	shutil.rmtree(UPLOAD_FOLDER)
	os.makedirs(UPLOAD_FOLDER)
	
	#print request.form 
    
	makesectioneven = []
	for index in range(len(request.form.getlist('makesectioneven[]'))) :
		crtEntry = request.form.getlist('makesectioneven[]')[index]
		try :
			nextEntry = request.form.getlist('makesectioneven[]')[index + 1]
		except Exception :
			nextEntry = None
		 
		if ( crtEntry == 'buffer' and nextEntry == 'on') :
			makesectioneven.append(True)
		elif ( crtEntry == 'buffer' and (nextEntry == 'buffer' or nextEntry == None )) :
			makesectioneven.append(False)
		else :
			pass
	
	#print ">>> makesectioneven: " + str(makesectioneven)
	
	margins = {}
	margins['top'] = request.form['top']
	margins['bottom'] = request.form['bottom']
	margins['left'] = request.form['left']
	margins['right'] = request.form['right']
	
	#print ">>> margins: " + str(margins)
	
	if(request.form['makeeven'] == 'on') :
		makeBookEven = True
	else : 
		makeBookEven = False
		
	#print ">>> makeBookEven: " + str(makeBookEven)
	
	if(request.form.getlist('LaTeX')) :
		generatePdf = False
	else : 
		generatePdf = True
	
	#print ">>> generatePdf: " + str(generatePdf)
	
	bookOptions = {}
	 
	if(request.form.getlist('TOC')) :
		bookOptions['toc'] = True
	else : 
		bookOptions['toc'] = False
	
	bookOptions['blankBeforeBackCover'] = False # if makeEven is True and Pdf is not even toggle this
	
	if(request.form.getlist('blankcover')) :
		bookOptions['blankAfterFrontCover'] = True
	else : 
		bookOptions['blankAfterFrontCover'] = False
	
	bookOptions['margins'] = margins

	#print ">>> bookOptions: " + str(bookOptions)
	
	crtFile = None
	
	covers = []
	crtFile = request.files.getlist('cover')[0]
	crtFile.save(os.path.join(app.config['UPLOAD_FOLDER'], crtFile.filename))
	covers.append(os.path.join(app.config['UPLOAD_FOLDER'], crtFile.filename))

	
	crtFile = request.files.getlist('back')[0]
	crtFile.save(os.path.join(app.config['UPLOAD_FOLDER'], crtFile.filename))
	covers.append(os.path.join(app.config['UPLOAD_FOLDER'], crtFile.filename))

	#print ">>> covers: " + str(covers)
	
	sections = []
	#print ">>>>>>> request.form.getlist('sectionnames[]') : " + str(request.form.getlist('sectionnames[]'))
	for index in range(len(request.form.getlist('sectionnames[]'))) :
		print "index is " + str(index)
		sectionname = request.form.getlist('sectionnames[]')[index]
		crtFile = request.files.getlist('files[]')[index]
		filepath = os.path.join(app.config['UPLOAD_FOLDER'], crtFile.filename)
		crtFile.save(filepath)
		makeEven = makesectioneven[index]
		sections.append({'sectionName' : sectionname, 'filepath' : filepath, 'makeEven' : makeEven})
	
	#print ">>> sections: " + str(sections)
	
	return_filepath = BookBinder.BookBinder(covers, bookOptions, sections, makeBookEven, generatePdf, UPLOAD_FOLDER + "/" + DEFAULT_LATEX_FILENAME)
	
	#return file
	if generatePdf :
		return send_from_directory(app.config['UPLOAD_FOLDER'], DEFAULT_PDF_FILENAME, as_attachment=True)
	else :
		return send_from_directory(app.config['UPLOAD_FOLDER'], DEFAULT_LATEX_FILENAME, as_attachment=True)
	

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
