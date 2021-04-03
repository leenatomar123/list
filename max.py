number=[50,40,23,70,56,12,5,10,7]
index=0
max=number[0]
while index<len(number):
    m=number[index]
    if m>max:
        max=m
    index+=1
print("maximum num is",max)        