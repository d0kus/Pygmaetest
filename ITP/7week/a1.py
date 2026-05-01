#snipA rel-inheritance, because cat is an animal
#snipB rel-compliance, because car has an engine
#snipC rel-association,because course uses students
#snipD rel between shape and rectangle - inheritance, between rectangle and square - inheritance

#Task2A
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def describe(self):
        return f'{self.brand} — top speed {self.speed} km/h'

class ElectricCar(Car):           # 1. inherit from Car
    def __init__(self, brand, speed, battery):
        Car.__init__(self, brand, speed)   # 2. call parent __init__
        self.battery_capacity = battery             # 3. store battery

    def describe(self):
        base = Car.describe(self)               # 4. reuse parent method
        return base + f', battery {self.battery_capacity} kWh'

ec = ElectricCar('Tesla', 250, 100)
print(ec.describe())
print()

#Task2B
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def info(self):
        return f'"{self.title}" by {self.author}'

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []         # 1. start with empty list

    def add_book(self, title, author):
        new_book = Book(title, author)  # 2. create Book here
        self.books.append(new_book)               # 3. add to list

    def show_catalog(self):
        for book in self.books:                       # 4. iterate books
            print(book.info())

# Test
lib = Library('City Library')
lib.add_book('1984', 'Orwell')
lib.add_book('Dune', 'Herbert')
lib.show_catalog()
print()

#Task2C
class Classroom:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
    def info(self):
        return f'Room {self.room_number} (capacity: {self.capacity})'

class Teacher:
    def __init__(self, name):
        self.name = name
        self.classroom = None    # 1. no classroom yet

    def assign_room(self, room_obj):  # 2. receive Classroom object as parameter
        self.classroom = room_obj     # 3. store reference

    def schedule(self):
        if self.classroom:
            return f'{self.name} teaches in {self.classroom.info()}'
        return f'{self.name} has no room assigned'

# Test — objects created independently
room = Classroom('C1.354', 30)
teacher = Teacher('Daniyar')
teacher.assign_room(room)
print(teacher.schedule())
print()

#Task3 ScenarioC

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class MedicalRecord:
    def __init__(self):
        self.diagnosis = "No"
        self.history = []
    def add_entry(self, entry):
        self.history.append(entry)

class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.medical_record = MedicalRecord()

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date

    def print_summary(self):
        print(f'Date: {self.date}')
        print(f'Doctor: {self.doctor.name}, speciality: {self.doctor.specialization}')
        print(f'Patient: {self.patient.name}, ID: {self.patient.patient_id}')

dr_house = Doctor("Gregory House", 45, "Diagnostic Medicine")
ivan = Patient("Ivan Ivanov", 30, "PAT-777")
meeting = Appointment(dr_house, ivan, "2026-04-28 10:00")
meeting.print_summary()
print()

#Task4
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return self.damage

    def __str__(self):
        return f'{self.name} has {self.damage} damage'

class Sword(Weapon):
    def __init__(self, name, damage, bonus_dmg):
        super().__init__(name, damage)
        self.bonus_dmg = bonus_dmg

    def attack(self):
        base = super.attack()
        return base + self.bonus_dmg

    def __str__(self):
        return f'{self.name} has {self.damage} base damage and {self.bonus_dmg} bonus damage'

class Inventory():
    def __init__(self):
        self.weapons = []

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def show(self):
        for weapon in self.weapons:
            print(weapon)

class Hero:
    def __init__(self, name):
        self.inventory = None
        self.name = name

    def set_inventory(self, inventory):
        self.inventory = inventory

    def fight(self):
        self.inventory.show()

inv = Inventory()
inv.add_weapon('Excalibur', 50, 20)
inv.add_weapon('Dagger', 15, 5)
hero = Hero('Arthur')
hero.set_inventory(inv)
hero.fight()

        



