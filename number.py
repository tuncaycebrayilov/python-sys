n = []
n.append(input('Enter your number: '))

def number(func):
    def wrapper(n):
        func("+994" + " " + a[1] + a[2] + " " + a[3] + a[4] + a[5] + " " + a[6] + a[7] + " " + a[8] + a[9] for a in n)
    return wrapper

@number
def number(n):
    print(*(n))

number(n)