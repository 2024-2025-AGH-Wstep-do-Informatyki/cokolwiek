import math

def createDict():
    return {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

def createList():
    return ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def convSys(st, fin, num):
    try:
        num = str(num)
        st = int(st)
        fin = int(fin)
    except ValueError:
        return 'Wrong values'
    
    val = 0
    ret = ''
    
    num = num[::-1]
    
    dict = createDict()
    list = createList()
    
    power = 0
    for d in num:
        val += dict[d] * pow(st, power)
        power += 1
    
    power = pow(fin, int(math.log(val,fin)))
    
    while (power > 0):
        i = int(val/power)
        val -= i * power
        ret += list[i]
        power /= fin
        power = int(power)
    if (val > 0 ):
        ret += list[int(val)]
    return ret
