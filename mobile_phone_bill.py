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

minutesUsed = "Enter the minutes used during the month: "
minutesCharged = int(input(minutesUsed))

# DETERMINE THE PACKAGE AND CALCULATE BILLS
validBill = False
if minutesCharged < 0:
  print ("ERROR! Invalid number.")
elif selectedPackage == "A":
  print ("PACKAGE A", divider2)
  if minutesCharged > packageAMinutes:
    additionalMinutes = minutesCharged - packageAMinutes
    additionalCharge = additionalMinutes * packageARate
  else:
    additionalMinutes = 0
    additionalCharge = 0
  validBill = True
  monthlyCharge = packageACharge
  totalbill = packageACharge + additionalCharge
elif selectedPackage == "B":
  print ("PACKAGE B", divider2)
  if minutesCharged > packageBMinutes:
    additionalMinutes = minutesCharged - packageBMinutes
    additionalCharge = additionalMinutes * packageBRate
  else:
    additionalMinutes = 0
    additionalCharge = 0
  validBill = True
  monthlyCharge = packageBCharge
  totalbill = packageBCharge + additionalCharge
elif selectedPackage == "C":
  print ("PACKAGE C", divider2)
  additionalMinutes = 0  
  additionalCharge = 0
  monthlyCharge = packageCCharge
  totalbill = packageCCharge + additionalCharge
  validBill = True
else:
  print ("Invalid package selected.")

# DISPLAY THE REPORT
if validBill == True:
  if selectedPackage == "C":
    print("*UNLIMITED MINUTES: no additional charge*")
  print()
  print ("YOUR MONTHLY BILL", divider2)
  print("Selected package: ",selectedPackage)
  print("Minutes used: ", minutesCharged)
  print(f"Monthly charge: ${monthlyCharge:.2f}")
  print("Additional minutes:", additionalMinutes)
  print(f"Additional minutes charge: ${additionalCharge:.2f}")
  print(f"Total amount due: ${totalbill:.2f}")
else:
  print ("No bill was calculated.")