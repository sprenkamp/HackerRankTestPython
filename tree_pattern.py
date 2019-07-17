def solution(A):
    count = 0
    for n, i in enumerate(A):
        if len(A)-(n+1) > 0:
            if A[n+1] == i:
                if len(A)-(n+1)>1 and A[n+2] < i:
                    new_height = A[n+2] - 1
                else:
                    new_height = i - 1
                A[n+1] = new_height
                count = count + 1
            if len(A)-(n+1) > 1:
                if A[n+1] < i and A[n + 1] > A[n+2]:
                    new_height = A[n+2] - 1
                    A[n+1] = new_height
                    count = count + 1
                elif A[n+1] > i and A[n + 1] < A[n+2]:
                    new_height = i - 1
                    A[n+1] = new_height
                    count = count + 1         
    return(count)

A =  [5, 4, 3, 2, 6] 
B = [3,3,5,2]
C = [3,3]
print(solution(C))