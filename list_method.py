#append()	Adds an element at the end of the list

my_list=['mary', 'john', 'alex', 1000 ,200, 3000,]
my_list.append('Donkey')
print(my_list)

my_list.insert(1,'elyas')
print(my_list)

my_list.pop(3)
print(my_list)

#append
lst=[10,20,30,['jane','mary',[1000,2000,3000]],40,50,60]
lst.append(70)
print(lst)

#insert
lst[3][2].insert(1,1500)
print(lst)

#sort
lst1=[50,20,10,1,5]
lst1.sort(reverse=True)
print(lst1)

#extend
lst2=['mary', 'john', 'alex']
lst1=[50,20,10,1,5]
lst2.extend(lst1)
print(lst2)
#count
print(lst2.count('mary'))