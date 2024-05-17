def menu():
    print('\nMENU')
    print('a - Add student')
    print('c - Calculate grade average')
    print('d - Remove student')
    print('o - Output student and name roster')
    print('u - Update student grade')
    print('q - Quit\n')

def calculate_average(dict):
    length = len(dict)
    sum = 0
    for i in dict:
        sum += dict[i]
    average = sum / length
    return (f'{average:.2f}')

user_choice = ''
student_dict = {}
student_num = 5

# for student grade please enter 0 ~ 100.
for i in range(student_num):
    name = input('Enter student name:\n')
    grade = int(input('Enter student grade(0~100):\n'))
    student_dict[name] = grade

while user_choice != 'q':
    # call menu function to print menu
    menu()
    user_choice = input('Choose an option:\n')

    if user_choice == 'a':
        name = input('Enter a new student name:\n')
        grade = int(input('Enter a new grade(0~100):\n'))
        # add a new student and grade in the dictionary
        student_dict[name] = grade

    elif user_choice == 'c':
        print('Student grade average is: ', end='')
        # call calculate_average functon to print average
        print(calculate_average(student_dict))

    elif user_choice == 'd':
        name = input('Enter the student name:\n')
        # delete student and grade
        del student_dict[name]

    elif user_choice == 'o':
        print('STUDENT AND GRADE ROSTER')
        for i in student_dict:
            print(f'Student name: {i}, grade: {student_dict[i]}')

    elif user_choice == 'u':
        name = input('Enter student name:\n')
        grade = int(input('Enter student grade(0~100):\n'))
        # update student and grade in the dictionary
        student_dict[name] = grade



