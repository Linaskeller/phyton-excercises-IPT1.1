#!/usr/bin/env python3
import sys
import math


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

diskriminante = (b * b) - (4 * a * c)

if diskriminante > 0:
	x_one = ( -b + math.sqrt(diskriminante)) / (2 * a)
	x_two = ( -b - math.sqrt(diskriminante)) / (2 * a)
	print(f"x1={x_one: .1f}, x2={x_two: .1f}")
elif diskriminante == 0:
	x = -b / 2*a
	print(f"x={x: .1f}")
else:
	print(f"keine lösung")

