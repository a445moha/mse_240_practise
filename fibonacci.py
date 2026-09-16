def fib(n):
    
    #if not (isinstance(n, int)):
        #raise TypeError("n must be an integer")
    #if n < 0:
        #raise ValueError("n must be 0 or higher")

    # base case..
    if n == 0:
        return 0
    elif n == 1:
        return 1

    n1 = fib(n - 1)
    n2 = fib(n - 2)
    
    # recursive case
    return _fib(n, 0, 1, 2)

def _fib(target, fib_i_minus_1, fib_1_minus_2, i):
    fib_i = fib_i_minus_1 + fib_1_minus_2
    if i == target:
        return fib_i
    else:
        return fib(target, fib_i, fib_i_minus_1, i + 1)

    

if __name__ == "__main__":
    print(fib()) 