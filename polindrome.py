place=["n","i","t","i","n"]
i=0
j=len-1
list1=[]
while i>=0:
    if place[i]==place[j]:
        list1.append(place[i])
        j=j+1
    i-=1    
    print(list1)
    if list1==place:
        print("it is polindrome")
    else:
        print("it is not polindrome")    
