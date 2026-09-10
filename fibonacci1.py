def fib(xn):
    
    #if not (isinstance(n, int)):
        #raise TypeError("n must be an integer")
    #if n < 0:
        #raise ValueError("n must be 0 or higher")

    # base case
    x1 = 0
    x2 = 1
    xn = x1
    for i in range(xn):
        xn = x1 + x2
        x1 = x2
        x2 = xn
    return  xn


if __name__ == "__main__":
    print(fib(4)) 