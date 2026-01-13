#!/usr/bin/env python3
import sys

sec = int(sys.argv[1])

h = sec // 3600
rest = sec % 3600
min = rest // 60
rest_sec = rest % 60

print(f"{h}h{min}m{rest_sec}s")
