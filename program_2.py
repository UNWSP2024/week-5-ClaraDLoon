#Program #2: Math Quiz
#Clara Riley
#Luke Snell
#10/04/24

import random as rd

def question():
    num1 = rd.randint(1, 500)
    num2 = rd.randint(1, 500)
    return num1, num2

def check_answer(num1, num2, answer):
    correct_answer = num1 + num2
    if answer == correct_answer:
        print('Congratulations! That is correct.')
    else:
        print('Sorry, wrong answer.')

def problem():
    num1, num2 = question()
    print(f'Add the following numbers: {num1} + {num2}')
    answer = int(input('Your answer is: '))
    check_answer(num1, num2, answer)

problem()
