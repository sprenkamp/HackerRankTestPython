def solution(N, S):
    available=0
    occupied=[]
    
    s = S.split(" ")
    for i in range(1,N+1):
        
        seatA = str(i)+'A'
        
        if (str(i)+'A' not in s) and (str(i)+'B' not in s) and (str(i)+'C' not in s) :
            available = available + 1
        if (str(i)+'D' not in s) and (str(i)+'E' not in s) and (str(i)+'F' not in s) and (str(i)+'G' not in s):
            available = available + 1
        if (str(i)+'H' not in s) and (str(i)+'J' not in s) and (str(i)+'K' not in s):
            available = available + 1
    
    result = available
    return result

print(solution(1,' '))