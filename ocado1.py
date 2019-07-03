def solution(A):
    sum = 0
    count =0
    A2= []
    print(len(A))
    for num in A:
        count = count +1
        print(num)

        if num >= 0 and (len(A)) > count:
            print('here')
            print(sum)
            sum = sum + num
            print(sum)            
        elif (len(A)) == count and num >0:

            sum = sum +num
            A2.append(sum)
            
            print(A2)
        else:
            print('negt')
            print(sum)   
            A2.append(sum)
            sum = 0
            print(A2)
    
    return (max(A2))

A = [1,-2,3,4,-4]
print(solution(A))