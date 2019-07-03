def solution(A):
    arr2 = A.copy()
    count = 0
    
    for a in A:
        
        if a == count:
            arr2.pop(a)
        count = count + 1
        
    
    arr3 = arr2.copy()
    arr3.sort()
    
    count = 0
    for a in arr2:
        
        b = (arr3.index(a))
        
        if arr2[b] == arr3[count]:
            
            arr2.pop(a)
        count = count + 1
    ans = len(arr2)
    print('---')
    return ans 

A = [5, 4, 0, 3, 1, 6, 2]

print(solution(A))