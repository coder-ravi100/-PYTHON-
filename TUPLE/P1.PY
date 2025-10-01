'''
2.TUPLE 
TUPLE EK COLLECTION DATA TYPE HAI (LIKE LIST)
LEKIN IMMUTABLE HAI = MEANS EK BAAR BAN GAYA TO USKE ELEMENTS CHANGE 
NAHI KAR SAKTE (ADD,REMOVE,UPDATE) POSSIBLE NAHI HAI

SYNTAX :  (1,2,3) OR 1,2,3

'''
#EX 1:TUPLE
num1 = (10,20,30)
num2 = 15,25,35
num3 = [40,50,60]
t = tuple(num3)#CONVERT INTO LIST TO TUPLE
print(f"Tuple Elements :num1:{num1}")
print(f"Tuple Elements :num2:{num2}")
print(f"Tuple Elements :num3:{t}")

