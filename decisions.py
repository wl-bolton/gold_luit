import random

number = random.randint(0,10)

print(number)

thresh = 5
if(number > thresh):
    print("Big number")
elif(number < thresh):
    print("Small number")
else:
    print("Number is", str(thresh)) 