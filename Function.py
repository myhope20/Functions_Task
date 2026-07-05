#functions
def name():
    print("Hello")
name()

#Parameters
def Mohan(name):
    print("Mohan",name)
Mohan("Raj")

#Parameters
def Hey_Come(name):
    print("Hey",name)
Hey_Come("Mohan")

#Arguments
def mohan(name):
    print("Mohan",name)
mohan("Raj") # calling function with argument

#Returning Values
def add(a,b):
    return a+b # Used to add two numbers and return the result
result = add(5,10) # Used to store the returned value in a variable
print(result)

#default arguments
def Mohan(name="Mohanraj"):
        print(name)
Mohan("Raj")

#Keyword Arguments
def mohan(name="Mohanraj", age=20):
    print(name,age)
mohan()

#Variable Length Arguments
def mohan(*num):
    print(sum(num))
mohan(10,20,30,40,50)


#Keyword Variable Length Arguments
def Numbers(**num):
    print(num)
Numbers(a=1,b=2,c=3)

#print key and values
def mohan(**num):
    for a,b in num.items():
        print(a,":",b)
mohan(a=1,b=2)
