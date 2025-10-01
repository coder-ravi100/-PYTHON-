#STRING METHOD
#1.ACCESS STRING
#2.STRING INDEXING
#3.STRING SLICING

#1.STRING ACCESS
#STRING KE KISI LETTER KO DIRECTLY ACCESS KARNA
name = "python"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[-1])
#print(name[6]) error show becouse 6 index in not present
print("-------")


str1 = "This Is Python Class"
print(str1[-4]) 
print(len(str1))

#2.INDEXING 
#LIST / ARRAY KE ANDER HAR ELEMENT KO EK NUMBER ASSIGN KIYA JATA  HAIA USS NUMBER KO INDEX KEHTE HAIN
#INDEX NEGATIVE OR POSITIVE HOTE HAI
#USING LOOP
name = "python"
for i in name:
    print(i)

print("------")

#name = input ("Enter The Name :")
for i in range(len(name)):
    print(f"{i}--->{name[i]}")
'''
❓"len() kyu use kiya?"
➡️ Kyunki humein loop ko utni baar chalana hai jitne characters string mein hai.
Without len(), Python ko pata hi nahi chalega ki string kitni lambi hai.
'''


print("--------")


#3.STRING SLICING
#STRING SCLICING KA MATLAB HOTA HAI EK STRING KE PART (SUBSTRING) KO NIKALNA ORIGINAL STRING  KO CUT KARKE
#[START : STOP : STEP]

name = "Tops Technologies"
#1
print(name[0:5]) #OUTPUT: Tops

#2
print(name[4:11]) #OUTPU: _Techno

#3.
print(name[5:]) #OUTPUT: Technologies

#4.
print(name[:10]) #zero by default hi rahega
#OUTPUT: Tops Techn

#5.
one_name = "Tops Technologies"
print(one_name[::2])
#OUTPUT: Tp ehoois

#6.
two_name = "Tops Technologies"
print(two_name[5:2])
#OUTPUT: Black Kuch bhi output nahi aaya



#REVERSE STRING LOGIC MEANS:RA VI = VI RA
text = input("Enter The Name:")
total_len = len(text)
half_part = total_len // 2
print(half_part)

first_part = text[:half_part]
second_part = text[half_part:]
print(f"Fisrt Part:{first_part} Second Part:{second_part}")
final_part = second_part + first_part
print(f"{final_part}")
