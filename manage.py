print('beginning phase 2.1')

import glob
all_html_files = glob.glob("content/*html")
print(all_html_files)

print ('beginning phase 2.1.2')

import os

file_path = "content/index.html"
file_name = os.path.basename(file_path)
print(file_name)
name_only, extension = os.path.splitext(file_name)
print(name_only)


#phase 2.1.3
print('beginning phase 2.1.3')

pages = []
pages.append({
	"filename": "content/index.html",
	"title": "index",
	"output": "docs/index.html",
	
	"filename": "content/projects.html",
	"title": "projects",
	"output": "docs/projects.html",
	
	"filename": "content/contact.html",
	"title": "contact",
	"output": "docs/contact.html",
})

print(pages)
	