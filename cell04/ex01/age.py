#!/usr/bin/env python3
age = int(input("Please tell me your age: "))
print('You are currently', age ,'years old.')
i = 10
while (i < 40) :
  print(f"In {i} years, you'll be {age + i} years old.")
  i += 10
