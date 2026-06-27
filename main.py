from classes import OpenCourse, WriteCourse
from classes import OpenStudent, WriteStudent
from classes import Main, Course
from classes import FindIdx

def first_check():
    print('1)Courses\n2)Students')
    while True:
        try:
            user = int(input('Choose a variant: '))
            return user
        except ValueError:
            print('Invalid input!')
            continue
        except KeyboardInterrupt:
            print('\nBye bye!')
            exit()
def main():
    main = Main()
    courses = OpenCourse().open()
    write_course = WriteCourse()
    students = OpenStudent().open()
    write_stud = WriteStudent()
    idx = FindIdx()
    while True:
        user = first_check()
        try:
            if user == 1:
                print('1)Add course')
                print('2)Display courses')
                print('3)Search course')
                print('4)Delete course')
                print('5)Calculate average grade of course')
                choose = int(input('Enter a variant: '))
                if choose == 1:
                    main.add_course(courses)
                    write_course.write(courses)
                elif choose == 2:
                    print(courses)
                elif choose == 3:
                    main.search_course(courses)
                elif choose == 4:
                    main.delete_course(courses)
                    write_course.write(courses)  
                elif choose == 5:
                    main.avg_score(courses)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                else:
                    print('Invalid input!')
                    continue
            elif user == 2:
                print('1)Add/Delete student')
                print('2)Add/Delete grade')
                print('3)Change course')
                print('4)Change grade')
                print('5)Display students')
                print('6)Search student')
                choice = int(input('Enter a variant: '))
                if choice == 1:
                    second_choice = input('You want to delete or add the student(d/a)? ').lower().strip()
                    if second_choice == 'd':
                        flag = main.delete_student(students, write_stud)
                        if flag:
                            print('Successfully deleted!')
                    elif second_choice == 'a':
                        flag = main.add_student(students, courses, write_stud, write_course, idx)
                        if flag == False:
                            continue
                        else:
                            print('Student is added!')
                    else:
                        print('Invalid input!')
                        continue
                elif choice == 2:
                    second_choice = input('You want to delete or add the grade(d/a)? ').lower().strip()
                    if second_choice == 'd':
                        flag = main.delete_grade(students, write_stud, idx)
                        if flag:
                            print('Successfully deleted!')
                    elif second_choice == 'a':
                        flag = main.add_grade(students, write_stud, idx)
                        if flag:
                            print('Successfully added!')
                    else:
                        print('Invalid input!')
                        continue
            else:
                print('Invalid input!')
                continue
        except ValueError:
            print('Invalid input!')
            continue
        except KeyboardInterrupt:
            print('\nBye bye!')
            exit()
        
main()

#total\students of course
#Check a course since adding student
