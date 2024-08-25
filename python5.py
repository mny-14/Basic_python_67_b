#
#Prat : Python white Loop
#



i = 1
while i < 5 :
    print ("i = ", i)
    i += 1 
    # 1 = 1 + 1


#i = i
#while i < 5 :
 #   print("i = " , i)
  #  if i == 3:
   #     continue
    #i+=1 # i = 1 + 1


i = i
while i < 5 :
    print("i = " , i)
    i+=1 # i = 1 + 1
else :
    print ("Game Over!")
        
 #
 #Part : Pythin For Loop
 # 

fruits = ["apple" , "banana" , "coconut"]

for fruit in fruits : 
    print("Fruit: " , fruit)



for fruit in fruits : 
    print("Fruit: " , fruit)
    if fruit == "banana":
        break
    

for fruit in fruits : 
    if fruit == "banana":
        break
    print("Fruit: " , fruit)


for fruit in fruits : 
    if fruit == "banana":
        continue
    print("Fruit: " , fruit)
    


for x in range (len(fruits)) :
    print("NAmber:" , x)


for x in range (5) :
    print("NAmber:" , x)
else:
    print("Game Over!")


adjs = ["red" , "blue" , "green"]
fruits = ["apple" , "banana" , "coconut"]
for adjs in adjs :
    for fruit in fruits :
        print("Fruit: " + adjs + " " + fruit)