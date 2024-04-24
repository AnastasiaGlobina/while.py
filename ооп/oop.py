class Note:
    def __init__(self, text):
        self.text = text
        self.count = 0
        self.iscompleted = False

    def upcount(self, increment=1):
        self.count += increment

    def reset_count(self):
        self.count = 0

note1 = Note("Задача 1")

print(note1.__dict__)

note1.upcount()
print(note1.count)

note1.reset_count()
print(note1.count)