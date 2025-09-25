#STRING SLICING -[START : STOP : STEP]
'''
🎯start → kaha se shuru karna hai (index number)
🎯stop → kaha tak lena hai (but stop index included nahi hota)
🎯step → kitne step chhod ke agla character lena hai (default 1 hota hai)
'''
#1.PRINT(NAME[0:5])
name1 = "Tops Technologies"
print(name1[0:5])
#INDEX 0 -> T , INDEX 4 -> S
#Rule:INDEX 0 SE 4 TAK KE LETTER PRINT HONGE
#OUTPUT : Tops 


#2.PRINT(NAME[4:10])
name2 = "Tops Technologies"
print(name2[4:11])
#INDEX :4 = SPACE = " "
#INDEX :9 = 0
#INDEX 11 EXCLUDED HAI
#OUTPUT:" Echno" (6Letter)

#3.PRINT(F"UPTO 10 LETTER {NAME[:10]}")
name3 = "Tops Technologies"
print(name3[:10])
#AGAR START EMPTY HAI -->DEFAULT = 0
#MATLAB NAME[0:10]
#OUTPUT:Tops Techno

#4.PRINT (F"FROM 5TH LETTER TO END {NAME4[5:]}")
name4 = "Tops Technologies"
print(f"From 5th Letter to end {name4[5:]}")
#Agar stop empty hai → default = end of string
#Matlab index 5 se last tak print karega
#Output: "Technologies"

#5.PRINT(F"PRINTING  ALTERNATE LATTER FROM STRING {NAME[::2]"})
name5 = "Tops Technologies"
print(f"Printing Alternate Latter From string {name5[::2]}")
#STEP = 2 -> HAR DUSRA CHARACTER LEGA
#"TOPS TECHNOLOGIES" -> "Tp hnlgis"

#6.PRINT(F"FROM 5TH LETTER TO END ALTERBATE LETTER {NAME[5::2]}")
name6 = "Tops Technologies"
print(f"From 5th Letter To End Alternate letter {name6[5::2]}")
#START = INDEX 5 (T TECHNOLOGIES)
#STEP = 2 (ALTERNATE LETTER)
#OUTPUT:  "Tcnlgis"

#7.PRINT(NAME[10:1])
name7 = "Tops Technologies"
print(name7[10:1])
#START = 10 , STOP = 1
#LEKIN PYTHON SLICING LEFT TO RIGHT HOTI HAI JAB STEP POSITIVE HO
#YAHA START > STOP HAI ->EMPTY STRING RETURN KAREGA
#OUTPUT : " " (BLACK)
