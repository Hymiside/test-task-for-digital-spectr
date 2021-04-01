"""
Для того чтобы корректно запустить программу проверки автомобильных знаков,
нужно вызвать функцию main(). В коде она уже вызвана с аргументом из примера.
Вы можете просто подставить новое значение.
"""


def check(serial_number, char):

    global a
    key = {'numbers for number': '1' '2' '3' '6' '7',
           'number for chars': '0' '4' '5'}
    list_for_char = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
    list_for_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    if str(serial_number) in key['numbers for number']:
        if char not in list_for_number:
            a = False

    elif str(serial_number) in key['number for chars']:
        if char not in list_for_char:
            a = False


def main(array_numbers):

    global a
    list_of_correct_answers = []
    list_of_wrong_answers = []
    for number in array_numbers:
        if 10 > len(number) > 7:
            a = True
            for i in range(len(number)):
                check(i, number[i])

            if a:
                list_of_correct_answers.append(number)
            else:
                list_of_wrong_answers.append(number)
        else:
            list_of_wrong_answers.append(number)
    print(f'Список с правильными автомобильными номерами: {list_of_correct_answers}')
    print(f'Список с неправильными автомобильными номерами: {list_of_wrong_answers}')


main(["А123АА11", "А222АА123", "А12АА123", "А123СС1234", "АА123А12"])