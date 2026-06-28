import json
import os

class OpenCourse:
    @staticmethod
    def open():
        try:
            if not os.path.exists('courses.json'):
                print('File of courses is not defined!')
                answer = input('Give your permission to create this file(y/n): ').lower().strip()
                if answer == 'y':
                    with open('courses.json', 'w', encoding='utf-8') as f:
                        return []
                else:
                    print('Bye bye!')
                    exit()
            else:
                with open('courses.json', 'r', encoding='utf-8') as f:
                    reader = json.load(f)
                return reader
        except KeyboardInterrupt:
            print('\nBye bye!')
            exit()

class OpenStudent:
    @staticmethod
    def open():
        try:
            if not os.path.exists('students.json'):
                print('File of students is not defined!')
                answer = input('Give your permission to create this file(y/n): ').lower().strip()
                if answer == 'y':
                    with open('students.json', 'w', encoding='utf-8') as f:
                        return []
                else:
                    exit()
            else:
                with open('students.json', 'r', encoding='utf-8') as f:
                    reader =json.load(f)
                return reader
        except KeyboardInterrupt:
            print('Bye bye!')
            exit()

class WriteCourse:
    @staticmethod
    def write(ml):
        try:
            with open('courses.json', 'w', encoding='utf-8') as f:
                json.dump(ml, f, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            print('File of courses does not exist!')
            exit()

class WriteStudent:
    @staticmethod
    def write(student):
        try:
            with open('students.json', 'w', encoding='utf-8') as f:
                json.dump(student, f, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            print('File of students does not exist!')
            exit()

class FindIdx:
    def idx_st(self, students, obj):
        for idx, stud in enumerate(students):
            if stud['Name'] == obj.name and stud['Course'] == obj.course:
                return idx
    def idx_cr(self, courses, obj):
        for idx, course in enumerate(courses):
            if course['Name'] == obj.name:
                return idx

class Course:
    def __init__(self, name, students=None, total=0):
        self.__name = name
        self.__students = students
        self.__total = total
    @property
    def name(self):
        return self.__name
    @property
    def students(self):
        return self.__students
    @students.setter
    def students(self, st):
        self.__students = st
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, n):
        self.__total = n
    @staticmethod
    def check_course_name(course, courses):
        for c in courses:
            if c['Name'] == course:
                obj = Course(c['Name'], c['Students'], c['Students total'])
                return True, obj
        return False, None
    def add_course(self, course, courses):
        courses.append(course.to_dict(course))
        print('Course is added!')
    def avg_score(self, students, course):
        ml = []
        for stud in students:
            if stud['Course'] == course:
                if stud['Grades'] == None:
                    ml.append(0)
                else:
                    for value in stud['Grades']:
                        ml.append(value)
        avg = sum(ml) // len(ml)
        print(f'Average score: {avg}')
        return
    def to_dict(self, course):
        return {'Name': course.name,
                'Students': course.students,
                'Students total': course.total}
    def __str__(self):
        return f'Name: {self.__name}\nStudents: {self.__students}\nStudents total: {self.__total}'

class Student:
    def __init__(self, name, course, grades=None):
        self.__name = name
        self.__course = course
        self.__grades = grades
    @property
    def name(self):
        return self.__name
    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course):
        self.__course = course
    @property
    def grades(self):
        return self.__grades
    @grades.setter
    def grades(self, grade):
        if grade == None:
            self.__grades = grade
        if type(grade) == list:
            for g in grade:
                if g > 100 or g < 0:
                    print('Invalid input!')
                else:
                    self.__grades = grade
    @staticmethod
    def find_student(name, course, students):
        for stud in students:
            if stud['Name'] == name and stud['Course'] == course:
                obj = Student(stud['Name'], stud['Course'], stud['Grades'])
                return True, obj
        return False, None
    def add_student(self, students, obj, write_stud):
        students.append(obj.to_dict(obj))
        write_stud.write(students)
    def to_dict(self, student):
        return {'Name': student.name,
                'Course': student.course,
                'Grades': student.grades}

class Main:
    def add_course(self, courses):
        try:
            course_name = input('Enter course name: ').title().lstrip().rstrip()
            flag, obj = Course.check_course_name(course_name, courses)
            if flag:
                print('That course is exist!')
                return 
            else:
                new_course = Course(course_name)
                new_course.add_course(new_course, courses)
        except KeyboardInterrupt:
            print('\nBye bye!')
            exit()
    def search_course(self, courses):
        try:
            course_name = input('Enter course name: ').rstrip().lstrip().title()
            flag, obj = Course.check_course_name(course_name, courses)
            if flag:
                print(20 * '=')
                print(obj)
                print(20 * '=')
            else:
                print('Course does not exist!')
        except KeyboardInterrupt:
            print('Bye bye!')
            exit()
    def delete_course(self, courses):
        try:
            course_name = input('Enter course name: ').title().rstrip().lstrip()
            flag, obj = Course.check_course_name(course_name, courses)
            if flag:
                    courses.remove(obj.to_dict(obj))
                    print('Course successfully deleted!')
                    return
            else:
                print('Course does not exist!')
        except KeyboardInterrupt:
            print('Bye bye!')
            exit()
    def avg_score(self, students, courses):
        course = input('Enter course: ').title().strip()
        flag, obj = Course.check_course_name(course, courses)
        if flag:
            obj.avg_score(students, course)
        else:
            print('Course does not exist!')
    def add_student(self, students, courses, write_stud, write_course, idx):
        name = input('Enter name: ').title().rstrip().lstrip()
        course = input('Enter course: ').title().strip()
        flag, obj = Student.find_student(name, course, students)
        flag2, obj2 = Course.check_course_name(course, courses)
        if not flag2:
            print('Course does not exist!')
            return False
        if flag:
            print('Student exists!')
            return False
        obj = Student(name, course)
        obj2.total = 1 + obj2.total
        if obj2.students == None:
            obj2.students = [obj.name]
            idx_cr = idx.idx_cr(courses, obj2)
            courses[idx_cr] = obj2.to_dict(obj2)
            write_course.write(courses)
        else:
            obj2.students.append(obj.name)
            idx_cr = idx.idx_cr(courses, obj2)
            courses[idx_cr] = obj2.to_dict(obj2)
            write_course.write(courses)
        obj.add_student(students, obj, write_stud)
    def delete_student(self, students, courses, write_stud, write_course):
        name = input('Enter student name: ').title().rstrip().lstrip()
        course = input('Enter course: ').title().strip()
        flag, obj = Student.find_student(name, course, students)
        flag2, obj2 = Course.check_course_name(course, courses)
        if flag:
            students.remove(obj.to_dict(obj))
            obj2.total = obj2.total - 1
            obj2.students.remove(name)
            write_course.write(courses)
            write_stud.write(students)
            return True
        else:
            print('Student does not exist!')
            return False
    def add_grade(self, students, write_stud, idx):
        name = input('Enter student name: ').title().rstrip().lstrip()
        course = input('Enter course: ').title().strip()
        flag, obj = Student.find_student(name, course, students)
        if flag:
            idx_st = idx.idx_st(students, obj)
            while True:
                try:
                    if obj.grades == None:
                        grade = int(input('Enter a grade: '))
                        obj.grades = [grade]
                        students[idx_st] = obj.to_dict(obj)
                        write_stud.write(students)
                        return True
                    else:
                        if len(obj.grades) == 2:
                            print('Grades are full!')
                            return False
                        grade = int(input('Enter a grade: '))
                        obj.grades.append(grade)
                        students[idx_st] = obj.to_dict(obj)
                        write_stud.write(students)
                        return True
                except ValueError:
                    print('Invalid input!')
                    continue
        else:
            print('Student does not exist!')
            return False
    def delete_grade(self, students, write_stud, idx):
        name = input('Enter student name: ').title().rstrip().lstrip()
        course = input('Enter course: ').title().strip()
        flag, obj = Student.find_student(name, course, students)
        if flag:
            idx_st = idx.idx_st(students, obj)
            while True:
                try:
                    grade = int(input('Enter the grade: '))
                    if obj.grades == None:
                        print('The student does not have any grades!')
                        return False
                    elif grade in obj.grades:
                        obj.grades.remove(grade)
                        students[idx_st] = obj.to_dict(obj)
                        write_stud.write(students)
                        return True
                    else:
                        print('The student does not have such a grade!')
                        return False
                except ValueError:
                    print('Invalid input!')
                    continue
        else:
            print('The student does not exist!')
            return False
    def change_course(self, students, courses, write_stud, write_course, idx):
        name = input('Enter student name: ').title().rstrip().lstrip()
        course = input('Enter current course: ').title().strip()
        flag, obj = Student.find_student(name, course, students)
        flag2, obj2 = Course.check_course_name(course, courses)
        if flag:
            obj2.total = obj2.total - 1
            obj2.students.remove(name)
            idx2 = idx.idx_cr(courses, obj2)
            courses[idx2] = obj2.to_dict(obj2)
            while True:
                new_course = input('Enter course: ').title().strip()
                fl, ob = Course.check_course_name(new_course, courses)
                if fl:
                    ob.total = ob.total + 1
                    if ob.students == None:
                        ob.students = [name]
                    else:
                        ob.students.append(name)
                    idx_ob = idx.idx_cr(courses, ob)
                    courses[idx_ob] = ob.to_dict(ob)
                    idx1 = idx.idx_st(students, obj)
                    obj.course = new_course
                    obj.grades = None
                    students[idx1] = obj.to_dict(obj)
                    write_stud.write(students)
                    write_course.write(courses)
                    return True
                else:
                    print('That course does not exist!')
                    continue
        else:
            print('Student does not exist!')
            return False
    def change_grade(self, students, write_stud, idx):
        name = input('Enter student name: ').title().rstrip().lstrip()
        course = input('Enter course name: ').title().strip()
        flag, obj = Student.find_student(name, course, students)
        if flag:
            while True:
                try:
                    if obj.grades == None:
                        print('Grades are null, please first add the grade!')
                        return False           
                    grade = int(input('Enter the grade which you want ot change: '))
                    if grade in obj.grades:
                        new_grade = int(input('Enter the new grade: '))
                        for g in range(len(obj.grades)):
                            if obj.grades[g] == grade:
                                obj.grades[g] = new_grade
                                idx_st = idx.idx_st(students, obj)
                                students[idx_st] = obj.to_dict(obj)
                                write_stud.write(students)
                                return True
                    else:
                        print('This student does not have such a grade!')
                        return False     
                except ValueError:
                    print('Invalid input!')
                    continue
    def display_students(self, students, courses):
        course = input('Enter a course which students you want to display: ').title().strip()
        flag, obj = Course.check_course_name(course, courses)
        if flag:
            ml = []
            for stud in students:
                if stud['Course'] == obj.name:
                    print(stud)
                    print(100 * '=')
        else:
            print('That course does not exist!')
    def search_student(self, students):
        name = input('Enter student name: ').title().rstrip().lstrip()
        course = input('Enter course: ').strip().title()
        flag, obj = Student.find_student(name, course, students)
        if flag:
            print(100 * '=')
            print(obj.to_dict(obj))
            print(100 * '=')
        else:
            print('Student does not exist!')