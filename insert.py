equation = input()
stack=[]
onp = []
i = 0
l = 0
ws = 0

def number(i):
    global l
    if i + 1 < len(equation) and '0' <= equation[i + 1] <= '9':
        l += 1
        return equation[i]+number(i+1)
    else:
        return equation[i]

while i<len(equation):
    if equation[i] >= '0' and equation[i] <= '9': #cyfra
        l = 0
        onp.append(number(i))
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