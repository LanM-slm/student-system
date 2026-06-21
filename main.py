from classes import OpenCourse
from classes import Main, Course

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
    courses = OpenCourse()
    while True:
        user = first_check()
        try:
            if user == 1:
                print('1)Add course')
                print('2)Display courses')
                print('3)Delete course')
                choose = int(input('Enter a variant: '))
                if choose == 1:
                    main.add_course(courses)
                elif choose == 2:
                    pass
                elif choose == 3:
                    pass
                else:
                    print('Invalid input!')
                    continue
            elif user == 2:
                pass
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

    