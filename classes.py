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

class WriteCourse:
    @staticmethod
    def write(ml):
        try:
            with open('courses.json', 'w', encoding='utf-8') as f:
                json.dump(ml, f, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            print('File of courses does not exist!')
            exit()

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
    @property
    def total(self):
        return self.__total
    @staticmethod
    def check_course_name(course, courses):
        for c in courses:
            if c['Name'] == course.name:
                return True
        return False
    def add_course(self, course, courses):
        courses.append(course.to_dict(course))
        print('Course is added!')
    def to_dict(self, course):
        return {'Name': course.name,
                'Students': course.students,
                'Students total': course.total}
    def __str__(self):
        return f'Name: {self.__name}\nStudents: {self.__students}\nStudents total: {self.__total}'

class Main:
    def add_course(self, courses):
        try:
            course_name = input('Enter course name: ').title().lstrip().rstrip()
            new_course = Course(course_name)
            flag = new_course.check_course_name(new_course, courses)
            if flag:
                print('That course is exist!')
                return
            else:
                new_course.add_course(new_course, courses)
        except KeyboardInterrupt:
            print('\nBye bye!')
            exit()
    def display_course(self, courses):
        try:
            course_name = input('Enter course name: ').rstrip().lstrip().title()
            obj = Course(course_name)
            flag = obj.check_course_name(obj, courses)
            if flag:
                print(20 * '=')
                print(obj)
                print(20 * '=')
            else:
                print('Course does not exist!')
        except KeyboardInterrupt:
            print('Bye bye!')
            exit()