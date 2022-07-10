# 1. import math to use log function
import math

# 2. set all values to 0 for future calculations
result = 0.0
sum_of_calc = 0
num_of_calc = 0

# 3. create a boolean value to prevent infinite loops
more_math = True

# 4. create a function to display menu
def print_menu():
    print(f'\nCurrent Result: {result}\n')
    print('Calculator Menu')
    print('-' * 15)
    print('0. Exit Program')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exponentiation')
    print('6. Logarithm')
    print('7. Display Average')


# 5. print menu and prompt user to make a selection
print_menu()
operation = int(input(('\nEnter Menu Selection: ')))


# 6. if user inputs 1-6, prompt user to enter input a number
while more_math == True:
    if 1 <= operation <= 6:
        operand_1 = input('Enter first operand: ')
        operand_2 = input('Enter second operand: ')

        # BONUS: set previous calculation to 'RESULT'
        if operand_2 == 'RESULT':
            operand_2 = last_result
        if operand_1 == 'RESULT':
            operand_1 = last_result

        # 7. carry out operation given by the inputed menu selection
        if operation <= 1:
            result = float(operand_1) + float(operand_2)
        elif operation <= 2:
            result = float(operand_1) - float(operand_2)
        elif operation <= 3:
            result = float(operand_1) * float(operand_2)
        elif operation <= 4:
            result = float(operand_1) / float(operand_2)
        elif operation <= 5:
            result = float(operand_1) ** float(operand_2)
        elif operation <= 6:
            result = math.log(float(operand_2), float(operand_1))

        # 8. print the results of the calculation and reprint the menu
        print_menu()
        operation = int(input('\nEnter Menu Selection: '))
        more_math = True

        # 9. update all values for future calculations
        last_result = result
        sum_of_calc += result
        num_of_calc += 1

    # 10. allow user to end the program
    elif operation == 0:
        print('\nThanks for using this calculator. Goodbye!')
        more_math = False

    # 11. calculate the average, but only if possible!
    elif operation == 7:
        if num_of_calc > 0:
            print(f'\nSum of calculations: {sum_of_calc}')
            print(f'Number of calculations: {num_of_calc}')
            print(f'Average of calculations: {(sum_of_calc / num_of_calc):.2f}\n')
            operation = int(input('Enter Menu Selection: '))
            more_math = True
        else:
            print('\nError: No calculations yet to average!\n')
            operation = int(input(('Enter Menu Selection: ')))
            more_math = True

    # print error message for an invalid selection
    else:
        print('\nError: Invalid selection!\n')
        operation = int(input(('Enter Menu Selection: ')))
        more_math = True



