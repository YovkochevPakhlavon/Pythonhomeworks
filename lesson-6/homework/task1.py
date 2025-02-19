def check(func):
    def divide(a,b):
        try:
            print(func(a,b))
        except ZeroDivisionError:
            print("Denominator can't be zero")
    return divide

@check
def div(a, b):
   return a / b

div(6,2)
div(6,0)