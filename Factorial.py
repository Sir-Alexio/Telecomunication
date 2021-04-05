
def myFact(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*(myFact(n-1))


