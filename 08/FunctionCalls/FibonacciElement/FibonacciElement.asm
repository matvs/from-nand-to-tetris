@261
D=A
@SP
M=D
@Sys.init
0;JMP
(Main.fibonacci)
@0
D=A
@R13
M=D
(function$Main.fibonacci$LOCAL$LOOP)
@0
D=A
@R13
D=D-M
@function$Main.fibonacci$LOCAL$LOOP$END
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@R13
M=M+1
@function$Main.fibonacci$LOCAL$LOOP
0;JMP
(function$Main.fibonacci$LOCAL$LOOP$END)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
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
D=D-M
@TRUE0
D;JLT
@FALSE0
0;JMP
(TRUE0)
D=-1
@END0
0;JMP
(FALSE0)
D=0
@END0
0;JMP
(END0)
@SP
M=M-1
A=M-1
M=D
@SP
M=M-1
A=M
D=M
@Main.fibonacci_IF_TRUE
D;JNE
@Main.fibonacci_IF_FALSE
0;JMP
(Main.fibonacci_IF_TRUE)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
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
(Main.fibonacci_IF_FALSE)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
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
D=D-M
@SP
M=M-1
A=M-1
M=D
@Main.fibonacci_Main.fibonacci_0
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci_Main.fibonacci_0)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
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
D=D-M
@SP
M=M-1
A=M-1
M=D
@Main.fibonacci_Main.fibonacci_1
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci_Main.fibonacci_1)
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
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init_Main.fibonacci_0
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
@6
D=A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Sys.init_Main.fibonacci_0)
(Sys.init_WHILE)
@Sys.init_WHILE
0;JMP
