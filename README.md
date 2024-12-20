# Assebler-for-22-bit-





SW SLT SLL SUB JMP AND LW ADDi NOP NOR BEQ OR ADD BNE SRL
Introduction
Developing a custom Central Processing Unit (CPU) based on the Instruction Set Architecture (ISA) is a fundamental aspect of computer architecture. This project involves the design and implementation of a CPU capable of executing instructions stored in memory sequentially. The CPU's design is inspired by the IAS (Institute for Advanced Study) architecture, incorporating elements such as a datapath,control units, an Arithmetic Logic Unit (ALU), and both instruction and data memory.This project emphasizes a modular approach to CPU design, integrating components such as:
1.Register File: Stores intermediate data and results.
2.ALU: Performs arithmetic and logical operations.
3.Control Unit: Decodes instructions and generates control signals for execution.
4.Instruction and Data Memory: Holds the program and associated data.
The primary objective is to create a functional CPU capable of:
1.Fetching instructions from memory.
2.Decoding instructions into meaningful operations.
3.Executing operations based on the ISA-defined formats.
4.Writing results back to memory or registers.
The final deliverables for this project include:
A Logisim file showcasing the complete datapath design with all required components.
A Project Report containing: 
The control unit table.
ALU control table.
Detailed ISA documentation with descriptions of formats, operands, operations, and opcodes.
Now I describe ISA descriptions of formats, operands, operations, and opcodes.
ISA:
An Instruction Set Architecture (ISA) is part of the abstract model of a computer that defines how the CPU is controlled by the software. The ISA acts as an interface between the hardware and the software, specifying both what the processor is capable of doing as well as how it gets done.

The ISA has three types of instructions (R-type, I-type, and J-type), each with a specific operand structure:
R-Type: 3 operands (rs, rt, rd)
I-Type: 2 operands (rs, rt) + immediate value
J-Type: 1 operand (address)
Types of operands:

1.Register-based operands:
Most instructions (ADD, SUB, AND, OR, etc ) operate on registers (rs, rt, rd).
2.Memory-based operands:
Instructions like LW and SW involve memory (using a base register and offset)

Number of Operations:
Based on the instructions provided, assume we are working with 16 total operations:
Arithmetic: 3 operations (add, sub, addi).
Logical: 5 operations (and,or,nor,sll,srl).
Branch: 4 operations (beq, bne,jmp,,slt).
Memory: 2 operations (lw, sw).
Other: 1 operation (nop).


]



The ISA supports 15 operations based on the instructions given in the specified order:
Instruction	   Type	Work
SW	I	Store word in memory.
SLT	R	Set if less than.
SLL	R	Logical shift left.
SUB	R	Subtract two registers.
JMP	J	Jump to a specified address.
AND	R	Bitwise AND.
LW	I	Load word from memory.
ADDi	I	Add immediate value to a register.
NOP	R	No operation.
NOR	R	Bitwise NOR.
BEQ	I	Branch if two registers are equal.
OR	R	Bitwise OR.
ADD	R	Add two registers.
BNE	I	Branch if two registers are not equal.
SRL	R	Logical shift right.


Arithmetic Operations: (Opcode and Binary Value)
For R type:
Instruction	Type	Opcode(4 bits)	rs(4 bits)	rt(4 bits)	rd(4 bits)	Shamt(2)	Function(4)
ADD	R	0000	4	4	4	2	0000
SUB	R	0000	4	4	4	2	0001
AND	R	0000	4	4	4	2	0010
OR	R	0000	4	4	4	   2	0011
NOR	R	0000	4	4	4	2	0100
SLL	R	0000	4	4	4	2	0101
SRL	R	0000	4	4	4	2	0110
SLT	R	0000	4	4	4	2	    0111
NOP	R	......	4	4	4	2	           …………
		   I Type					
Instruction	Type	Opcode(4 bits)	rs(4 bits)	rt(4 bits)	Immediate(10)		
ADDi	I	0010	4	4	10		
BEQ	I	0100	4	4	10		
BNE	I	0101	4	4	10		
LW	I	0110	4	4	10		
SW	I	0111	4	4	10 		
			J tYPE				
Instruction	Type	Opcode(4 bits)	Adress(18 bits)
jmp	I	1110	


Control Unit
For better view we give xlsx file

	Name	Opcode	RegDst	ALUSrc	MemtoReg	RegWrite	MemRead	MemWrite	Jump	Branch	A Inv.	B Inv.	ALUOp1	ALUOp2	Shift	Store	Load	Cin	Cout	Function
I	SW	0111	0	1	X	0	0	1	0	0	0	0	0	0	0	1	0		0	0
R	SLT	0000	1	0	0	1	0	0	0	0	0	1	1	0	0	0	0		1	0111
R	SLL	0000	1	0	0	1	0	0	0	0	0	0	1	0	1	0	0		0	0101
R	SUB	0000	1	0	0	1	0	0	0	0	1	1	1	0	0	0	0	1	1	0001
J	JMP	1110	-	-	-	-	-	-	1	0	0	0	N/A	N/A	0	0	0		0	
R	AND	0000	1	0	0	1	0	0	0	0	0	0	1	0	0	0	0		0	0010
I	LW	0110	0	1	1	1	1	0	0	0	0	0	0	0	0	0	1		0	
I	ADDi	0010	0	1	0	1	0	0	0	0	0	0	0	0	0	0	0		1	
	NOP	0000	0	0	0	0	0	0	0	0	0	0	N/A	N/A	0	0	0		0	0100
R	NOR	0000	1	0	0	1	0	0	0	0	1	1	1	0	0	0	0		0	
I	BEQ	0100	0	0	X	0	0	0	0	1	0	1	0	1	0	0	0		1	
R	OR	0000	1	0	0	1	0	0	0	0	0	0	1	0	0	0	0		0	0011
R	ADD	0000	1	0	0	1	0	0	0	0	0	0	1	0	0	0	0		1	0000
I	BNE	0101	0	0	X	0	0	0	0	1	0	1	0	1	0	0	0		1	
R	SRL	0000	1	0	0	1	0	0	0	0	0	0	1	0	1	0	0		0	0110



















































































