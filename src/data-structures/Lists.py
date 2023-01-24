from typing import List


def summation(numbers: List[int]) -> int:
    if len(numbers) <= 1:
        return numbers[0]
    acc: int = 0
    for i in numbers:
        acc += i
    return acc


class Person:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height

    def greetings(self) -> str:
        return f"Hi! ${self.name}"


def age_average(people: List[Person]) -> float:
    if len(people) == 1:
        return float(people[0].age)
    acc: int = 0
    for person in people:
        acc += person.age
    return acc / len(people)


def main() -> None:
    new_list: List[int] = [10, 15, 20, 25, 30]
    new_list_acc = summation(new_list)
    print(new_list_acc)

    P1 = Person("John", 15, 1.72)
    P2 = Person("Doe", 22, 2.15)
    P3 = Person("Kevin", 18, 1.75)

    people: List[Person] = [P1, P2, P3]

    value = age_average(people)
    print(value)


main()
