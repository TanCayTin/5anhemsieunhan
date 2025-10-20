'''
Made by PhucTan
I think it is too annoying to make too much file, so I did all the exercises in one file :V
'''

import math
def PrimeNumber(k):
    if k<2:
        return False
    
    for i in range (2, int(math.sqrt(k))):
        if k % i == 0:
            return False
    return True

    
def main():
    t = 1
    while t!=0:
        n = int(input("What task you want check? Only exercises 2, 4, 6, 8, and 10!\n"))
        if  n % 2 == 0 and 2<=n<=10 :
            t = 0
        
        else:
            print("Error, do it again!")
        
    if n == 2:
        a = int(input("Enter a random number: "))
        print (a)
        print ("This task takes a number then return them")
    elif n == 4:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        sum = n1 + n2
        print(" Sum of these numbers: ", sum)
        print("This task receives two numbers then gives the sum of them")
    elif n == 6:
        nu1 = int(input("Choose a number: "))
        nu2 = int(input("Choose an another number (can be the same with the last one): "))
        product = nu1*nu2
        print("The product of the these numbers is: ", product)
        print("Two numbers are the input of this task while their product is the aim of this task")
    elif n ==8:
        bro1 = int(input("Can you give me a number?: "))
        bro2 = int(input("OK thanks. But please give me one more number xD, but please don's type 0 :) : "))
        remainder = bro1 % bro2
        print("Ok so we got remainder of these number. It is: ", remainder)
        print("By getting two numbers from input, this task can give us the remainder of them")
    else:
        print("OK so we are going to print all prime number less than 100\n")
        for i in range (2, 100):
            if PrimeNumber(i):
                print(i)
        print("This task provide prime numbers from 1 to 100")
main()