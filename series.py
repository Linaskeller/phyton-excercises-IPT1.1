#!/usr/bin/env python3
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
x = 0
y = a

while x < b:
	print(f"{a}", end =" ")
	x += 1
	a += y
print(f" ")
