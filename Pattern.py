#1. Simple Diamond Pattern in Python
# no of columns = size
size = 8
spaces = size
for i in range(size//2+2):
    for j in range(size):
        # condition for left spaces
        if j < i-1:
            print(' ',end=" ")
        # condition for right spaces
        elif j > spaces:
            print(" ",end=" ")
        #condition for making diamond
        elif (i == 0 and j == 0) | (i == 0 and j == size - 1):
            print(' ',end=" ")
        else:
            print("*",end=" ")
    spaces -= 1
    print()
#2. Python – Print Heart Pattern
# 3. Pyhton half diamond pattern
def displat(n):
    print("*")

    for i in range(1,n+1):
        print("*",end="")
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print("*",end="")
        print()
    # to display above in reverse order
    for i in range(n-1,0,-1):
        print("*",end="")
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print("*",end="")
        print()
    print("*")

n = 5
print('\nfor n = ',n)
displat(n)
n = 3
print('\nfor n = ',n)
displat(n)
# Python Program to print hollow half diamond hash pattern
def hollow_half_diamond(n):
    # printing upper half pattern
    for i in range(1,n+1):
        for j in range(1,i+1):
            # printin hollow means # on only boundry
            if i == j or j == 1:
                print("#",end=" ")
            else:
                print(" ",end=" ")
        print()
    # now printing lower half
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            if j == 1 or i == j:
                print("#",end=" ")
            else:
                print(" ",end=" ")
        print()
if __name__ == "__main__":
    n = 7
    hollow_half_diamond(n)
#Program to Print K using Alphabets

# another pattern of same k type
def display_k(n):
    for i in range(n,0,-1):
        c = 65
        for j in range(0,i):
            print(chr(c+j),end=" ")
        print()

    for i in range(1,n):
        c = 65
        for j in range(0,i+1):
            print(chr(c + j),end=" ")
        print()
n = 5
display_k(n)
# Program to print half Diamond star pattern
def half_diamond_star(n):
    # upper half of pattern
    for i in range(n):
        for j in range(0,i+1):
            print("*",end="")
        print()
    # now lower half pattern
    for i in range(1,n):
        for j in range(i,n):
            print("*",end="")
        print()
n = 5
half_diamond_star(n)
# Python program to right rotate n-numbers by 1
def number_pattern(n):
    for i in range(1,n+1,1):
        for  j in range(1,n+1,1):
            if i == j:
                print(j,end=" ")
                # if i less than j
                if i <= j:
                    for k in range(j+1,n+1,1):
                        print(k,end=" ")
                for p in range(1,j,1):
                    print(p,end=" ")
        print()
n = 5
number_pattern(n)
# Python Program to print digit pattern
def digit_pattern(n):
    for i in n:
        print("|",end="")
        print("*" * int(i))
n = "41325"
digit_pattern(n)
# Python | Print an Inverted Star Pattern
def inverted_star(n):
    for i in range(n,0,-1):
        print((n-i) * " " + i * "*")
inverted_star(3)
inverted_star(5)
inverted_star(8)
# Program to print the diamond shape
def diamond(rows):
    for i in range(1,rows+1):
        #for upper part
        for j in range(1, rows-i+1):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
        print()
    for i in range(rows-1,0,-1):
        for j in range(1, rows-i+1):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
        print()
diamond(5)
diamond(8)
diamond(3)
# Programs for printing pyramid patterns in Python
def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()
pyramid(5)
pyramid(3)
# in 180 degrees
def pyramid180(n):
    #number of spaces
    x = 2*n - 2
    for i in range(0,n):
        for j in range(0,x):
            print(end=" ")
        # decrementing x after each loop
        x = x - 2
        # for columns
        for j in range(0,i+1):
            print("* ",end="")
        print()
pyramid180(5)
pyramid180(8)
# using loop
def pyramid180_1(n):
    for i in range(1,n+1):
        print(" " * (n-i) + "*" * i)

pyramid180_1(5)
pyramid180_1(8)
# number pattern
def number_pattern(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print()
number_pattern(5)
#
def num1(n):
    for i in range(n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
num1(5)
