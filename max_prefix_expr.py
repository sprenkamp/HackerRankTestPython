def max_result_expression(expression, variables):
    
    l ="".join(expression.rstrip())
    strArr = l.split(" ")    
    num = []
    if len(variables) == 0:
        num = find_result(strArr)                
        result = num.pop()                     
    else:
        find_max=[]
        for n, i in enumerate(strArr):
            if i == 'x':             
                a = variables['x']                
                x=[]
                for i in reversed(a):
                    x.append(i)
                x1 = x.pop()
                x2 = x.pop()
                for i in range(x1,x2):                        
                    strArr[n] = i
                    if 'y' in strArr:
                        for m, j in enumerate(strArr):
                            if j == 'y':             
                                b = variables['y']
                                
                                y=[]
                                for k in reversed(b):
                                    y.append(k)
                                y1 = y.pop()
                                y2 = y.pop()
                                for i in range(y1,y2):
                                    strArr[m] = i
                                    num = find_result(strArr)
                                    find_max.append(num.pop())
                    else:
                        num = find_result(strArr)                        
                        find_max.append(num.pop())            
        result = max(find_max)    
    return result

def find_result(strArr):
    num =[]
    print(strArr)
    for i in reversed(strArr):       
        if i == '+':               
            sum(num)
        elif i == '-':               
            diff(num)
        elif i == '*':               
            mul(num)
        elif i == '/':                
            div(num)
        elif i == '%':
            remain(num)
        else:
            num.append(i)
    return num

def sum(num):
    a =  int(num.pop())
    b = int(num.pop())
    c = a + b
    num.append(c)
    return num

def diff(num):
    a =  int(num.pop())
    b = int(num.pop())
    c = a - b
    num.append(c)
    return num

def div(num):
    a =  int(num.pop())
    b = int(num.pop())
    c = a / b
    num.append(c)
    return num

def mul(num):
    a =  int(num.pop())
    b = int(num.pop())
    c = a * b
    num.append(c)
    return num

def remain(num):
    a =  int(num.pop())
    b = int(num.pop())
    c = a % b
    num.append(c)
    return num

expr = "+ 6 * - 4 + 2 3 8"  #-2 output
e = "* + 2 x y" # 9
var = { "x": (0, 2), "y": (2, 4) }
print(expr)
print(max_result_expression(expr, {}))