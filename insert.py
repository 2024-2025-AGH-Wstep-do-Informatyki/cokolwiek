def number(i):
    global l
    if i + 1 < len(equation) and '0' <= equation[i + 1] <= '9':
        l += 1
        return equation[i]+number(i+1)
    else:
        return equation[i]

equation = input()
stack=[]
onp = []
i = 0
l = 0
ws = 0
dzialania = {'+','-','*','/','^'}

while i<len(equation):
    if equation[i] >= '0' and equation[i] <= '9': #cyfra
        l = 0
        onp.append(int(number(i)))
        i += l
    elif equation[i] == '+' or equation[i] == '-': #dodawanie odejmowanie
        while ws and stack[ws - 1] != '(':
            ws -=1
            onp.append(stack[ws])
            stack.pop(ws)
        stack.append(equation[i])
        ws +=1
    elif equation[i] == '*' or equation[i] == '/': #mnożenie dzielenie
        while ws and stack[ws - 1] != '(' and stack[ws - 1] != '+' and stack[ws - 1] != '-':
            ws -=1
            onp.append(stack[ws])
            stack.pop(ws)
        stack.append(equation[i])
        ws +=1
    elif equation[i] == '^': #potęgowanie
        while ws and stack[ws - 1] == '^':
            ws -=1
            onp.append(stack[ws])
            stack.pop(ws)
        stack.append(equation[i])
        ws +=1
    elif equation[i] == '(': #początek nawiasu
        stack.append(equation[i])
        ws +=1
    elif equation[i] == ')': #koniec nawiasu
        while stack[ws - 1] != '(':
            ws -=1
            onp.append(stack[ws])
            stack.pop(ws)
        ws -= 1
        stack.pop(ws)
    i+=1
while ws:
    ws -= 1
    onp.append(stack[ws])
    stack.pop(ws)
print(onp)
wynik = 0
i = 0
while len(onp) > 1:
    if onp[i] in dzialania:
        if onp[i] =='+':
            onp[i-2]+=onp[i-1]
        elif onp[i] =='-':
            onp[i-2]-=onp[i-1]
        elif onp[i] =='*':
            onp[i-2]*=onp[i-1]
        elif onp[i] =='/':
            onp[i-2]/=onp[i-1]
        onp.pop(i)
        onp.pop(i - 1)
        i-=2

    i+=1
print(onp)