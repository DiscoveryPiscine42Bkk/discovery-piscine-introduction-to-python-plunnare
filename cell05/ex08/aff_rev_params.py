#!/usr/bin/env python3
import sys 

if len(sys.argv) != 4 :
    print("none")
else : 
    for i in reversed(sys.argv[1:]): 
        print(i)