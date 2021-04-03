i=int(input("enter a number"))
num=i
list=[]
while i>0:
    number=int(input("enter a number"))
    list.append(number)
    i-=1
print(list) 
odd_number=0
even_number=0
negative_number=0
zero=0
j=num-1
while j>=0:
    if list[j]>0:
        positive_number+=1
    if list[j]<=0:
        negative_number+=1
    if list[j]==0:
        zero+=1
    if list[j]%2==0:
        even_number+=1
    else:
        odd_number+=1
    j+=1
print("even_number")                            
print("odd_number")
print("positive_number")
print("negative_number")
print("zero")