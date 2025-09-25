'''
🎯Index kya hai?
Python (aur zyada languages) me string / list / array ke andar har ek element ko ek 
number assign kiya jata hai, us number ko index kehte hain. Ye number use karke hum us 
position pe rakhe character ya element ko access karte hain
'''

'''
str = "This is Pyrhon Class"
✅positive index ---> left se count (0 se shure)

T  h  i  s  I  s    P  y  t  h  o   n     C   l    a   s   s.

0  1  2  3  4  5    6  7  8  9  10  11    12  13   14  15  16

✅Negative Index --->Right Se Count (-1 se shuru)

     T    h   i   s     I   s     P   y   t   h   o  n    C  l  a  s  s
-19 -18 -17 -16   -15 -14   -13 -12 -11 -10 -9 -8   -7 -6 -5 -4 -3 -2 -1 
'''
str1 = "This is python Class"
print(str1[-4])
print(len(str1))

name = input("Enter name :")
for i in name:
    print(i)

#ACCESSING TROUGHT INDEX
for i in range (len(name)):
    print(f"{i} --->{name[i]}")