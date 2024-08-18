def fib(n):

    if n<=1:
        return n
    last = fib(n-1)
    s_last = fib(n-2)

    return last + s_last



if __name__ == "__main__":
    
    # to print the nth fibonacci
    n = int(input())
    print(fib(n))

    """
    to print the fibonacci squence use for loop
    for each i print the nth fib(i)
    """

    # for i in range(n+1):

    #     print(fib(i))


