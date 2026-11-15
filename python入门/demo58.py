#面向对象之多态
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):#传入Animal类型的对象
    animal.speak()

dog=Dog()
cat=Cat()
make_noise(dog)
make_noise(cat)


#演示抽象类
class AC:
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_f(self):
        pass

class Media_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_f(self):
        print("美的空调左右摆风")

class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_f(self):
        print("格力空调左右摆风")

def cool(ac:AC):
    ac.cool_wind()

media=Media_AC()
gree=Gree_AC()

cool(media)
cool(gree)