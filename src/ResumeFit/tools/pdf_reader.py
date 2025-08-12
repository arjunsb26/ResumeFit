from langchain.document_loaders import PyPDFLoader

# Load your PDF file
# This gives you one Document per page (we assume the resume is one page)
pages = PyPDFLoader("inputs/jakes-resume.pdf").load()

doc = pages[0]
# print(doc)
print(repr(doc.page_content))