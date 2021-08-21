"""
To help write minterms expressions
"""


def m_product(pro):
    exp = ""
    for i in range(len(pro)):
        exp += pro[len(pro)-1-i]
        if i != len(pro)-1:
            exp+='*'
    return exp


def product(line,inps):
    b_line = bin(line)[2:]
    n_inps = inps - len(b_line)
    exp = []
    for i in range(n_inps):
        exp.append("~i"+str(inps-1-i))
    for i in range(len(b_line)):
        if b_line[i] == '0':
            b_exp = "~i"
        else:
            b_exp = "i"
        b_exp += str(inps-1-n_inps-i)
        exp.append(b_exp)
    return m_product(exp)

def expression(lines,inps):
    exp = ""
    for i in lines:
        exp+=product(i,inps)+"+"
    return exp[:-1]
