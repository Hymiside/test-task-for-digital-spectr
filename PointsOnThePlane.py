import math
import random

floor = -99
top = 100


class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


    def __str__(self):
        return f'({self.x},{self.y})'


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def get_sin_oy(self) -> float:
        return self.x / math.sqrt(self.x ** 2 + self.y ** 2)


    def get_area(self) -> int:
        if self.x >= 0 and self.y > 0:
            return 1
        elif self.x >= 0 and self.y <= 0:
            return 4
        elif self.x < 0 and self.y < 0:
            return 3
        else:
            return 2


    def get_distance(self, dist) -> float:
        return math.sqrt((self.x - dist.x) ** 2 + (self.y - dist.y) ** 2)


    def comparator(self):
        if self.x == 0 and self.y == 0:
            return 0

        res = self.get_sin_oy()
        area = self.get_area()


        if area == 1:
            res = res

        elif area == 2:
            res += 4

        elif area == 3:
            res += 3

        else:
            res = 2 - res

        return res


def generate_list(size: int) -> [Point]:
    return [Point(random.randrange(floor, top), random.randrange(floor, top)) for _ in range(0, size)]


def analyze(points: [Point]) -> dict:
    center = Point(0, 0)
    min_point = Point(0, 0)
    min_val = math.sqrt(100 ** 2 + 100 ** 2) + 1
    max_point = Point(0, 0)
    max_val = -1
    avg = 0

    for p in points:
        dist = p.get_distance(center)
        if dist < min_val:
            min_val = dist
            min_point = p

        if dist > max_val:
            max_val = dist
            max_point = p

        avg += dist

    avg /= len(points)

    return {
        'min_val': min_val,
        'min_point': min_point,
        'max_val': max_val,
        'max_point': max_point,
        'avg': avg
    }


if __name__ == '__main__':
    size = 0
    while True:
        print("Введите количество точек!")

        try:
            size = int(input())
        except ValueError:
            print("Ошибка. Введите корректное число!")
            continue

        if size <= 0:
            print("Ошибка. Количество точек должно быть натуральным числом!")
            continue

        break

    points = generate_list(size)
    points.sort(key=Point.comparator, reverse=True)

    if points[-1].get_area() == 1:
        points.insert(0, points[-1])
        points.pop(len(points) - 1)

    print('Список точек в порядке обратном часовой стрелке, начиная из 1 четверти:')
    print(', '.join([str(p) for p in points]))

    statistics = analyze(points)

    print(f'Максимальное расстояние = {round(statistics.get("max_val"), 4)} у точки {statistics.get("max_point")}')
    print(f'Минимальное расстояние = {round(statistics.get("min_val"), 4)} у точки {statistics.get("min_point")}')
    print(f'Среднее расстояние = {round(statistics.get("avg"), 4)}')
