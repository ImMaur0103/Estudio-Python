#---------------------------
#Program Lab 3.1.1.8
#Create by Mauricio Lopez
#--------------------------

#Read 2 numbers and find the largest number

#Read Number1
Number_1 = int(input("Enter the first number: "))

#Read Number2
Number_2 = int(input("Enter the second number: "))

if Number_1 < Number_2:
	Number_Larger = Number_2
elif Number_1 > Number_2:
	Number_Larger = Number_1
else:
	Number_Larger = 'The both numbers are the same(' + str(Number_1) + ')'

print("The larger number is:", str(Number_Larger))
