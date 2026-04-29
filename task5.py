#1.An airline is pricing tickets differently for children and adults. Build a program that determines ticket cost based on age and applies a discount where applicable.
age = int(input("Enter age: "))
fare=1000
if age < 18:
       fare*=0.5
       res=f'50% discourt appleid fare ' 
       
else:
        res=f' No discount appleid ' 
300

print(res)

item=input('enter the name of the product:')
current_stock=int(input("enter the current stock:"))
minimum_stock=4000

if current_stock<=minimum_stock:
    print(f'{item} Stock needs restocking')
else:
    print(f'{item} stock is sufficient')

# A bank wants to improve its ATM service. Create a program that stores a customer’s name and 
#  request a withdrawal. If the amount requested is greater than the available balance, the transaction should fail. 
# If successful, deduct the amount together with a transaction fee of KES 30 and display the new balance.

custumer_name=input("Enter your name: ")
account_balance=10000
amount_requested=int(input("Enter the amount to withdrawal: "))

trans=30
if amount_requested>account_balance :
      print(f'{custumer_name} Transaction failed inssufficient funds to withdraw {amount_requested} your balance is {account_balance}')

else:
      account_balance=account_balance-(amount_requested + trans)
      print(f'{custumer_name} {amount_requested} withdrawned successfully New balance {account_balance}')


