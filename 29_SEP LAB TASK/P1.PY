
#1.CONVERT NAMES TO UPPER CASE FROM LIST

#list = ["ravi","romil","Shyaam","Abhijit"]
#output  = [RAVI, ROMIL, SHYAAM, ABHIJIT]
#METHOD 1🤣 WRONG
#names = ["ravi","romil","Shyaam","Abhijit"]
# iteam1 = names[0].upper()
# iteam2 = names[1].upper()
# iteam3 = names[2].upper()
# iteam4 = names[3].upper()
# print(iteam1,iteam2,iteam3,iteam4)

#2.METHOD USE APPEND FUNCTION
names = ["ravi","romil","shyaam","abhijit"]
uppar_case = [] #empty list
for counter in names:
    uppar_case.append(counter.upper())

print(uppar_case)


#2.FIND LENGTH OF EACH STRING FROM LIST
#INPUT: ravi,romil,abhijit,shyaam
#OUTPUT:4, 5, 5, 7
iteam = ["ravi","romil","Aarya","abhijit"]
length_list = [] #khaali list mein element aayege
for counter in iteam:
    length_list.append(len(counter))

print(length_list)


#3.FIND LARGEST STRING FROM LIST
names = ["ravi","romil","Aarya","abhijit"]
largest = names[0] #assume pehle hi sabse bada hai

for i in names:
    if len(i) > len(largest):  #agar current name lamba hai
        largest = i            #update largest

print("Largest Name Is:",largest)

#4.CREATE VALID EMAIL ID (@ AUR 'DOT' DONO  HONE CHAHIY AUR @ KE BAAD 'DOT' AANA CHAHIYE)
email = "ravirathod100100@gmail.com" #doubt Question
ans = email.endswith(".com")
if ans:
    print(f"{email}:is Valid Email Address")
else:
    print(f"{email}:is Invalid Email Address")
    
#5.FIND SECOND HIGHEST NUMBER (WIITHOUT SORT AND MAX IN BUILT FUNCTION) IN LIST
names = [20,50,40,10]
highest_num = [0]

#The code remains to be written
'''
middle number logic code for C language
int a = 10, b = 20, c = 30;
int max , min ,middle;
max = a;
if(b > max) max = b;
if(c > max) max = x;

min = a;
if(b < min) min = b;
if(c < min) min = c;

mindle = (a + b + c) - max - min;
printf("Middle %d",middle)

'''

#6.FIND NUMBER OF VOWELS IN STRING FROM LIST
#INPUT: ['ravi','romil','raaj','abhijit']
#OUTPUT:[ravi=2,romil=2,raaj=2,abhijit=3]

# iteam = ['ravi','romil','raaj','abhijit']
# vowels_list = [0]
vowels_list = input("Enter The Value :")
#for i in vowels_list:
if(vowels_list == 'a' or vowels_list == 'e' or vowels_list == 'i' or vowels_list == 'o'or vowels_list == 'u' 
    and 'A' or vowels_list == 'E' or vowels_list == 'I' or vowels_list == 'O' or vowels_list == 'U'):
        #vowels_list.append(len(counter))
    print("Vowel:",vowels_list)
else:
    print("Consonant:",vowels_list)

    #The code remains to be written