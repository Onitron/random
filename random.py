import random 
events=["pile","face"]
seç=input("enter pile or face ")
if random.choice(events)==seç:
    print("you won!")
else:
    print("you lost!")

