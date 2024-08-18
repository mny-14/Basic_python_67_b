this_list = ["apple" , "banana" ,"cocnut" , "apple" , "banana"]
print(this_list)
print(type(this_list))
print(len(this_list))

print(this_list[2])

this_list.append("cherry")
print(this_list,len(this_list))
this_list.insert(1 , "orange")
print(this_list,len(this_list))



this_list2 = ["apple" , "banana" ,"cocnut" , "apple" , "banana"]
this_list3 = ["mango" , "pinapple" ,"grape"]

this_list2.extend(this_list3)
print(this_list2, len(this_list2))


this_list4 = ["apple" , "banana" ,"cocnut" , "apple" , "banana"]
this_list4.remove("banana")
print(this_list4, len(this_list4))



this_list5 = ["apple" , "banana" ,"cocnut" , "apple" , "banana"]
this_list5.pop(2)
print(this_list5, len(this_list5))





this_list6 = ["apple" , "banana" ,"cocnut" , "apple" , "banana"]
del this_list6[1]
print(this_list6, len(this_list6))


this_list6.clear()
print(this_list6, len(this_list6))





del this_list5



this_list7 = ["orang" , "mangu" ,"kiwi" , "pinapple" , "banana"]
this_list7.sort()
print(this_list7, len(this_list7))



this_list8 = ["orang" , "mangu" ,"kiwi" , "pinapple" , "banana"]
this_list8.remove("banana")
print(this_list8, len(this_list8))


list1 = ["a" , "b" , "c"]
list2 = ["1" , "2" , "3"]
list3 = list1 + list2
print(list3)






#part : tuple


#



this_tuple = ("apple" , "banana" , "coconat")
print(this_tuple)
print(type(this_tuple))
print(len(this_tuple))


print(this_tuple[0])



this_tuple2 = ("apple" , "banana" , "coconat")
this_tuple3_list = list(this_tuple2)
print(this_tuple3_list, type(this_tuple3_list))
this_tuple4 = tuple (this_tuple3_list)
print(this_tuple4, type(this_tuple4))


this_tuple5 = ("apple" , "banana" ,  "coconat")
this_tuple6_list = list(this_tuple5)
this_tuple6_list.append("durian")
this_tuple7 = tuple (this_tuple6_list)
print(this_tuple7 , type(this_tuple7))






# part python set 

#   




this_set = {"apple " , "coconut" , "banana"}

print(this_set)
print(type(this_set))
print(len(this_set))


for x in this_set :
    print(x)


this_set2 = {"apple " , "coconut" , "banana"}
this_set2.add("durian")
print(this_set2, type(this_set2))
this_set2.remove("coconut")
print(this_set2, type(this_set2))



this_set3 = {"apple " , "coconut" , "banana"}

this_set4 = {"durian " , "grape"}
this_set3.update(this_set4)
print(this_set3, type(this_set3))





this_set5 = {"apple " , "coconut" , "banana"}

this_set6 = {"durian " , "grape"}

this_set7 = {1, 2,3}
this_set8 = this_set5 | this_set6 | this_set7
print(this_set8, type(this_set8))









# part : dictionary

# 






THIS_dict = {
    "brand " : "Ford" ,
    "model" : "Rapter",
    "year" : "2024"


}

print(THIS_dict)
print(type(THIS_dict))
print(len(THIS_dict))



print(THIS_dict["brand "])
print(THIS_dict.get("year"))
print(THIS_dict.keys())

THIS_dict["year"] = "1998"
print(THIS_dict)
THIS_dict.update({

    "year" : "1998"
    ,"model" : "Mustang"
})


THIS_dict ["color"] = "Red"
print(THIS_dict)

del THIS_dict ["year"]
print (THIS_dict)


THIS_dict.clear()
print(THIS_dict, type(THIS_dict))
del THIS_dict



THIS_dict2 = {
    "brand " : "TOYOTA" ,
    "model" : "YARIS",
    "year" : "2016"


}


THIS_dict3 = {
    "brand " : "HONDA" ,
    "model" : "CIVIS",
    "year" : "2024"


}


THIS_dict4 = {
    "brand " : "LAMBORGHINI" ,
    "model" : "HURACAN",
    "year" : "2019"


}

my_car ={
    "car1" : THIS_dict2 ,
    "car2" : THIS_dict3 ,
    "car3" : THIS_dict4 ,




}


print(my_car, len(my_car))
print(my_car["car2"]["model"])

git config --global user.name "mny-14"
git config --global user.email "6749010039@phuketvc.ac.th"




git add .
git