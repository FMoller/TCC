"""
To help write minterms expressions
"""

def product_(line,inps):
    b_line = bin(line)[2:]
    n_inps = inps - b_line
    exp = ""
    for i in range(n_inps):
        exp = exp + "~i"+str(inps-1-i)+'*'
    for i in range(len(b_line)):
        if b_line[i] == '0':
            exp += "~i"
        else:
            exp += "i"
        exp += str(inps-1-n_inps-i)+'*'
    return exp[:-1]
    
    
