
def f(A):
    for i :=0; i< A.length -1; i++ do:
        if (A[i] > A[i+1]):
            swap A[i] with A[i+1]
    return A