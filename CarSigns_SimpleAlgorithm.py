"""
Для того чтобы корректно запустить программу проверки автомобильных знаков,
нужно вызвать функцию main(). В коде она уже вызвана с аргументом из примера.
Вы можете просто подставить новое значение.
"""

from string import digits


def main(numbers):
    list_of_correct_answers = []
    list_of_wrong_answers = []
    key_char = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']

    for number in numbers:
        if 10 > len(number) > 7:
            a = True
            for i in range(len(number)):
                if i == 0:
                    if number[i] not in key_char:
                        a = False

                elif i == 1:
                    if number[i] not in digits:
                        a = False

                elif i == 2:
                    if number[i] not in digits:
                        a = False

                elif i == 3:
                    if number[i] not in digits:
                        a = False

                elif i == 4:
                    if number[i] not in key_char:
                        a = False

                elif i == 5:
                    if number[i] not in key_char:
                        a = False

                elif i == 6:
                    if number[i] not in digits:
                        a = False

                elif i == 7:
                    if number[i] not in digits:
                        a = False

            if a:
                list_of_correct_answers.append(number)
            else:
                list_of_wrong_answers.append(number)
        else:
            list_of_wrong_answers.append(number)
    print(f'Список с правильными автомобильными номерами: {list_of_correct_answers}')
    print(f'Список с неправильными автомобильными номерами: {list_of_wrong_answers}')


main(["А123АА11", "А222АА123", "А12АА123", "А123СС1234", "АА123А12"])
