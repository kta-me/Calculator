i=7
a=1
b=5

def whileFunction(i):
    while i < 10:
        print(i)
        i += 1

def ifFunction(a, b):
    if a == b:
        print("a == b")
    else:
        print("a not equal b")

def devisionControl(a):
    if a % 3 == 0:
        print("Number is devided 3")
    else:
        print("Number is not devided 3")

whileFunction(i)
ifFunction(a, b)
devisionControl(9)
