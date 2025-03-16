import random 
side=["pile","face"]
choice=input("enter pile or face ")
if random.choice(side)==choice:
    print("you won!")
else:
    print("you lost!")

