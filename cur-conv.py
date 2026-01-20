#!/usr/bin/env python3
import sys
import math


anzahl = float(sys.argv[1])
waehrung = sys.argv[2]
match waehrung:
	case 'USD':
		chf = anzahl * 0.80
		print(f"CHF {chf: 0.2f}")
	case 'EUR':
		chf = anzahl * 0.93
		print(f"CHF {chf: 0.2f}")
	case 'GBP':
		chf = anzahl * 1.07
		print(f"CHF {chf: 0.2f}")

