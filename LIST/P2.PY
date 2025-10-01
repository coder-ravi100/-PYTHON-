#LIST COMPREHENSION
#1.NORMAL WAY (LONG FROM) #doubt
lst1 = [1,2,3,4]
lst2 = []
for i in lst1:
    lst2.append(i)
print(lst2)


#2.LIST COMPREHENSION (SHORT FORM) #doubt
lst1 = [10,20,30,40]
lst2 = [i for i in lst1]
print(lst2)


#MORE EXAMPLE OF COMPREHENSION
#1.FIND SQUARE OF NUMBER
lst = [1,2,3,4,5]
squares = [i*i for i in lst]
print(squares)

#FIND EVEN NUMBERS ONLY
lst = [1,2,3,4,5,6,7,8,9,10]
even_list = [i for i in lst if i % 2  == 0 ]
print(even_list)