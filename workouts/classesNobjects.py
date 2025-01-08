#Exercise 1 / 
'''class laptop:
    price = ""
    model = ""
    ram = ""

hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price = 50000
dell.price = 60000
lenovo.price = 70000

print(hp.price)
print(dell.price)
print(lenovo.price)'''

# Exercise 2

class laptop:
    def __init__(self):
        self.brand = ""
        self.ram = ""
        self. storage = ""
    def display(self):
        print("The Brand name is: " + self.brand)
        print("The Ram capacity is: " + self.ram)
        print("The Storage capacity is: " + self.storage + "\n")

hp=laptop()
dell=laptop()
lenovo=laptop()
        
hp.brand = "HP"
hp.ram = "8 gb"
hp.storage = "512 gb"

dell.brand = "Dell"
dell.ram = "16 gb"
dell.storage = "128 gb"

lenovo.brand = "Lenovo"
lenovo.ram = "4 gb"
lenovo.storage = "250 ssd"

        
hp.display()  
dell.display()  
lenovo.display()

# Exercise 3 
class student:
    def __init__(self):
        self.name=""
        self.regnum=""

    def display(self):
        print("Student Name: "+self.name)
        print("Register Number: " + self.regnum + "\n")

john = student()
aldrige = student()

john.name = "John"
john.regnum= "15987"

aldrige.name= "Aldrige"
aldrige.regnum= "184653"

john.display()
aldrige.display()

#Exercise 4 

class fruit:
    def __init__(self,color):
        self.col=color

apple=fruit("red")
print(apple.col)

# Exercise 5

class teacher:
    def __init__(self,name,register):
        self.nam = name
        self.reg = register

    def display(self):
        print("Name of teacher: " + self.nam)
        print("Register of teacher: " + self.reg)

t1 = teacher("Aldrige", "12345")
t2 = teacher("Alister", "16546")

t1.display()
t2.display()

# Exercise 6 / Calculator

class calculator:
    def add(self,a,b):
        print(a+b)

    def sub (self,a,b):
        print(a-b)

    def mul (self,a,b):
        print(a*b)

    def div (self,a,b):
        print(a/b)

number=calculator()

number.add(1,2)
number.sub(5,6)
number.mul(4,8)
number.div(10,2)