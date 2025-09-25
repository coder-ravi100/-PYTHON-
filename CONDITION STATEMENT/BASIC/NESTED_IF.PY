#NESTED IF - ELIF - (IF-ELSE)
#EK CONDITION KE ANDER DUSARI  CONDITION CHECK KARNI HO
'''
IF(CONDITION 1)

    IF(CONDITION 2)
        //BLOCK OF CODE
    ELSE:
    BLOCK OF CODE

ELSE:
    BLOCK OF CODE

'''
#PROGRAM TO CHECK AGE AND THEN DONATE BLOOD
age = int (input ("Enter The Age :"))
weight = int (input ("Enter The Weight :"))

if age >= 18:

    if weight >=55:

        print("You can Donate Blood")

    else: #THIS LINE FOR WEIGHT MATCH

        print("Cannot Donate Blood Due To Underweight")

else: #THIS LINE FOR AGE MATCH

    print("Cannot Donate Blood Due To Age")