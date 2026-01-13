#!/usr/bin/env python3
import math
import sys

radius = float(sys.argv[1])

Umfang = 2 * math.pi * radius
Flache = math.pi * radius * radius

print(f"A={Flache:.2f}\nU={Umfang:.2f}")
