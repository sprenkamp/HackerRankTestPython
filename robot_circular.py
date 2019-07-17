N = 0
E = 1
S = 2
W = 3

def isCircular(path): 

    x = 0
    y = 0
    dir = N 
    for i in range(len(path)): 
        
        move = path[i] 

        if move == 'R': 
            dir = (dir + 1)%4
        elif move == 'L': 
            dir = (4 + dir - 1)%4
        else: 
            if dir == N: 
                y += 1
            elif dir == E: 
                x += 1
            elif dir == S: 
                y -= 1
            else: 
                x -= 1
    return (x == 0 and y == 0)

def solution(commands):
    list_result = []
    for i in commands:
        if(isCircular(i)):
            list_result.append('YES')
        else:
            if len(i)>1 and i[0] == i[-2]:
                list_result.append('YES')
            else:
                list_result.append('NO')
    return list_result

# Driver program 
path = ["GGGGR",'RGL']

print(solution(path))