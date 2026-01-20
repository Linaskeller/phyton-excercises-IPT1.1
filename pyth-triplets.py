#!/usr/bin/env python3
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

a_square = a * a
b_square = b * b
c_square = c * c

if a_square + b_square == c_square :
	print(f"{a}, {b} und {c} sind ein pythagoräisches triplet")
else:
	print(f"{a}, {b} und {c} sind kein pythagoräisches triplet")

