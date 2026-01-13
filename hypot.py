#!/usr/bin/env python3
import sys
import math

x = float(sys.argv[1])
y = float(sys.argv[2])

z = math.sqrt(x**2 + y**2)

print(f"c={z:.2f}")
