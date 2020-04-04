class animal():
    def eat(self):
        print("Eating Eating!")

class cat(animal):
    def setName(self,text):
        self.name = text
        print("FUCK", self.name)
    def eat(self):
        print("Meoww !",self.name)
cat1 = cat()
cat1.setName("TJ")
cat1.eat()
