def solution(A):
    machine_stack = []
    l ="".join(A.rstrip())
    strArr = l.split(" ") 
    for i in strArr:
        if i.isnumeric():
            machine_stack.append(i)
        elif i == 'DUP':
            if len(machine_stack)>0:
                a = machine_stack.pop()
                machine_stack.append(a)
                machine_stack.append(a)
            else:
                return -1
        elif i == 'POP':
            if len(machine_stack)>0:
                machine_stack.pop()
            else:
                return -1
        elif i == '+':
            if len(machine_stack)<2:
                return -1
            else:
                a = int(machine_stack.pop())
                b = int(machine_stack.pop())
                c = a + b
                machine_stack.append(c)            
        elif i == '-':
            if len(machine_stack)<2:
                return -1
            else:
                a = int(machine_stack.pop())
                b = int(machine_stack.pop())
                c = a - b
                if c < 0:
                    return -1
                else:
                    machine_stack.append(c)
    result = machine_stack.pop()
    return result

A =  '13 DUP 4 POP 5 DUP + DUP + -'
B = '5 6 + -'
C = 'DUP 4 - -'
print(solution(C))