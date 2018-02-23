class SweetPotato:
    def __init__(self):
        self.cookedLevel=0
        self.cookedString="生的"
        self.condiments=[]
    #烤地瓜
    def cook(self,time):
        self.cookedLevel+=time
        if self.cookedLevel>8:
            self.cookedString="烤糊了"
        elif self.cookedLevel>5:
            self.cookedString="熟了"
        elif self.cookedLevel>3:
            self.cookedString="半生不熟"
        else:
            self.cookedString="生的"
    def addCondiments(self,temp):
        self.condiments.append(temp)
sweetPatato=SweetPotato()
sweetPatato.cook(2)
print(sweetPatato.cookedString)
sweetPatato.cook(2)
print(sweetPatato.cookedString)
sweetPatato.addCondiments("番茄酱")
print(sweetPatato.condiments)