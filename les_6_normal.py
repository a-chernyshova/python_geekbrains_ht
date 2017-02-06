# -*- coding: utf-8 -*-
#normal
# Задание-1: # Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.
class Person:
    def __init__(self, name, second_name, age, status):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.status = status
        self.kids = []

    def full_name(self):
        return self.name + ' ' + self.second_name

class Student(Person):
    def __init__(self, name, second_name, age, class_team):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.parents = []
        self.class_team = class_team

    def add_parent(self, person):
        if len(self.parents)<2:
            self.parents.append(person)
            person.kids.append(self)
        else:
            print('Не может быть более двух родителей')

    def print_parents(self):
        print('Parents of: ', self.name)
        for parent in self.parents:
            print(parent.name, parent.second_name)


class Teacher(Person):
    def __init__(self, name, second_name, age, subject, classes, school):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.subject = subject
        self.classes = classes
        self.school = school

    def info(self):
        return self.name + ' ' + self.second_name + ', teacher of ' + self.subject

    def classes_list(self):
        _list = ''
        for i in self.classes:
            _list += str(i) + ', '
        return _list

class Klass:
    def __init__(self, name, subjects, supervisor, school):
        self.name = name
        self.student_list = []
        self.subjects = subjects
        self.supervisor = supervisor
        self.school = school

    def amount_of_students(self):
        return len(self.student_list)

    def print_subjects(self):
        print('List of subject in:', self.name)
        for i in self.subjects:
            print(i)

    def teachers_list(self):
        print('List of teachers in', self.name)
        for teacher in School.teacher_list:
            if teacher.subject in self.subjects:
                print(teacher.name, teacher.second_name)

    def add_student(self, student):
        self.student_list.append(student)

    def print_students(self):
        print('List of students:')
        for student in self.student_list:
            print(student.name, student.second_name)

class School:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.teacher_list = []

    def has_teacher(self, subject):
        for teacher in self.teacher_list:
            if teacher.subject == subject:
                return True
        return False

    def add_teacher(self, teacher):
        if not self.has_teacher(teacher.subject):
            self.teacher_list.append(teacher)

    def show_teacher_list(self):
        print('Teacher list:')
        for i in self.teacher_list:
            print(i.subject, i.name, i.second_name)

s1 = Student('Anton', 'Petrov', 13, '5 A')
s2 = Student('Boris', 'Ivanov', 14, '5 A')
p2 = Person('Ana', 'Petrova', 36, 'married')
p1 = Person('Mikle', 'Petrov', 40, 'married')
p3 = Person('Alex', 'Petrov', 20, 'single')
t1 = Teacher('Rimma', "Men'shikova", 47, 'mathematic', ['5 A', '7 A', '10 A'], 'NSSH')
k1 = Klass('5 A', ['mathematic', 'literature', 'biology'], 'Natalia Aminova', 'NSSH')
sc1 = School('NSSH', 'bla bla adress')
t2 = Teacher('Alla', "Men'shikova", 45, 'mathematic', ['5 A', '7 A', '10 A'], 'NSSH')
t3 = Teacher('Inna', "Men'shikova", 47, 'biology', ['5 A', '7 A', '10 A'], 'NSSH')
# sc1.add_teacher(t1)
# sc1.show_teacher_list()
# sc1.add_teacher(t2)
# sc1.show_teacher_list()
# sc1.add_teacher(t3)
# sc1.show_teacher_list()
# s1.add_parent(p2)
# s1.add_parent(p1)
# s1.add_parent(p3)
# s1.print_parents()
k1.print_subjects()
print(t1.info())
k1.add_student(s1)
k1.print_students()

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе