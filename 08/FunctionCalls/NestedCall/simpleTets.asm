@256
D=A
@SP
M=D
@Sys.init
0;JMP
(Sys.init)
@0
D=A
@R13
M=D
(function$Sys.init$LOCAL$LOOP)
@0
D=A
@R13
D=D-M
@function$Sys.init$LOCAL$LOOP$END
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@R13
M=M+1
@function$Sys.init$LOCAL$LOOP
0;JMP
(function$Sys.init$LOCAL$LOOP$END)
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@THIS
M=D
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@THAT
M=D
@Sys.init_Sys.main_0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@5
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.main
0;JMP
(Sys.init_Sys.main_0)
@1
D=A
@5
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
(Sys.init_LOOP)
@Sys.init_LOOP
0;JMP
(Sys.main)
@0
D=A
@R13
M=D
(function$Sys.main$LOCAL$LOOP)
@5
D=A
@R13
D=D-M
@function$Sys.main$LOCAL$LOOP$END
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@R13
M=M+1
@function$Sys.main$LOCAL$LOOP
0;JMP
(function$Sys.main$LOCAL$LOOP$END)
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@THIS
M=D
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
M=M-1
A=M
D=M
@THAT
M=D
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
@300
D=A
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M-D
D=M
@SP
A=M-1
D=D+M
@SP
M=M-1
A=M-1
M=D
@LCL
D=M
@FRAME
M=D
@5
D=A
@FRAME
A=M-D
D=M
@RET
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M
@SP
M=D+1
@1
D=A
@FRAME
A=M-D
D=M
@THAT
M=D
@2
D=A
@FRAME
A=M-D
D=M
@THIS
M=D
@3
D=A
@FRAME
A=M-D
D=M
@ARG
M=D
@4
D=A
@FRAME
A=M-D
D=M
@LCL
M=D
@RET
A=M
0;JMP