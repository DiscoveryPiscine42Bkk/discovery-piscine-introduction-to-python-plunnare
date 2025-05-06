#!/usr/bin/env python3
a = int(input("Enter a number less than 25  \n"))
if ( a < 25 ) :
    i = a
    while ( i <= 25 ) :
        print ('Inside the loop, my variable is', i)
        i += 1
else :
    print("Error")
