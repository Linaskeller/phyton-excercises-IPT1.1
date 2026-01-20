#!/usr/bin/env python3
import sys
import math

grad = float(sys.argv[1])
einheit = sys.argv[2]


match einheit:
	case 'c' | 'C':
		fahrenheit = grad *(9/5) + 32
		print(f"{grad}°{einheit} = {fahrenheit: 0.1f}°F")
	case 'f' | 'F':
		celsius = (grad -32) * (5 / 9)
		print(f"{grad}°{einheit} = {celsius: 0.1f}°C")
