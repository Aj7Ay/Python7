mydict={1:"Ajay", 2:"Ciri", 3:"panda", 4:"Rabbit", 5:"adhivik", 5:"Atulyamaya"}   #duplicate values will overwrite
print(mydict)
print(mydict[1])        #returns first key value 
print(len(mydict))
dict1 = {"brand": "Ford","electric": False,"year": 1964,"colors": ["red", "white", "blue"]} 
print(dict1)            #The values in dictionary items can be of any data type
print(type(mydict))
print(type(dict1))
x = dict1["brand"]
print(x)             #displays key value of brand    
x = mydict.get(2)       #using .get()
print(x)
x = mydict.keys()
print(x)              #returns keys only #before the change
mydict["6"] = "Ice cream"
print(x)               #after change 
x=mydict.values()      #returns only values 
print(x)
print(dict1)
dict1["year"]=2020                                  #replaces year with 2020
print(dict1)
x= mydict.items()
print(x)
if "model" in mydict:
  print("Yes, 'model' is one of the keys in the mydict dictionary")        #it will not display coz its not in dict
if "brand" in dict1:
  print("Yes, 'brand' is one of the keys in the dict1 dictionary")      #if brand is there in dict it will display yes 
dict1.update({"year": 2023})
print(dict1)  
dict1.pop("year")          #removes the item with specified key
print(dict1)
print(mydict)
mydict.popitem()               #removes last item from dict
print(mydict)
del dict1["electric"]   #removes the item with the specified key name
print(dict1)
for x in mydict:
    print(x)              #Print all key names in the dictionary, one by one
for x in mydict:
    print(mydict[x])       #Print all values in the dictionary, one by one
for x in dict1.values():
  print(x)                 # use the values() method to return values of a dictionary
for x, y in mydict.items():
  print(x, y)               #Loop through both keys and values, by using the items() method
dict2 = mydict.copy()
print(dict2)               #copy of a dictionary with the copy() method
myfamily = {"child1" : {"name" : "A","year" : 1999},"child2" : {"name" : "B","year" : 2004},}  #nested dict
print(myfamily)
ajdict={"mydict":mydict, "dict1": dict1}
print(ajdict)                        #adding two dict into one
ajdict.clear()
print(ajdict)
del ajdict
print(ajdict)    