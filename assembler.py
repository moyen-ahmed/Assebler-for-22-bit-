def convertBinToHex(bin):
    hex = " "
    if bin == "0000":
        hex = "0"
    elif bin == "0001":
        hex = "1"
    elif bin == "0010":
        hex = "2"
    elif bin == "0011":
        hex = "3"
    elif bin == "0100":
        hex = "4"
    elif bin == "0101":
        hex = "5"
    elif bin == "0110":
        hex = "6"
    elif bin == "0111":
        hex = "7"
    elif bin == "1000":
        hex = "8"
    elif bin == "1001":
        hex = "9"
    elif bin == "1010":
        hex = "A"
    elif bin == "1011":
        hex = "B"
    elif bin == "1100":
        hex = "C"
    elif bin == "1101":
        hex = "D"
    elif bin == "1110":
        hex = "E"
    elif bin == "1111":
        hex = "F"
    return hex

# Check instruction type for your project
def checkInstruction(inst):
    convertInstruction = " "
    if inst == "addi":
        convertInstruction = "0010"
    elif inst == "beq":
        convertInstruction = "0100"
    elif inst == "bne":
        convertInstruction = "0101"
    elif inst == "lw":
        convertInstruction = "0110"
    elif inst == "sw":
        convertInstruction = "0111"
    elif inst == "jmp":
        convertInstruction = "1110"
    else:
        convertInstruction = "Invalid instructions"
    return convertInstruction

# Check R-type function
def checkFunction(func):
    convertInstruction = " "
    if func == "add":
        convertInstruction = "0000"
    elif func == "sub":
        convertInstruction = "0001"
    elif func == "and":
        convertInstruction = "0010"
    elif func == "or":
        convertInstruction = "0011"
    elif func == "nor":
        convertInstruction = "0100"
    elif func == "sll":
        convertInstruction = "0101"
    elif func == "srl":
        convertInstruction = "0110"
    elif func == "slt":
        convertInstruction = "0111"
    elif func == "nop":
        convertInstruction = "0000"
    else:
        convertInstruction = "Invalid instructions"
    return convertInstruction

# Check register mapping
def checkRegister(reg):
    convertReg = ""
    if reg == "$t0":
        convertReg = "0000"
    elif reg == "$t1":
        convertReg = "0001"
    elif reg == "$t2":
        convertReg = "0010"
    elif reg == "$t3":
        convertReg = "0011"
    elif reg == "$t4":
        convertReg = "0100"
    elif reg == "$t5":
        convertReg = "0101"
    elif reg == "$t6":
        convertReg = "0110"
    elif reg == "$t7":
        convertReg = "0111"
    elif reg == "$t8":
        convertReg = "1000"
    elif reg == "$t9":
        convertReg = "1001"
    elif reg == "$t10":
        convertReg = "1010"
    elif reg == "$t11":
        convertReg = "1011"
    elif reg == "$t12":
        convertReg = "1100"
    elif reg == "$t13":
        convertReg = "1101"
    elif reg == "$t14":
        convertReg = "1110"
    elif reg == "$t15":
        convertReg = "1111"
    else:
        convertReg = "Invalid Register"
    return convertReg

# Decimal to binary conversion for various bit lengths
def decimalToBinary(num, bits=4):
    if num < 0:
        num = (1 << bits) + num
    return f"{num:0{bits}b}"

# Read and process input file
readf = open("inputs", "r")
writef = open("outputs", "w")
writef.write("v2.0 raw\n")

for i in readf:
    splitted = i.split()

    # For R-type instruction
    if splitted[0] in ["add", "sub", "and", "or", "nor", "sll", "srl", "slt", "nop"]:
        conv_func = convertBinToHex(checkFunction(splitted[0]))
        conv_rd = convertBinToHex(checkRegister(splitted[1]))
        conv_rs = convertBinToHex(checkRegister(splitted[2]))
        conv_rt = convertBinToHex(checkRegister(splitted[3]))
        shamt = "00"  # Fixed 2-bit shift amount

        out = "0" + conv_rs + conv_rt + conv_rd + shamt + conv_func
        print(out)
        writef.write(out + "\n")

    # For I-type instruction
    elif splitted[0] in ["addi", "beq", "bne", "lw", "sw"]:
        conv_inst = convertBinToHex(checkInstruction(splitted[0]))
        conv_rt = convertBinToHex(checkRegister(splitted[1]))
        conv_rs = convertBinToHex(checkRegister(splitted[2]))
        conv_im = convertBinToHex(decimalToBinary(int(splitted[3]), 10))

        out = conv_inst + conv_rs + conv_rt + conv_im
        print(out)
        writef.write(out + "\n")

    # For J-type instruction
    elif splitted[0] == "jmp":
        conv_inst = convertBinToHex(checkInstruction(splitted[0]))
        conv_target = decimalToBinary(int(splitted[1]), 18)
        out = conv_inst + conv_target
        print(out)
        writef.write(out + "\n")

readf.close()
writef.close()
