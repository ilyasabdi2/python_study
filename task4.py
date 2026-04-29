#1.Take three inputs from a user, separately. Print the largest of the numbers.
    #Hint: Determine what type of data is taken in as input.
num1=input('Enter the fisrt number:')
num1=int(num1)
num2=input("Enter the second numer: ")
num2=int(num2)
num3=input("Enter the third numner: ")
num3=int(num3)
num4=input("Enter the fourth number: ")
num4=int(num4)

if num1>num2 and num1>num3 and num1>num4:
    print(num1)

elif num2>num1 and num2>num3 and num2>num4:
    print(num2)

elif num3>num1 and num3>num2 and num3>num4: 
    print(num3)

else :
    print(num4)


#2.Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# Take temperature input from user
temperature = float(input("Enter the temperature in °C: "))

# Check conditions
if temperature > 30:
    print("The temperature is too high")
elif temperature > 15 and temperature<=30:
    print("Normal temperature")
else:
    print("Cold temperature")


#use a balance 
balance=int(input("Enter your balance: "))
if balance <100 :
    print("Insufficient funds")

elif balance >=100 and balance<= 1000:
    print('Moderate balance')

else:
    print("High balance")

#3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
number=int(input("Enter your number: "))
if number <10 :
    print("small")
elif number >10 and number<50 :
    print("Meduim")

else:
    print("Large")


#4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
password=input("enter your password: ")
correct_password="secret123"
if password==correct_password:
    print("Access   granted")

else:
    print("Access denied")

# Write a program that asks the user for email and password checks if the email is equal to "admin@gmail.com" and passaword is equal to "admin123" if it is print Access granted otherwise print Access Denied
password=input("Enter your password: ")
email=input("Enter your email: ")
correct_password='admin123'
correct_email="admin@gmail.com"
if password==correct_password:
    print(' Access granted')

elif correct_email:
    print("Access granted")

else:
    print("Access denied")