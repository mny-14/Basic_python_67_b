#
# Part : Python Class and object
#

#Buile class
class Myclass :
    x = 5

object1 = Myclass()
print("Object1 = " ,object1.x)
object2 = Myclass()
print("Object2 = " ,object2.x)




class SpyXFamily :
    def __init__(self , name_f , age_f) :
        self.name = name_f
        self.age = age_f
    

    def __str__(self) :
        return f" {self.name}  - {self.age}"
    

    def sayHi(self , last_name = "Forger") :
        print(f"Hey brun what 'sup {self.name} {last_name}")

        
p1 = SpyXFamily("Anya" , 8)
print(p1.name , p1.age)
print(p1)
p1.sayHi() 



p2 = SpyXFamily("Dasmond" , 8)
print(p2.name , p2.age)
p2.sayHi("Dasmond")




class car :
    def __init__(self, boby_color, engine_size) :
        self.wheels = 4
        self.window = 4
        self.window_front = 1
        self.window_back = 1
        self.boby_color = boby_color
        self.engine_size = engine_size


    def push_window_button(self):
        # some window
        pass


    def pop_window_butoon(self) :
        #  do something
        pass

    def calspeed(self):
        return self.engine_size * 1000
    
    def turnOnFrontLight(self , status = "off") :
        if status == "On":
            # do somthing
            pass
        else:
            # do somthing
            pass

    
        