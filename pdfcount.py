import re

#rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)

#def countPages(filename):
#    data = file(filename,"rb").read()
#    return len(rxcountpages.findall(data))

#if __name__=="__main__":
#    print "Number of pages in PDF File:", countPages("/home/drr/Desktop/tempbook.pdf")

import sys
import os

f=open ("/home/drr/Desktop/tempbook.pdf", mode='rb')
a=0
while a==0:
    x=f.readline()
    if x == b'<</Type/Pages\n':
        x=f.readline()
        x=x.replace (b'/Count ', b'')
        x=x.replace (b'\n', b'')
        a=1
        print(int(x))
