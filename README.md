BookBinderV2
============

Version 2 of BookBinder.
A web application to generate custom PDF e-books from PDF sections (front and back covers, and chapters).
Version 2 is written in Python using the Flask framework and Javascript/HTML5 for form validation.

BookBinder generates and compiles a LaTeX file. The resulting PDF is returned to the user.

##Features
* Choice of front cover and addition blank back to the cover
* Choice of back cover
* Numbered pages, in book format (right corner for odd pages and in the left corner for even pages)
* Adjustable page number using page margins
* Addition of a table of contents
* Creating an even number to have the back cover as an even page (like a book)
* Option to make each section even


##Software Dependencies
On a Debian server (Ubuntu 14.04)
* python 2.7
* flask
* latexmk
* texlive-base
* texlive-latex-base
* texlive-latex-recommended
* texlive-latex-extra
* poppler-utils (for pdfinfo)
