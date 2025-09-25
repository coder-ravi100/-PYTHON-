#REVERSE STRING LOGIC
name = "Ravi"
total_len = len(name)
half_len = total_len // 2
print(half_len)
first_part = name[:half_len] #matlab string ke start se half_len tak ka part
last_part = name[half_len:] #matlab half_len se end tak ka part
print(f"First Part {first_part} Last {last_part}")
final_str = last_part + first_part #Yaha hum string ko ulta karke half-half swap kar rahe hain
print(f"final Result {final_str}")
#OUTPUT : viRa

word = "Ravi"
name = word[-2] + word[-1] + word[0:2]
print(name)