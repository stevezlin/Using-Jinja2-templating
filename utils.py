import os
import glob
from jinja2 import Template






print ('Using functions and loops to combine pages')

# read all HTML files using ( glob and os)
def create_pages():
		all_html_files = glob.glob("content/*.html")
		print(all_html_files)
		
		for file in all_html_files:
			file_path = file 
			file_name = os.path.basename(file_path)
			name_only, extension = os.path.splitext(file_name)
			print(file_name)
			
			pages = []
			pages.append({
            "filename": each,
            "title": name_only,
            "output": "docs/" + name_only + '.html',
            "link": name_only + '.html',
            "output_filepath": 'docs/' + name_only + '.html'
			})
		

def apply_template():

    for page in pages:
        file_path = page['filename']
        index_html = open(file_path).read()
        page_html = template.render(
            title = page['title'],
            content = index_html,
            pages = pages,
            selected = page["output_filename"]
        )
		open(page['output'], "w+").write(page_html)






	





