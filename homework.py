class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.all_rates = []
        self.aver_gr = 0
        self.grades = {}

        Student.students.append(self)

    def rate_st(self, lector, course, grade):
        if isinstance(lector, Lector) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print('Ошибка')
            return
            
    def average_grade(self):
        for k, v in self.grades.items():
            self.all_rates.extend(v)
        self.aver_gr = round((sum(self.all_rates)/len(self.all_rates)), 3)
        return self.aver_gr

    def __str__(self):
        res = str('Имя: ' + self.name + '\nФамилия: ' + self.surname
                  + '\nСредняя оценка за домашние задания: ' + str(self.average_grade())
                  + '\nКурсы в процессе изучения: ' + ", ".join(self.courses_in_progress)
                  + '\nЗавершенные курсы: ' + ", ".join(self.finished_courses))
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        if self.aver_gr < other.aver_gr:
            print(f'У {self.surname} средний бал ниже, чем у {other.surname}')
        else:
            print(f'У {self.surname} средний бал выше, чем у {other.surname}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lector(Mentor):
    lectors = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.all_rates = []
        self.aver_gr = 0
        Lector.lectors.append(self)

    def average_grade(self):
        for k, v in self.grades.items():
            self.all_rates.extend(v)
        self.aver_gr = round((sum(self.all_rates) / len(self.all_rates)), 2)
        return self.aver_gr

    def __str__(self):
        res = str('Имя: ' + self.name +
                  '\nФамилия: ' + self.surname +
                  '\nСредняя оценка за лекции: ' + str(self.average_grade()))
        return res

    def __lt__(self, other):
        if not isinstance(other, Lector):
            print('Нет такого проверяющего')
            return
        if self.aver_gr < other.aver_gr:
            print(f'У {self.surname} средний бал ниже, чем у {other.surname}')
        else:
            print(f'У {self.surname} средний бал выше, чем у {other.surname}')
        

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка!')
            return

    def __str__(self):
        res = str('Имя: ' + self.name +
                  '\nФамилия: ' + self.surname)
        return res


def av_rate_st(list_, course):
    courses = {}
    for men in list_:
        for k, v in men.grades.items():
            if k not in courses:
                courses[k] = v
            else:
                courses[k].extend(v)
    av_grade_courses_std = {c: round(sum(g) / len(g), 2) for c, g in courses.items()}
    if course in av_grade_courses_std:
        print(f'У студентов по курсу {course} средний бал {av_grade_courses_std[course]}')
    else:
        print('У студентов нет такого предмета')


def av_rate_lct(list_, course):
    courses = {}
    for men in list_:
        for k, v in men.grades.items():
            if k not in courses:
                courses[k] = v
            else:
                courses[k].extend(v)
    av_grade_courses_lct = {c: round(sum(g) / len(g), 2) for c, g in courses.items()}
    if course in av_grade_courses_lct:
        print(f'У лекторов по курсу {course} средний бал {av_grade_courses_lct[course]}')
    else:
        print('У лекторов нет такого предмета')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GitHub']
best_student.finished_courses += ['Math']

studentOne = Student('Petr', 'Volkov', 'men')
studentOne.courses_in_progress += ['Python']
studentOne.courses_in_progress += ['GitHub']

studentTwo = Student('Vasya', 'Rogov', 'men')
studentTwo.courses_in_progress += ['Python']
studentTwo.courses_in_progress += ['English']
studentTwo.finished_courses += ['Math']
 
cool_review = Reviewer('Some', 'Buddy')
cool_review.courses_attached += ['Python']
cool_review.courses_attached += ['GitHub']

reviewerOne = Reviewer('Larisa', 'Ivanovna')
reviewerOne.courses_attached += ['Python']
reviewerOne.courses_attached += ['GitHub']
reviewerOne.courses_attached += ['English']

best_lector = Lector('Hello', 'Everybody')
best_lector.courses_attached += ['Python']
best_lector.courses_attached += ['GitHub']

lector1 = Lector('Ivan', 'Ivanov')
lector1.courses_attached += ['Python']
lector1.courses_attached += ['GitHub']

lector2 = Lector('Leonid', 'Gusev')
lector2.courses_attached += ['Python']
lector2.courses_attached += ['English']

print('Проверяем работу методов')
print()
cool_review.rate_hw(best_student, 'Python', 10)
cool_review.rate_hw(best_student, 'GitHub', 7)
cool_review.rate_hw(studentOne, 'Python', 10)
cool_review.rate_hw(studentOne, 'Python', 6)
cool_review.rate_hw(studentOne, 'GitHub', 8)
cool_review.rate_hw(studentTwo, 'Python', 9)
# cool_review.rate_hw(studentTwo, 'English', 10)

reviewerOne.rate_hw(best_student, 'Python', 7)
reviewerOne.rate_hw(best_student, 'GitHub', 8)
reviewerOne.rate_hw(studentOne, 'Python', 3)
reviewerOne.rate_hw(studentOne, 'Python', 7)
reviewerOne.rate_hw(studentOne, 'GitHub', 9)
reviewerOne.rate_hw(studentTwo, 'Python', 9)
reviewerOne.rate_hw(studentTwo, 'English', 10)


studentOne.rate_st(lector1, 'Python', 10)
studentOne.rate_st(lector1, 'GitHub', 8)
studentOne.rate_st(lector2, 'Python', 8)
studentOne.rate_st(best_lector, 'Python', 8)
studentOne.rate_st(best_lector, 'GitHub', 9)

studentTwo.rate_st(lector1, 'Python', 9)
studentTwo.rate_st(lector2, 'Python', 10)
studentTwo.rate_st(lector2, 'English', 10)
studentTwo.rate_st(best_lector, 'Python', 7)

best_student.rate_st(lector1, 'Python', 9)
best_student.rate_st(lector1, 'GitHub', 7)
best_student.rate_st(lector2, 'Python', 10)
best_student.rate_st(best_lector, 'Python', 7)
best_student.rate_st(best_lector, 'GitHub', 10)
 
print(best_student)
print(studentOne)
print(studentTwo)
print()
print(best_lector)
print(lector1)
print(lector2)
print()
best_lector.__lt__(lector1)
best_lector.__lt__(lector2)
lector1.__lt__(lector2)
print()
best_student.__lt__(studentOne)
studentOne.__lt__(studentTwo)
studentTwo.__lt__(studentOne)

av_rate_st(Student.students, 'English')
av_rate_st(Student.students, 'Python')
av_rate_st(Student.students, 'GitHub')
av_rate_lct(Lector.lectors, 'English')
av_rate_lct(Lector.lectors, 'Math')
