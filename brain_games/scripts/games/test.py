import random
import operator
import prompt
# def generation_expression():
#     num_1 = random.randint(10, 50)
#     op = random.choice(['-', '+', '*'])
#     num_2 = random.randint(1, 10)
#     print(f'Question: {num_1} {op} {num_2}')
#     user_answer = int(prompt.string('Your answer: '))
#     answer_list = []
#     answer_list.append(user_answer)
#     print(answer_list)
#     if op == '-':
#         answer_list.append(operator.sub(num_1, num_2))
#         return answer_list
#     elif op == '+':
#         answer_list.append(operator.add(num_1, num_2))
#         return answer_list
#     elif op == '*':
#         answer_list.append(operator.mul(num_1, num_2))
#         return answer_list
#
# print(generation_expression())
#
# def welcome_user():
#     print('Welcome to the Brain Games!')
#     user_name: str | None = prompt.string('May I have your name? ')
#     print(f'Hello, {user_name}!')
#     return user_name
#
#
# # print(generation_expression())



def ask_question():
    number = random.randint(0, 100)
    answers_list = []
    answers_list.append(number)
    question = f'Question: {number}'
    print(question)
    user_answer = prompt.string('Your answer: ')
    answers_list.append(user_answer)
    print(answers_list)
    return answers_list

print(ask_question())
