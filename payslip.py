#!/usr/bin/env python3
import math
import sys

brutto = float(sys.argv[1])

ahv = brutto * 0.087
iv = brutto * 0.014
eo = brutto * 0.005
alv = brutto * 0.011
nbu = brutto * 0.0073
pk = brutto * 0.089

netto = brutto - ahv - iv - eo - alv - nbu - pk

print(f"{'Bruttolohn':<12} {brutto:>10.2f}")
print(f"{'AHV:':<12} {-ahv:>10.2f}")
print(f"{'IV:':<12} {-iv:>10.2f}")
print(f"{'EO:':<12} {-eo:>10.2f}")
print(f"{'ALV:':<12} {-alv:>10.2f}")
print(f"{'NBU:':<12} {-nbu:>10.2f}")
print(f"{'PK:':<12} {-pk:>10.2f}")
print(f"{'Nettolohn:':<12} {netto:>10.2f}")
