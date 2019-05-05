import sys
import modulesVM
from os import path, listdir


if __name__ == "__main__":
	parser = modulesVM.Parser()
	if path.isdir(sys.argv[1]):
		for file in listdir(sys.argv[1]):
			if file.endswith(".vm"):
				 #print(path.join(sys.argv[1], file))
				 parser.parse(path.join(sys.argv[1], file))
	else:
		parser.parse(sys.argv[1])
	compiler = modulesVM.Compiler()
	compiler.compile(sys.argv[1],parser.getCommands())
	#parser.print()