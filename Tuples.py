days_of_the_wk=('Monday', 'Tuesday','Wednsday','Thursday','Friday','Saturday','Sunday')
print(days_of_the_wk[1:4])
print(days_of_the_wk[5])
print(days_of_the_wk[3:6])


days_of_the_wk=list(days_of_the_wk)
days_of_the_wk[1]='tue'
print(days_of_the_wk)

days_of_the_wk.append('January')
print(days_of_the_wk)
days_of_the_wk=tuple(days_of_the_wk)
print(days_of_the_wk)
