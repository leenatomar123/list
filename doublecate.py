list=[1,2,3,4,5,1,2,4,5,6,1,2,3,4,5,5,1]
new_list=[]
i=0
while i<len(list):
    if list[i] not in new_list:
        new_list.append(list[i])
    i+=1
print(new_list)    