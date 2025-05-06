#!/usr/bin/env python3
import sys
if len(sys.argv) > 1: 
    print("none")
else :
    num = 0
    while num <= 10 :
        print(f"table de {num};" , end = " ") 
      
        j = 0
        while j <=10 :
            print(f"{num * j}" , end = " ") 
            j += 1
        print() 
        num += 1
