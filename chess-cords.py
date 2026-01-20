#!/usr/bin/env python3
import sys
import math

chord = sys.argv[1]
straight = int(chord[1]) % 2

match chord[0]:
	case 'a'|'c'|'e'|'g':
		if straight == 0:
			print(f"weiss")
		else:
			print(f"schwarz")
	case 'b'|'d'|'f'|'h':
		if straight == 0:
			print(f"schwarz")
		else:
			print(f"weiss")
