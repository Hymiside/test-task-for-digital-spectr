from string import digits


def check_number(numbers):

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