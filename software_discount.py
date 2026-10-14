# PJ Bryan
# CMP-131-80230
# Week 06
# Lab 01
# Assignment 6
# 10/08/2026


# PROGRAM TITLE AND DIVIDERS
divider1 = "*******************"
divider2 = "-------------------"
print ("SOFTWARE DISCOUNT", divider1)

# ASK AND STORE USER INPUT
numberofUnits = "Enter the amount of units purchased: "
unitsPurchased = int(input(numberofUnits))

# VALIDATE INPUT 
if unitsPurchased > 0:

# PERFORM CALCULATIONS
  originalCost = unitsPurchased * 99.00

# DETERMINING THE DISCOUNTS
  if unitsPurchased <= 9:
    discountRate = 0
  elif unitsPurchased <= 19:
    discountRate = 0.2
  elif unitsPurchased <= 49:
    discountRate = 0.3
  elif unitsPurchased <= 99:
    discountRate = 0.4
  else:
    discountRate = 0.5

# MORE CALCULATIONS
  discountAmount = originalCost * discountRate
  finalCost = originalCost - discountAmount

# PRINT CALCULATIONS
  print ("SUMMARY", divider2)

  print (f"Units Purchased: {unitsPurchased:,}")
  print ("Price per unit: $99.00")
  print (f"Original Cost: ${originalCost:,.2f}")
  print (f"Discount Rate: {discountRate:.0%}")
  print (f"Discount Amount: ${discountAmount:,.2f}")
  print (f"Final Cost: ${finalCost:,.2f}")


# ERROR MESSAGE
else:
  print ("ERROR! Value is less than, or equal to 0.")