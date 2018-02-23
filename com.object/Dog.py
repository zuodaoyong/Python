class Dog:
    def __init__(self,name,weight,color):
        self.weight=weight
        self.name=name
        self.color=color

    def __str__(self):
        return "name:"+self.name+",weight:"+str(self.weight)+",color:"+self.color
    def bark(self):
        print(self.name,self.weight,self.color)

dog=Dog("大白",5,"黄色")
dog.bark();
print(dog)