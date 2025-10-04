set_num1 = {1,2,3,23,45}
set_num2 = {1,2,9,67}
# ans = set_num1+set_num2
# print(ans)

ans = list(set_num1) + list(set_num2)
print(ans)  

ans = set_num1 | set_num2
print(ans)   

ans = set_num1.union(set_num2)
print(ans)  


