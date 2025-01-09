def calc(onp):
    i = 0
    operators = {'+','-','*','/','^'}
    while len(onp) > 1:
        match onp[i]:
            case '+':
                onp[i - 2] += onp[i - 1]
            case '-':
                onp[i - 2] -= onp[i - 1]
            case '*':
                onp[i - 2] *= onp[i - 1]
            case '/':
                onp[i - 2] /= onp[i - 1]
            case '^':
                onp[i - 2] **= onp[i - 1]
            case _:
                onp[i] = int(onp[i])
        if onp[i] in operators:
            onp.pop(i)
            onp.pop(i - 1)
            i-=2
        i+=1
    return onp[0]