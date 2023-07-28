a=89
print(type(a)) #int
b=12j
print(type(b)) #complex
#prints the datatype of the variable

#lists- ordered chanageable and can have duplicates,can contain multiple datatypes 
# use []
x=[1,2,3,4,3]
print(type(x)) #list
x.append(5)#adds value
x.insert(0,7)#adds value
x.pop(4) #removes from list 
print(x)  #access list 
print(len(x)) #length of the list
#access list items 
print(x[2])# 3 item
print(x[-1])#last item 
print(x[-2])# second last item
#accessing a range of items 
print(x[1:3])#The search will start at index 1 (included) and end at index 3 (not included).
print(x[:3])#Returns the items from the beginning to, but NOT including, index 3
print(x[2:])#Returns the items from index 2 to the end
print(x[-2:])#Returns the items from index -2 to the end
print(x[:])#Returns a copy of the list
print(x[::-1])#reverses the list
print(x[::-2])#reverses the list
print(x[::-2])#reverses the list
print(x[::-1])#reverses the list

#tuples- ordered chanageable and can have duplicates
#Tupes - store items in a single variable 
#can contain multiple datatypes
#use ()
y=(1,2,3,4,5,5)
print(type(y)) #tuple
print(y)
print(len(y))#length
# tuple with mixed datatypes
my_tuple_1 = (1, "Hello", 3.4)
print(my_tuple_1)
print(type(my_tuple_1))
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
print(type(my_tuple))
#access tuples 
print(y[2]) #index 2
print(y[-1])# last index
#add items to tuple
c=list(y) #first convertss into a list 
c.append(6)
y=tuple(c)#then convert back into tuple
print(y)
#add two tuples 
laptops =('dell','hp','acer')
Laptop=('macbook')
laptops += Laptop
NS= laptops+Laptop
print(laptops)
print(NS)
 #loops
for x in y:
  print(x) #prints out all the values in vertical list

#Sets=store multiple items in asingle variable
#unchangeable but can add and remove
#no duplicates
#uses {}

s={1,2,3,4,5}
print(s)
print(type(s))
print(len(s))

print(2 in s)# accessing item in set 
s.add(6)#adding item
print(s)
s.remove(2)# removing item in set
print(s)
#adding 2 sets
set1={9,8,7,0}
set2=s.union(set1)
print(set2)