import re
        
def prioridade(a, b):
    if a == "(" or a == ")": a = 5
    elif a == "/": a = 4;
    elif a == "*": a = 3
    elif a == "-": a = 2
    else: a = 1
    if b == "(" or b == ")": b = 5
    elif b == "/": b = 4
    elif b == "*": b = 3
    elif b == "-": b = 2
    else: b = 1
    if (a > b):
        return True
    else:
        return False

def exp_lista(exp):
    l = re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", exp)
    for i, v in enumerate(l):
        if v == " ":
            del(l[i])
    return l

def TraduzPosFixa(l):
    pilha = []
    pf = []
    operadores = ["+","-", "*", "/", "(", ")"]
    for v in l:
        if v not in operadores:
            pf.append(v)
        elif len(pilha) == 0:
            pilha.append(v)
        elif prioridade(pilha[-1], v) == True and pilha[-1] != "(" and pilha[-1] != ")":
            pf.append(pilha.pop())
            pilha.append(v)
        elif v == ")":
            v_p = pilha[-1]
            while v_p != "(":
                if pilha[-1] != ")":
                    pf.append(pilha.pop())
                else:
                    pilha.pop()
                v_p = pilha[-1]
            pilha.pop()
        else:
            pilha.append(v)
    for i in range(len(pilha)):
        if pilha[-(i + 1)] not in ["(", ")"]:
            pf.append(pilha[-(i + 1)])
    return(pf)
    
def CalcPosFixa(listaexp):
    operadores = ["+", "-", "*", "/"]
    l = []
    for v in listaexp:
        if v not in operadores:
            l.append(v)
        else:
            if v == "+":
                l[-2] = float(l[-2]) + float(l[-1])
            elif v == "-":
                l[-2] = float(l[-2]) - float(l[-1])
            elif v == "*":
                l[-2] = float(l[-2]) * float(l[-1])
            else:
                l[-2] = float(l[-2]) / float(l[-1])
            l.pop()
    return l[0]
    
def main():
    exp = 0
    while exp != "fim":
        exp = input(">>>")
        tr = TraduzPosFixa(exp_lista(exp))
        res = CalcPosFixa(tr)
        print(res)
main()
        
    
            
