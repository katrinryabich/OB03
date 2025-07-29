class Engine():
    def start(self):
        print("двигатель запущен")

    def stop(self):
        print("двигатель остановлен")

class Car():
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

first_car = Car()
first_car.start()
first_car.stop()



class Teacher():
    def teach(self):
        print("преподаватель учит")

class School():
    def __init__(self, new_teacher):
        self.teacher = new_teacher

    def start_lesson(self):
        self.teacher.teach()

first_teacher = Teacher()
school = School(first_teacher)


class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав")

class Cat(Animal):
    def make_sound(self):
        print("мяу")

class Cow(Animal):
    def make_sound(self):
        print("муу")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()
