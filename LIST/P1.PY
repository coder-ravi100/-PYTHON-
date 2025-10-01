#1.APPEN(X) METHOD FUNCTION
#LAST MEIN ELEMENT ADD KARTA HAI
#EX :1.append()
lst_nums = [12,34,56,78]
print(f"Original List {lst_nums}")

lst_nums.append(900)
print(f"After append {lst_nums}")

lst_nums.append(700)
print(f"After append {lst_nums}")

lst_nums.append(450)
print(f"After append {lst_nums}")

#2.EXTEND(LIST)
#EK LIST KE SAATH DUSARI LIST MERGE KARTA HAI 

#EX 1:EXTEND(LIST)
a = [1,2]
b = [3,4]
print(f"Before {a}")
a.extend(b)
print(f"After {a}")

#EX 2: EXTEND(LIST)
lst1 = ["Ahmedabad","Baroda"]
lst2 = ["Udaipur","Jaipur"]
lst1.extend(lst2)
print(lst1)

#3.DEL()KEYWORD HAI 
#KISI ELEMENT KO DELETE KARNE KELIYE

#EX 1:DEL()
nums = [10,20,30,40,50,60,70,80,90,100] #single time delete hota hai
del nums[9]
print(nums)

#EX 2:DEL()
iteam = [32.56,"Test","Ahmedabad",21]
del iteam[2]
print(iteam)

#4.COPY()FUNCTION
#EK COPY BANATA HAI (INDEPENDET HOTI HAI)

#EX 1:
a = [1,2,3]
b = a.copy()
b.append(4)
print(a)
print(b)

#EX 2:
iteam = [32.56,"Ahmedabad","Test",23]
new_iteam = iteam.copy()
new_iteam.append("Rajkot")
print(iteam)
print(new_iteam)

#5.CLEAR()FUNCTION
#PURA LIST EMPTY KAR DEGA

#EX 1:
nums = [1,2,3,4]
copy = nums
print(copy)

nums.clear()
print(nums)

#EX 2:
iteam = [32.56,"Ahmedabad","Surat",90]
copy = iteam
print(copy)
iteam.clear()
print(iteam)

#6.INSERT(INDEX,X)FUNCTION
#SPECIFIC INDEX PAR ELEMENT ADD KAREGA

#EX 1:
fruits = ["apple","cherry"]
copy = fruits
print(fruits)
fruits.insert(1,"Banana")
print(fruits)

cities = ["Ahmedabad","Rajkot","Baroda","Surat"]
copy = cities
print(copy)
cities.insert(1,"Modasa")
print(cities)

#7.COUNT(X)FUNCTION
#KITANI BAAR ELEMENT REPEAT HUA HAI

#EX 1:
cities = ["Ahmedabad","Modasa","Modasa","Modasa","Surat","Varodara"]
# copy = cities
# print(copy)
print(f"{cities.count("Modasa")}")
print(cities.count("Surat"))
print(f"{cities.count("Valsad")}")

#EX 2:
nums = [12,11,12,13,11,14,15,11,12,19]
print(f"{nums.count(11)}")
print(nums.count(12))


#8.INDEX(X)
#ELEMENT KA PEHLA INDEX POSITION RETURN KAREGA (INDEX POSITION RETURN KARTA HAI)

#EX 1:
fruits = ["apple","banana","Cherry","Mengo","Coconate"]
print(fruits.index("banana"))
print(fruits.index("Cherry"))

#EX 2:
nums =  [23,34,54,23,45,56,89,23,56,23]
print(nums.index(23,4,8))

#DRY RUN CODE
'''
| 0:23 | 1:34 | 2:54 | 3:23 | 4:45 | 5:56 | 6:89 | 7:23 | 8:56 | 9:23 |

INDEX 4-->45(NOT FOUND)
INDEX 5-->56(NOT FOUND)
INDEX 6-->89(NOT FOUND)
INDEX 7-->45(YEH FOUNDED)
OUTPUT:PRINT = 7
'''

#9.POP(INDEX)
#ELEMENT REMOVE KAREGA (BY DEFAULT LAST ELEMENT FOR REMOVE)

#EX 1:
element = [10,20,30,40]
element.pop()
print(element) #DELETE FRO LAST ELEMENT 40 

#EX 2:
cities = ["Ahmedabad","Baroda","Anand","Modasa","Baroda","Gandhinagar"]
print(f"After {cities}")
cities.pop() #last element (Gandhinagar) remove
cities.pop() #ab new last element (Baroda) remove
cities.pop() #ab  new last element (Modasa) remove
cities.pop(2)#index 2 pe jo element hai (Anand)
print(f"Before {cities}")


#10.REMOVE(X)METHOD❌ DOUBT 
'''
SIRF PEHLA OCCURENCE HATATA HAI JO LIST ME MILTA HAI 
AGAR ELEMENT NAHI MILA TO ERROR DETA HAI
YEH METHOD RETURN  KUCH BHI NAHI KARTA (SIRF LIST KO MODIFY KARTA HAI)
'''

#EX 1:
nums = [10,20,30,20,40,10]#REMOVE 10
nums.remove(10)
print(nums)

#EX 2:
nums = [10,20,30]#REMOVE 10 
nums.remove(10)
print(nums)

#EX 3:
iteams = ['Ahmedabad',345,567,345,345,6756,34234]
print(f"Before Remove {iteams}")
iteams.remove(345)
print(f"After Remove {iteams}")


#11.REVERSE()
#LIST.REVERSE() : LIST KE SAARE ELEMENTS KO ULTA KAR DETA HAI (LAST-FIRST,FIRST-LAST)
#SIRF ORDER CHANGE KARTA HAI SORTING NAHI
#YEH FUNCTION KUCH BHI RETURN NAHI KARTA LIST KO MODIFY KARTA HAI

#EX 1:
nums = [20,10,30,50]
print(f"Normal String:{nums}")
nums.reverse()
print(f"Reverse String:{nums}")


#EX 2:
cities = ['Ahmedabad','Ajmer','Jaipur','Gandhinagar']
print(f"Normal String :{cities}")
cities.reverse()
print(f"Reverse String :{cities}")


#12.SORT()FUNCTION
#LLIST.SORT() LIST KO ASCENDING ORDER (BY DEFAULT) YA 
#DESCENDING (REVERSE=TRUE) ORDER ME  ARRANGE KARTA HAI
#DEFAULT = ASCENDING ORDER
#AGAR REVERSE  = TRUE PASS KARO - > DESCENDING HOGA 

#EX 1:
nums = [40,10,20,30]
nums.sort()
print(nums)#(ASCENDING ORDER)

#EX 2:
nums.sort(reverse=True)
print(nums)#(DESCENDING)

# lst = [10,'Python',30]
# lst.sort()
# print(lst)

#EX 3:
letter = ['Ahmedabad','Ajmer','Jaipur']
letter.sort(reverse=True)
print(letter) #(DESCENDING)



