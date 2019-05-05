import sys
import parserHack


if __name__ == "__main__":
	parser = parserHack.Parser(sys.argv[1])
	parser.parse()
	#parser.print()