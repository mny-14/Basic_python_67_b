# #Part : Python Function
#


def myFunction():
    i = 1
    while i <= 3:
        print("Hello World " , i)
        i+=1

myFunction()
myFunction()



#parameter
def myName(name):
    print("My name is "  + name )
myName("Anya")
myName("Loid")

def myFullName(first_name = "Unknown" , Last_name = "Forger"):
    print("My name is "  + first_name + " " + Last_name )
myFullName("Anya")
myFullName("Bond","Forger")
myFullName("Yor ","Forger")

myFullName(Last_name = "Forger" , first_name = "LOid") #เมื่อต้องการสลับตำแหน่ง



def myFruit(fruits):
    for fruit in fruits :
        print(fruit)

fruits = ["Apple" , "banana" , "coconut"]
myFruit(fruits)


def redpotion(hp):
    return hp + 50
print("Hp :" , redpotion(100))
print("Hp :" , redpotion(30))