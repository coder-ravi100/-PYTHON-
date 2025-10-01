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
fruits = ["apple","banana","Cherry"]
print(fruits.index("banana"))