def solution(A):
    count = 0
    for n, i in enumerate(A):
        for j in range(n,len(A)):          
            if i == A[j]:              
                count = count + 1              
    self_count = len(A)
    count = count - self_count
    if count > 1000000000:
        return 1000000000
    return(count)

A =  [3, 5, 6, 3, 3, 5]
B = [3, 5, 6, 5,3,6]
print(solution(B))