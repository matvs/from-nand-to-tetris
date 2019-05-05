import re

A_COMMAND = "A_COMMAND"
C_COMMAND = "C_COMMAND"
L_COMMAND = "L_COMMAND"

symbols = {
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R1O': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD': 24576,
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4
}

JUMP_CODES={
	'' : '000',
	'JGT' : '001',
	'JEQ' : '010',
	'JGE' : '011',
	'JLT' : '100',
	'JNE' : '101',
	'JLE' : '110',
	'JMP' : '111',
}

DEST_CODES={
	'' : '000',
	'M' : '001',
	'D' : '010',
	'MD' : '011',
	'A' : '100',
	'AM' : '101',
	'AD' : '110',
	'AMD' : '111',
}

COMP_CODES={
	'0': '0101010',
	"1"     : "0111111",
    "-1"    : "0111010",
	"D"     : "0001100",
        "A"     : "0110000",
        "M"     : "1110000",
        "!D"    : "0001101",
        "!A"    : "0110001",
        "!M"    : "1110001",
        "-D"    : "0001111",
        "-A"    : "0110011",
        "-M"    : "1110011",
        "D+1"   : "0011111",
        "A+1"   : "0110111",
        "M+1"   : "1110111",
        "D-1"   : "0001110",
        "A-1"   : "0110010",
        "M-1"   : "1110010",
        "D+A"   : "0000010",
        "D+M"   : "1000010",
        "D-A"   : "0010011",
        "D-M"   : "1010011",
        "A-D"   : "0000111",
        "M-D"   : "1000111",
        "D&A"   : "0000000",
        "D&M"   : "1000000",
        "D|A"   : "0010101",
        "D|M"   : "1010101",
	
}

class Parser:
	def __init__(self,filename):
		self.filename=filename
		self.commands=[]
		self.next_address = 16
		
	def createCommands(self):
		with open(self.filename + '.asm') as f:
			for i, line in enumerate(f):
				line = line.strip()
				type = C_COMMAND
				if  not line or (len(line) > 0 and line[0] == '/'):
					continue
				elif line[0] == '@':
					type=A_COMMAND
					self.commands.append(Command(type,line[1:len(line)]))
				elif line[0] == '(':
					type= L_COMMAND
					self.commands.append(Command(type,line[1:(len(line) - 1)]))
				else:
					dest = comp = jmp = ''
					pos = line.find("=")
					if pos != -1:
						data = line.split("=")
						dest = data[0].strip()
						line = data[1].strip()
					pos = line.find(";")
					if pos != -1:
						data = line.split(";")
						line = data[0].strip()
						jmp = data[1].strip()
					comp = line.strip()
					comp = comp.replace(" ","")
					dest = dest.replace(" ","")
					jmp = jmp.replace(" ","")
					self.commands.append(Command(type,'',dest,comp,jmp))
		return self
	
	def labelsToAddress(self):
		#for command in self.commands:
			#if command.type == L_COMMAND:
				#commands = self.commands[:]
				#for command2 in commands:
					#if command2.type == L_COMMAND and command2.symbol != command.symbol:
						#commands.remove(command2)
				#for i,command2 in enumerate(commands):
					#if command2.type == L_COMMAND:
						#symbols[command.symbol] = i
						#print(command.symbol +" "+str(i))
		line_number=0
		for command in self.commands:
			if command.type == L_COMMAND:
				symbols[command.symbol] = line_number
				#print(command.symbol + " " + str(line_number))
			else:
				line_number = line_number + 1
						
			
		return self
	
	def symbolsToNumbers(self):
		for i,command in enumerate(self.commands):
			if command.type == A_COMMAND:
				if not re.match('^[0-9]+$', command.symbol):
					if command.symbol not in symbols:
						#print(command.symbol)
						symbols[command.symbol] = self.next_address
						command.symbol = self.next_address
						self.next_address = self.next_address + 1
					else:
						command.symbol = symbols[command.symbol]
				
	def generateMachineCode(self):
		with open(self.filename + '.hack', 'w') as the_file:
			for command in self.commands:
				if command.type == A_COMMAND:
					the_file.write('0' + self.convertToBin(command.symbol)+'\n')
				elif command.type == C_COMMAND:
					the_file.write('111' +COMP_CODES[command.comp]+ DEST_CODES[command.dest]+ JUMP_CODES[command.jmp]+'\n')
		
	def parse(self):
		self.createCommands().labelsToAddress().symbolsToNumbers()
		self.generateMachineCode()
		
	def convertToBin(self,n):
		binary = bin(int(n))[2:]
		length = 15 - len(binary)
		for i in range(0,length):
			binary = '0' + binary
		return binary
			
				
		
			
						
	def print(self):
		for command in self.commands:
			command.print()
				
			
	
class Command:
	def __init__(self,type,symbol='',dest='',comp='',jmp=''):
		self.type=type
		self.symbol=symbol
		self.dest=dest
		self.comp=comp
		self.jmp=jmp
	def print(self):
		print(self.type + " symbol " + str(self.symbol) + " dest " + str(self.dest) + " comp " + str(self.comp) + " jump " + str(self.jmp))

