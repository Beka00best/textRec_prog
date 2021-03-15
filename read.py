#!/usr/bin/python

import fitz

pdf_document = "PDF/english_doc_bad_text.pdf"  
doc = fitz.open(pdf_document)  
print ("number of pages: %i" % doc.pageCount)
  
print(doc.metadata)
page1 = doc.loadPage(0)  
page1text = page1.getText("text")  
print(page1text) 

# for page in doc:
#   text = page.get_text()
#   print(text)