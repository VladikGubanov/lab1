def print_students(students):
    print(u"Имя".ljust(10), u"Фамилия".ljust(10),
          u"Экзамены".ljust(50), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(10),
              student["surname"].ljust(10), str(student["exams"]).ljust(50),
              str(student["marks"]).ljust(20))


def filter(groupmates, sb):
    id = 0
    idd = []
    for groupmate in groupmates:
        id =int( id + 1)
        ss = 0

        for mark in groupmate["marks"]:
            ss = ss + mark
        ss = ss / 3

        if ss >= sb:
            idd.append(id)
    return idd


groupmates = [
    {
        "name": "Петр",
        "surname": "Петров",
        "exams": ["Математика", "Информатика", "Физика"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Иван",
        "surname": "Иванов",
        "exams": ["Философия", "Web", "ИС"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Алексей",
        "surname": "Алексеев",
        "exams": ["Химия", "Астрономия", "Иностранный язык"],
        "marks": [5, 5, 5]
    }
]

print_students(groupmates)
print('')
sb = int(input('Введите средний балл - '))
print('')

ids = filter(groupmates, sb)

filter = []

for elem in ids:
    filter.append(groupmates[elem])

print_students(filter)
