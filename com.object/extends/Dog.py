import Animal


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
dog=Dog()
dog.run()
