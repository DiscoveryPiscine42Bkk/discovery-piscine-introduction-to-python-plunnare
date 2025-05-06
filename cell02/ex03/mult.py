#!/usr/bin/env python3
a = int(input("Enter the first number: \n"))
b = int(input("Enter the second number: \n"))
mi = a * b 
print (a, 'x', b ,'=', mi)
if (mi > 0) :
    print ("The result is positive.")
elif(mi < 0) :
    print("The result is negative.")
else :
    print("The result is positive and negative.")