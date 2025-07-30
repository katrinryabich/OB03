import json
from pathlib import Path


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



class Zookeeper():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feeding(self):
        print("Животные накормлены")

    def cleaning(self):
        print("Вольеры чисты")

    def monitoring(self):
        #Пусть функцуия будет фоново включена пока её не отключат
        print("За животными ведется наблюдение, всё спокойно.")

class Veterinarian():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def healing(self):
        print("животные здоровы")

class Zoologist():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def animal_behavior_research(self):
        print("у прадставителей разных классов могут быть разные повадки")



class Zoo():
    def __init__(self, animals_path = "animals.json", employee_path = "employee.json"):
        self.animals_path = Path(animals_path)
        self.employee_path = Path(employee_path)
        self.animals_store = self.__load_animals_store()
        self.employee_store = self.__load_employee_store()
        self.__load_animals_store()

    def __load_animals_store(self):
        if self.animals_path.exists():
            with open(self.animals_path, 'r', encoding ='utf-8') as anst:
                employee_store = json.load(anst)
                return []
        else:
            return []


    def __load_employee_store(self):
        if self.employee_path.exists():
            with open(self.employee_path, 'r', encoding='utf-8') as empst:
                return json.load(empst)
        else: return []

    def __make_animal_object(self, animal_store):
        name = animal_store["name"]
        age = animal_store["age"]
        special_attribute = animal_store["special_attribute"]
        animal_type = animal_store.get("type")
        if animal_type == "Bird":
            return Bird(name, age, special_attribute)
        elif animal_type == "Mammal":
            return Mammal(name, age, special_attribute)
        elif animal_type == "Reptile":
            return Reptile(name, age, special_attribute)
        else: raise ValueError(f"Неудалось установить тип животного: {animal_type}")


    def make_employee_object(self, employee_store):
        name = employee_store["name"]
        age = employee_store["age"]
        profession = employee_store["profession"]
        emplioyee_type = employee_store.get("profession")
        if emplioyee_type == "Vet":
            return Veterinarian(name, age)
        elif profession == "Zoologist":
            return Zoologist(name, age)
        elif emplioyee_type == "Zookeeper":
            return Zookeeper(name, age)
        else:
            raise ValueError(f"Незнакомая профессия: {emplioyee_type}")
    def __save_animals_store(self):
        try:
            with open(self.animals_path,'w',encoding='utf-8') as anst:
                json.dump(self.animals_store,anst, indent=2, ensure_ascii=False)
        except Exception:
            print(f"Ошибка при сохранении")

    def __save_employee_store(self):
        try:
            with open(self.employee_path,'w',encoding='utf-8') as anst:
                json.dump(self.employee_store,anst, indent=2, ensure_ascii=False)
        except Exception:
            print(f"Ошибка при сохранении")


    def add_animal(self,name, age, special_attribute, animal_type):
        new_animal = {
            "name": name,
            "age": age,
            "special_attribute": special_attribute
        }
        self.animals_store.append(new_animal)
        self.__save_animals_store()

    def add_employee(self, name, age, profession):
        new_employee = {
            "name": name,
            "age": age,
            "profession" : profession
        }

        self.employee_store.append(new_employee)
        self.__save_employee_store()

