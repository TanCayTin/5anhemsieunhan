def ex1():
    print("Hello, world!")

def ex3():
    a = int(input("Enter a: "))
    if a % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def ex5():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    h = a - b
    print("The difference between two numbers is:", h)

def ex7():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    t = a // b
    print("The quotient of two numbers is:", t)

def ex9():
    a = int(input("Enter a: "))
    ok = True
    for i in range(2, a):
        if a % i == 0:
            ok = False
            break
    if ok:
        print("Number is prime")
    else:
        print("Number is not prime")

def main():
    n = int(input("Which exercise number do you choose (odd number)? "))
    if n==1:
        ex1()
    elif n==3:
        ex3()
    elif n==5:
        ex5()
    elif n==7:
        ex7()
    else:
        ex9()

main()