from zoo import *
animals = [Bird("Liot",4,"2m"), Mammal("Kaha",9,"1,5m"), Reptile("Tissa",2,"black")]
for animal in animals:
    animal.make_sound()

admin = Zoo()
first_bird  = admin.add_animal("Kali","9 months","1 m", "bird")
#admin.add_employee("Стас", 22, "Zookeeper")

# print(admin.animals_store)
# print(admin.employee_store)


admin.animals_store[4].make_sound()
admin.employee_store[2].feeding()

