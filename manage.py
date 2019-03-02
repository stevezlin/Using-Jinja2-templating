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
	
})

print(pages)


#phase 2.2.2



from jinja2 import Template
index_html = open("content/index.html").read()

template_html = open("templates/base.html").read()
template = Template(template_html)
template.render(
	title="Homepage",
	content=index_html,
)

print('phase 2.2.2 completed')

#phase 2.3.1

{% for page in pages %}
<a href="{{ page.output_filename }}">{{ page.title }}</a>
{% endfor %}
























