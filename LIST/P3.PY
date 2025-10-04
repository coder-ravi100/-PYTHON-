#CONPREHENSION SHORT WAY / READABLE WAY / CONSICE WAY
lst_number  = [1,2,9]
lst_new_number = []
#copy into another list
for i in lst_number:
    lst_new_number.append(i)
print(lst_number)


lst_new_number = [i**5 for i in lst_new_number]
print(lst_new_number)

#WANT TO CONVERT ALL STRING INTO UPPER CASE
lst_city = ['baroda','surat','ahmedabad']
lst_upper_city = [i.upper() for i in lst_city if len(i)>5]
print(lst_upper_city)

#power and sub power 
lst_num = [1,2,3]
#output((1,1,1),(2,4,8),(3,9,27))
lst_num_ans = [(i,i**2,i**3)for i in lst_num]
print(lst_num_ans)


lst_num_sq = (i*i for i in lst_num)
print(list(lst_num_sq))