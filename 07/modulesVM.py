import re
import os 

C_ARITHMETIC = "C_ARITHMETIC"
C_PUSH = "C_PUSH"
C_POP = "C_POP"
C_LABEL = "C_LABEL"
C_GOTO = "C_GOTO"
C_IF = "C_IF"
C_FUNCTION = "C_FUNCTION"
C_RETURN = "C_RETURN"
C_CALL = "C_CALL"

class Command:
	def __init__(self,type,arg1='',arg2='',filename='',):
		self.type=type
		self.arg1=arg1
		self.arg2=arg2
		self.filename=filename
	

class Call_Command(Command):
		def __init__(self,type,arg1='',arg2='',function_name='',call_counter = 0):
			super().__init__(type,arg1,arg2)
			self.function_name = function_name
			self.call_counter = call_counter
		
		

class Parser:
	def __init__(self):
		self.commands = []
		
	def parse(self, filename):
		function_name = "null"
		call_counter = 0
		with open(filename) as f:
			for i, line in enumerate(f):
				line = line.strip()
				if  not line or (len(line) > 0 and line[0] == '/'):
					continue
				#if re.match('//', line):
				if line.find('//') != -1:
					line = line.split("//")[0].strip()
					#print(line.split("//"))
				line = re.sub(r'[ ]+',' ',line)	
				#print(line)
				command = line.split(" ")
				if command[0] == "add" or command[0] == "sub" or command[0] == "and" or command[0] == "or" or command[0] == "neg" or command[0] == "eq" or command[0] == "gt" or command[0] == "lt" or command[0] == "not":
					self.commands.append(Command(C_ARITHMETIC,command[0]))
				elif command[0] == "push":
					self.commands.append(Command(C_PUSH,command[1],command[2],filename))
				elif command[0] == "pop":
					self.commands.append(Command(C_POP,command[1],command[2],filename))
				elif command[0] == "label":
					self.commands.append(Command(C_LABEL,command[1], function_name))
				elif command[0] == "if-goto":
					self.commands.append(Command(C_IF,command[1],function_name))
				elif command[0] == "goto":
					self.commands.append(Command(C_GOTO,command[1],function_name))
				elif command[0] == "function":
					self.commands.append(Command(C_FUNCTION,command[1],command[2]))
					function_name = command[1]
					call_counter = 0
				elif command[0] == "return":
					self.commands.append(Command(C_RETURN))
				elif command[0] == "call":
					self.commands.append(Call_Command(C_CALL,command[1],command[2],function_name,call_counter))
					call_counter += 1
					
	def getCommands(self):
		return self.commands
		

class Compiler:
	def compile(self, name, commands):
		if os.path.isfile(name):
			name = name[0: len(name) - 3]
		with open(name + '.asm', 'w') as the_file:
			label_counter=-1
			the_file.write('@256'+'\n')
			the_file.write('D=A'+'\n')
			the_file.write('@SP'+'\n')
			the_file.write('M=D'+'\n')
			the_file.write('@Sys.init'+'\n')
			the_file.write('0;JMP'+'\n')
			
			for command in commands:
				if command.type == C_ARITHMETIC:
					if command.arg1 == "add" or command.arg1 == "sub"  or command.arg1 == "eq"  or command.arg1 == "gt"  or command.arg1 == "lt"  or command.arg1 == "and"  or command.arg1 == "or":
						the_file.write('@2'+'\n')
						the_file.write('D=A'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('A=M-D'+'\n')
						the_file.write('D=M'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('A=M-1'+'\n')
						
						if command.arg1 == "eq" or command.arg1 == "gt" or command.arg1 == "lt":
							label_counter = label_counter + 1
							the_file.write('D=D-M'+'\n')
							the_file.write('@TRUE'+str(label_counter)+'\n')
							
						if command.arg1 == "add":
							the_file.write('D=D+M'+'\n')
						elif command.arg1 == "sub":
							the_file.write('D=D-M'+'\n')
						elif command.arg1 == "eq":
							the_file.write('D;JEQ'+'\n')
						elif command.arg1 == "gt":
							the_file.write('D;JGT'+'\n')
						elif command.arg1 == "lt":
							the_file.write('D;JLT'+'\n')
						elif command.arg1 == "and":
							the_file.write('D=D&M'+'\n')
						elif command.arg1 == "or":
							the_file.write('D=D|M'+'\n')
						
						if command.arg1 == "eq" or command.arg1 == "gt" or command.arg1 == "lt":
							the_file.write('@FALSE'+str(label_counter)+'\n')
							the_file.write('0;JMP'+'\n')
							the_file.write('(TRUE'+str(label_counter)+')'+'\n')
							the_file.write('D=-1'+'\n')
							the_file.write('@END'+str(label_counter)+'\n')
							the_file.write('0;JMP'+'\n')
							the_file.write('(FALSE'+str(label_counter)+')'+'\n')
							the_file.write('D=0'+'\n')
							the_file.write('@END'+str(label_counter)+'\n')
							the_file.write('0;JMP'+'\n')
							the_file.write('(END'+str(label_counter)+')'+'\n')
						
						the_file.write('@SP'+'\n')
						the_file.write('M=M-1'+'\n')
						the_file.write('A=M-1'+'\n')
						the_file.write('M=D'+'\n')
						
					else:
						the_file.write('@SP'+'\n')
						the_file.write('A=M-1'+'\n')
						if command.arg1 == "neg":
							the_file.write('D=-M'+'\n')
						if command.arg1 == "not":
							the_file.write('D=!M'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('A=M-1'+'\n')
						the_file.write('M=D'+'\n')
						
				elif command.type == C_PUSH:
					if command.arg1 == 'constant':
						the_file.write('@' + command.arg2 +'\n')
						the_file.write('D=A'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('A=M'+'\n')
						the_file.write('M=D'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('M=M+1'+'\n')
					elif command.arg1 == 'local' or command.arg1 == "argument" or command.arg1 == "this" or command.arg1 == "that" or command.arg1 == "temp" or command.arg1 == "static":
						if command.arg1 != 'static':
							the_file.write('@' + command.arg2 +'\n')
							the_file.write('D=A'+'\n')
						if command.arg1 == 'local': 
							the_file.write('@LCL' +'\n')
						elif command.arg1 == 'argument': 
							the_file.write('@ARG' +'\n')
						elif command.arg1 == 'this': 
							the_file.write('@THIS' +'\n')
						elif command.arg1 == 'that': 
							the_file.write('@THAT' +'\n')
						elif command.arg1 == 'temp': 
							the_file.write('@5' +'\n')	
						
						if command.arg1 == 'temp':
							the_file.write('A=D+A'+'\n')
						elif command.arg1 == 'static':
							the_file.write('@'+os.path.basename(command.filename[0: len(command.filename) - 3])+ '.' + command.arg2 +'\n')
						else:
							the_file.write('A=M+D'+'\n')
						
						the_file.write('D=M' +'\n')
						the_file.write('@SP' +'\n')
						the_file.write('A=M'+'\n')
						the_file.write('M=D' +'\n')
						the_file.write('@SP'+'\n')
						the_file.write('M=M+1'+'\n')
					elif command.arg1 == 'pointer':
						if int(command.arg2) == 0: 
							the_file.write('@THIS' +'\n')
						elif int(command.arg2) == 1: 
							the_file.write('@THAT' +'\n')
						the_file.write('D=M'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('A=M'+'\n')
						the_file.write('M=D'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('M=M+1'+'\n')
						 
						
				elif command.type == C_POP:
					if command.arg1 == 'local' or command.arg1 == "argument" or command.arg1 == "this" or command.arg1 == "that" or command.arg1 == "temp" or command.arg1 == "static":
						if command.arg1 != 'static':
							the_file.write('@' + command.arg2 +'\n')
							the_file.write('D=A'+'\n')
						if command.arg1 == 'local': 
							the_file.write('@LCL' +'\n')
						elif command.arg1 == 'argument': 
							the_file.write('@ARG' +'\n')
						elif command.arg1 == 'this': 
							the_file.write('@THIS' +'\n')
						elif command.arg1 == 'that': 
							the_file.write('@THAT' +'\n')
						elif command.arg1 == 'temp': 
							the_file.write('@5' +'\n')	
							
						if command.arg1 == 'temp':
							the_file.write('D=D+A'+'\n')
						elif command.arg1 == 'static':
							the_file.write('@'+os.path.basename(command.filename[0: len(command.filename) - 3])+ '.' + command.arg2 +'\n')
							the_file.write('D=A'+'\n')
						else:
							the_file.write('D=M+D'+'\n')
							
						the_file.write('@R13'+'\n')
						the_file.write('M=D'+'\n')
						the_file.write('@SP'+'\n')
						the_file.write('M=M-1'+'\n')
						the_file.write('A=M'+'\n')
						the_file.write('D=M'+'\n')
						the_file.write('@R13'+'\n')
						the_file.write('A=M'+'\n')
						the_file.write('M=D'+'\n')
						
					elif command.arg1 == 'pointer':
						the_file.write('@SP'+'\n')
						the_file.write('M=M-1'+'\n')
						the_file.write('A=M'+'\n')
						the_file.write('D=M'+'\n')
						if int(command.arg2) == 0: 
							the_file.write('@THIS' +'\n')
						elif int(command.arg2) == 1: 
							the_file.write('@THAT' +'\n')
						the_file.write('M=D'+'\n')
						
				elif command.type == C_LABEL:
					the_file.write('('+command.arg2+'_'+command.arg1+')\n')
				elif command.type == C_GOTO:
					the_file.write('@'+command.arg2+'_'+command.arg1+'\n')
					the_file.write('0;JMP'+'\n')
					
				elif command.type == C_IF:
					the_file.write('@SP'+'\n')
					the_file.write('M=M-1'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@'+command.arg2+'_'+command.arg1+'\n')
					the_file.write('D;JNE'+'\n')
					
				elif command.type == C_FUNCTION:
					the_file.write('('+command.arg1+')\n')
					the_file.write('@0'+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@R13'+'\n')
					the_file.write('M=D'+'\n')
					the_file.write('(function$'+command.arg1+'$LOCAL$LOOP)\n')
					the_file.write('@'+command.arg2+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@R13'+'\n')
					the_file.write('D=D-M'+'\n')
					the_file.write('@function$'+command.arg1+'$LOCAL$LOOP$END\n')
					the_file.write('D;JEQ'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('M=0'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('M=M+1'+'\n')
					the_file.write('@R13'+'\n')
					the_file.write('M=M+1'+'\n')
					the_file.write('@function$'+command.arg1+'$LOCAL$LOOP\n')
					the_file.write('0;JMP'+'\n')
					the_file.write('(function$'+command.arg1+'$LOCAL$LOOP$END)\n')
					
				elif command.type == C_RETURN:
					the_file.write('@LCL'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@FRAME'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@5'+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@FRAME'+'\n')
					the_file.write('A=M-D'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@RET'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@SP'+'\n')
					the_file.write('A=M-1'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@ARG'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@ARG'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('M=D+1'+'\n')
					
					
					the_file.write('@1'+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@FRAME'+'\n')
					the_file.write('A=M-D'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@THAT'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@2'+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@FRAME'+'\n')
					the_file.write('A=M-D'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@THIS'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@3'+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@FRAME'+'\n')
					the_file.write('A=M-D'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@ARG'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@4'+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@FRAME'+'\n')
					the_file.write('A=M-D'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@LCL'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@RET'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('0;JMP'+'\n')
				elif command.type == C_CALL:
					the_file.write('@'+command.function_name+'_'+command.arg1+'_'+str(command.call_counter)+'\n')
					the_file.write('D=A'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('M=D'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('M=M+1'+'\n')
					
					the_file.write('@LCL\n')
					the_file.write('D=M'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('M=D'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('M=M+1'+'\n')
					
					the_file.write('@ARG\n')
					the_file.write('D=M'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('M=D'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('M=M+1'+'\n')
					
					the_file.write('@THIS\n')
					the_file.write('D=M'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('M=D'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('M=M+1'+'\n')
					
					the_file.write('@THAT\n')
					the_file.write('D=M'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('A=M'+'\n')
					the_file.write('M=D'+'\n')
					the_file.write('@SP'+'\n')
					the_file.write('M=M+1'+'\n')
					
					the_file.write('@'+str(int(command.arg2)+5)+'\n')
					the_file.write('D=A\n')
					the_file.write('@SP\n')
					the_file.write('D=M-D\n')
					the_file.write('@ARG\n')
					the_file.write('M=D\n')
					
					the_file.write('@SP'+'\n')
					the_file.write('D=M'+'\n')
					the_file.write('@LCL'+'\n')
					the_file.write('M=D'+'\n')
					
					the_file.write('@'+command.arg1+'\n')
					the_file.write('0;JMP'+'\n')
					
					the_file.write('('+command.function_name+'_'+command.arg1+'_'+str(command.call_counter)+')\n')
						
			