class Animal():
    def __init__(self, name, age):
        pass
    
    def make_sound(self):
        pass
    
    def eat(self):
        pass
    
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print("Птицы издают множество разнообразных звуков: щебетание, трели, свист, трели, карканье, барабанный бой")

    def eat(self):
        print("В общем, птицы могут питаться семенами, ягодами, фруктами, насекомыми, мелкими млекопитающими, рыбой, яйцами, почками, личинками и др.")

class Mammal(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        print("Среди издаваемых млекопитающими звуков наиболее характерны рёв, стон, мяуканье, шипенье")

    def eat(self):
        print("Млекопитающие могут быть хищниками, травоядными, всеядными")

class Reptile(Animal):
    def __init__(self, name, age, scales_color):
        super().__init__(name, age)
        self.scales_color = scales_color

    def make_sound(self):
        print("Звуки, издаваемые рептилиями и амфибиями, могут быть весьма разнообразными и выполнять различные функции")

    def eat(self):
        print("Есть рептилии со смешанным типом питания, которые употребляют как растительную, так и животную пищу")


