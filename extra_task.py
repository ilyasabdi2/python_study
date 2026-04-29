#Create a new file extra_if_task.py

#1.Write a program that checks login credentials:
#"Access granted" if email = "admin@gmail.com" and password = "Admin@123"
#"Wrong password" if email is correct but password is wrong
#"Email not found" otherwise
password=input("Enter your email: ")
email=input("Enter you password: ")
correct_password= "Admin@123"
correct_email="admin@gmail.com"
if email == "admin@gmail.com" and password == "Admin@123" :
    print("Access granted")

elif email==correct_email and password !=correct_password :
    print("Wrong password")

else :
    print("Email not found")
    

#2.Create a program that validates an email:
#"Invalid email" if it does not contain "@" or "."
#"Gmail account" if it ends with "@gmail.com"
#"Other email provider" otherwise
Email=input("Enter your email: ")
if "@" not in email or "."  not in email :
    print("Invalid email")

elif email.endswith("@gmail.com") :
    print("Gmail account")

else:
    print("Other email provider")

#3.Write a program that checks password strength:
#"Weak" if length < 6
#"Moderate" if length 6–10 and contains at least one digit
#"Strong" if length > 10 and contains both digits and uppercase letters
#Strength=input("password length: ")
#if len ("password")< 6 :
   # print("Weak")

#elif 'length' >6 and 'length' <=10 :
   # print("Moderate")

#else:
    #print("Strong")


#4.Write a program that checks a password:
#"Invalid" if it does not start with a capital letter
#"Invalid" if it does not end with a number
#"Valid password" otherwise
password=input("Enter your password: ")

if not password[0].isupper():
    print("Invalid")
elif not password[-1].isdigit():
    print("Invalid")
else:
    print("Valid password")

#5.Write a program that takes a number and checks:
#"Fizz" if divisible by 3
#"Buzz" if divisible by 5
#"FizzBuzz" if divisible by both
#Otherwise print the number
number=int(input("Enter number: "))
if number % 3 == 0 and number % 5 == 0 :
    print("FizzBuzz")

elif number % 5 == 0 :
    print("Buzz")

elif number % 3 == 0 :
    print("Fizz")

else:
    print(number)


#6.Create a program that takes a score and prints a grade:
#A (≥ 80)
#B (70–79)
#C (60–69)
#D (50–59)
#F (< 50)

score=int(input('Enter your score: '))
if score >=80:
    print("Grande A")

elif score>=70 and score <=79 :
    print("Grande B")

elif score>=60 and score <=69 :
    print("Grande C")

elif score>=50 and score <=59 :
    print("Grande D")

else:
    print("F")


#7.Create a program that takes two numbers and prints:
#"Equal" if same"
#"First is greater"
#"Second is greater"
num1=int(input("Enter your number: "))
num2=int(input("Enter your number: "))
if num1>num2:
    print("First is greater")

elif num2>num1:
    print("Second is greater")

else:
    print("Equal")

    
#8Write a program that takes a day number (1–7) and prints:
#Weekday (1–5)
#Weekend (6–7)
days=int(input("Enter your days number: "))
if 1<= days <= 5 :
    print("Weekday")

elif 6<= days <=7 :
    print("Weekend")

else:
    print("Invalid day number")


#9.Create a program that takes a temperature and prints:
#"Freezing" if ≤ 0
#"Cold" if 1–15
#"Warm" if 16–30
#"Hot" if > 30
temp=int(input('Enter the temp: '))
if temp <0:
    print("Freezing")

elif temp>=1 and temp<=15 :
    print("Cold")

elif temp>=16 and temp<=30 :
    print("Warm")

else:
    print("Hot")


#10.Create a program that takes a year and prints:
#"Leap year" if divisible by 4
#"Century year" if divisible by 100
#"Common year" otherwise
year = int(input("Enter a year: "))

if year % 100 == 0:
    print("Century year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Common year")