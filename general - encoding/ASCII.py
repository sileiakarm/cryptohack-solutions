int_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag_list = ['']*len(int_list)
j=0
for i in int_list:
    flag_list[j]=chr(i)
    j+=1
print(''.join(flag_list))