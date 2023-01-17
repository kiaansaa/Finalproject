import random
ANIMAL = ["dog","cat","cow","tiger","elephant","jackle","deer","bear"]
NAME = ["Keshav","Avay","Avhishek","Priyansh","Nischal","ram","hari","larry"]
COLOR = ["red","blue","white","balck","orange","voilet","velvet","yellow"]

print("Password Generator")
print("\n")
print("===================")
print("\n")
count=0

while True:
    try:
        
        no_of_password = int(input ("Enter the number of passwords needed:" ))
        break
    except:
        print("Please enter a numeric value.")
print("\n")

if no_of_password < 1 or no_of_password > 24:
    print("please enter a value between 1 and 24.")
    exit()

else:
    
    for i in range(no_of_password):
    
        a = random.choice (ANIMAL)
        n = random.choice (NAME)
        c = random.choice (COLOR)
        password = a + n + c
        print('{} --> {}'.format(i+1, password))
        count +=1