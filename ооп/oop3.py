class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @staticmethod
    def total_people():
        print(f"Всего создано {Person.count} экземпляров класса Person")

person1 = Person("Алиса")
person2 = Person("Женя")
person3 = Person("Настя")
Person.total_people()