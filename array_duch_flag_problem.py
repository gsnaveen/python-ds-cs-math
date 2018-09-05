instr = '001121211002'

instr = list(instr)
mylen = len(instr)
midPointer = 0 
index = 0
runner = 0
while  index < mylen and runner <  mylen:
    
    if instr[index] == "0":
        instr.insert(0,instr.pop(index))
        index += 1
    elif instr[index] == "1":
        index += 1
    elif instr[index] == "2":
        instr.append(instr.pop(index))
        
    runner += 1

print("".join(instr))
