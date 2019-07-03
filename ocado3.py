def solution(A):
    decimal =int(A,2) 
    
    count = 0
    while decimal >= 1:
        if(decimal%2==0):
            decimal = decimal /2
        else:
            decimal= decimal -1
        print (decimal)
        
        count = count +1


    return(count)

A = '011100'
print(solution(A))