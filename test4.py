def f(n):
    if n ==1:
        return 1
    x= f(n/2)
    y =f(n/2)
    return 2

print(f(6))