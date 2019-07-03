def solution(A):

    B=[]
    if len(A) <= 1:
        return -2
    else:
        A= sorted(A)

        seen = {}
        dupes = []

        for x in A:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    return 0
                seen[x] += 1

        diff = 10**20
        n = len(A)
        for i in range(n-1): 
            if A[i+1] - A[i] < diff: 
                diff = A[i+1] - A[i]

        if diff > 100000000:
            return -1
        else:
            return diff
        
A = [0, 3, 3, 7, 5, 3, 11, 1]
print(solution(A))