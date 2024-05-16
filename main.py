# List of information used
students = ['Lawrence', 'Joseph', 'Tyler', 'Katie', 'Daniel']
hometown = ['Detroit', 'Ann Arbor', 'Troy', 'Flint', 'Muskegon']
favorite_food = ['pizza', 'chicken wings', 'hamburgers', 'sushi', 'tacos']
keep_going = 'y'

# Asking user to list or input name directly
question = str(input('Would you like to list or input a name? Type "list" or "input": ')).lower()

# If statement to cycle through previous user input
# If list is chosen enumerate cycles through and displays the student names
# If input is chosen user types a name, and it will display the corresponding number so user can answer next prompt
if question == 'list':
    def list_students():
        print('Student names:')
        for i, names in enumerate(students, 1):
            print(f'{i}: {names}')
    list_students()
    print()
elif question == 'input':
    name_input = str(input('>> ')).capitalize()
    if name_input not in students:
        print('Student is not listed.')
    else:
        student_number = students.index(name_input)
        print(f'{name_input} has a student number of: {student_number + 1}')

while keep_going == 'y':
    while True:
        student_number = int(input('Which student would you like to learn more about? Enter a number 1-5: '))
        if student_number > len(students) or student_number < 1:
            print(f'Number {student_number} is not a valid student number, please try again.')
        else:
            break

    student_name = students[student_number - 1]
    print(f'Student {student_number} is {student_name}. What would you like to know?')

    selection = str(input('Enter "hometown" or "favorite food": ')).lower()

    if 'hometown' in selection:
        print(f'{student_name} is from {hometown[student_number - 1]}')
    elif 'favorite food' in selection:
        print(f'{student_name}\'s favorite food is {favorite_food[student_number - 1]}')
    else:
        print('That category does not exist. Please try again.')

    keep_going = str(input('Would you like to learn about another student? Enter "y" or "n": ')).lower()
