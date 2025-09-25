#escape sequnces
# Simple string
name1 = "Tops Technologies"       
print(name1)                      # Output: Tops Technologies

# Backslashes used in string → escape karna padega
name2 = "\\Tops Technologies\\"  
print(name2)                      # Output: \Tops Technologies\

# Single quotes inside single-quoted string → escape using \'
name3 = 'Tops \'Technologies\''
print(name3)                      # Output: Tops 'Technologies'

# New line character → line break karega
name4 = "Tops\nTechnologies"     
print(name4)                      # Output:
                                  # Tops
                                  # Technologies

# Tab space → 4-8 spaces between words
name5 = "Tops\tTechnologies"     
print(name5)                      # Output: Tops    Technologies

# Backspace → pehle wale character ko hata dega
name6 = "Tops\bTechnologies"     
print(name6)                      # Output: TopTechnologies

# Normal string again
name7 = "Tops Technologies"       
print(name7)                      # Output: Tops Technologies

#Use End \n
#Sep \t