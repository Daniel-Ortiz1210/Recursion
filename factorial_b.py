
def factorial(number, res=1):

    if number == 1:
        return res

    res *= number
    return factorial(number=number-1, res=res)


print(factorial(4))