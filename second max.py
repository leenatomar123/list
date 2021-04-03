number=[50,40,23,70,56,12,5,10,7]
max=number[0]
secondmax= number [1]
i=0
while i<len(number):
    if number[i]>max:
      secondmax=max
      max=number[i]
    elif number[i]>secondmax:
        secondmax=number[i]
    i=i+1
print("second highest number is",secondmax)   