#-----------------------------------
#Lab 3.1.1.11
#Create by Mauricio Lopez
#-----------------------------------
income = float(input("Enter the annual income: "))

if income < 85528:
	tax = (income * 0.18) - 556.2
else:
	tax = 14839 + (income - 85528) * 0.32

if tax < 0:
	tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
