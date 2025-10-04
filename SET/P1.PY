'''
SET DEFINITION
>COLLECTION TYPE IN PYTHON
>UNIQUE VALUES ONLY (DUPLICATES HATA DETA HAI)
>UNORDERED (KISI FIX ORDER MEIN NAHI HOTA)
>MUTABLE (ADD/REMOVE KAR SAKTE HO)
>INDEXING ❌ (LIST/TUPLE KI TARAH [0] SE ACCESS NAHI KAR SAKTE)
'''
#1.SET CREATION
#NORMAL SET
sets = {1,2,3,4}
print(sets)

#Empty set
sets = {}           #yeh Dictionary banata hai , set nahi
print(type(sets))   #<class 'dict>

#Empty Set
sets = set()
print(type(sets))   #<Class 'Set>

#2.ACCESSING ELEMENTS
#💊DIRECT INDEXING ❌
#💊LOOP SE ACCESS ✔️

sets = {"apple","banana","Mango"}
for i in sets:
    print(i,end=" ")

#SET METHODS (IMPORTANT FUNCTIONS)
#ADDING ELEMEMTS
sets = {1,2,3}
sets.add(4)  #EK ELEMENT ADD
print(sets)  #{1,2,3,4}

sets.update([5,6])  #MULTIPLE ELEMENTS ADD
print(sets)         #{1,2,3,4,5,6}

#REMOVING ELEMENTS 
sets = {1,2,3} #element hoga to hi remove karega warna error 
sets.remove(2) #{1,3}

sets.discard(5) #error nahi aayega  agar element nahi mila
print(sets)     #{1,3}

#POP ELEMENT (RANDOM REMOVE)
s = {10,20,30}
x = s.pop()
print(x)  #koi bhi ek random element
print(s)  #baaki set

#CLEAR SET
sets = {1,2,3}
sets.clear()
print(sets)

#DELETE SET
sets = {1,2,3,4}
del sets
#print(sets)

#MATHEMATICAL SET OPERATORS
print("#MATHEMATICAL SET OPERATORS")
a = {1,2,3,4}
b = {3,4,5,6}

print(a |  b)   #UNION {1,2,3,4,5,6}
print(a & b)    #INTERSECTION {3,4}
print(a - b)    #DIFFERENCE {1,2}
print(b - a)    #DIFFERENCE {5,6}
print(a ^ b)    #SYMMERTIC DIFFERENCE {1,2,5,6}

ans = a - b
print(f"defference :{ans}")
ans = b - a
print(f"defference :{ans}")


#USEFUL SET FUNCTIONS
sets = {10,20,30}
print(len(sets))    #SIZE OF SET
print(max(sets))    #LARGEST VALUE
print(min(sets))    #SMALLEST VALUE
print(sum(sets))    #SUM OF VALUES

print(20 in sets)       #TRUE
print(50 not in sets)   #TRUE


#SET RELATIONS (SUBSET / SUPERSET /DJSJOINT)
a = {1,2,3}
b = {1,2,3,4,5}
c = {6,7}

print(a.issubset(b))     #TRUE ()
print(b.issuperset(a))   #TRUE ()
print(a.isdisjoint(c))   #TRUE (NO COMMON ELEMENTS)

#FROZEN SET (IMMUTABLE SET)
#NORMAL SET MUTABLE HOTE HAI.FROZEN SET EK IMMUTABLE SET HAI (CHANGE NAHI KAR SAKTE)
fs = frozenset([1,2,3,4])
print(fs)
#fs.add(5) ❌ error can't  add to frozenset

#PRACTICAL EXAMPLE (DUPLICATE REMOVAL)
numbers = {1,2,2,3,4,4,5}
unique = set(numbers)
print(unique) #{1,2,3,4,5}

'''
Summary (Set ekdum short mein)

Set = Unique + Unordered + Mutable

Indexing ❌, Loop ✔️

Important methods = add(), update(), remove(), discard(), pop(), clear()

Operations = Union, Intersection, Difference, Symmetric Difference

Special = issubset(), issuperset(), isdisjoint()

Immutable version = frozenset
'''