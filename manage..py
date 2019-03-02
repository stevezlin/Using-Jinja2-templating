import utils

import sys


print("This is argv:", sys.argv)
command = sys.argv[1]

print(command)
if command == "build":
	print("Build was specified")
	import utils
	utils.create_pages()

elif command == "new":
	print("New page was specified")
	import utils
	utils.create_pages()


else:
	print("Please specify ’build’ or ’new’")
