# PJ Bryan
# CMP-131-80230
# Week 06
# Lab 01
# Assignment 6
# 10/08/2026

# PROGRAM TITLE AND DIVIDERS
divider1 = "*******************"
divider2 = "-------------------"
print ("MOBILE PHONE BILL", divider1)
print()

# PACKAGE A
packageACharge = 39.99
packageAMinutes = 450
packageARate = 0.45

print("PACKAGE A", divider2)
print(f"Monthly charge: ${packageACharge:.2f}")
print("Included minutes:", packageAMinutes)
print(f"Additional minute rate: ${packageARate:.2f}")

print()

# PACKAGE B
packageBCharge = 59.99
packageBMinutes = 900
packageBRate = 0.40

print("PACKAGE B", divider2)
print(f"Monthly charge: ${packageBCharge:.2f}")
print("Included minutes:", packageBMinutes)
print(f"Additional minute rate: ${packageBRate:.2f}")

print()

# PACKAGE C
packageCCharge = 69.99
packageCMinutes = "UNLIMITED"
packageCRate = "NO ADDITIONAL CHARGES"

print("PACKAGE C", divider2)
print(f"Monthly charge: ${packageCCharge:.2f}")
print("Included minutes:", packageCMinutes)
print("Additional minute rate:", packageCRate)

print()

# ASK AND STORE USER INPUT
requestedPackage = "Select a package (A, B, or C): "
selectedPackage = input(requestedPackage)
#minutes input
