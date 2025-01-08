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
