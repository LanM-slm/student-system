import json

class OpenCourse:
    @staticmethod
    def open():
        try:
            if not os.path.exists('courses.json'):
                print('File of courses is not defined!')
                answer = input('Give your permission to create this file(y/n): ').lower().strip()
                if answer == y:
                    with open('courses.json', 'w', encoding='utf-8') as f:
                        json.write([], indent=4, ensure_ascii=False)
                else:
                    print('Bye bye!')
                    exit()
            else:
                with open('courses.json', 'r', encoding='utf-8') as f:
                    reader = json.read(f)
                return reader
        except KeyboardInterrupt:
            print('\nBye bye!')
            exit()
            
class Course:
    def __init__(self, name, students=0):
        self.__name = name
        self.__students = students
    @staticmethod
    def check_course_name(course, courses):
        for c in courses:
            if c.name == course.name:
                return True
        return False
    def add_course(self, course, courses):
        courses.append(course.to_dict())
        print('Course is added!')
    def to_dict(self, course):
        return {'Name': course.name,
                'Students': course.students}
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
                new_course.add_course()
        except KeyboardInterrupt:
            print('\nBye bye!')
            exit()
        