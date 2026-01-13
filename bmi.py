#!/usr/bin/env python3

heightincm = float(input("Körpergrösse in cm: "))
weight = float(input("Körpergewicht in kg: "))

heightinm = heightincm / 100
bmi = weight / (heightinm ** 2)

print(f"Dein Body-Mass-Index: {bmi:.2f}")
