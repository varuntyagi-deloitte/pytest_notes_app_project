import random


def random_email():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    word = random.choice(letters)
    number = random.choice(numbers)
    for i in range(5):
        word = word + random.choice(letters)
    for i in range(3):
        number = number + random.choice(numbers)
    email = word+str(number)+"@gmail.com"
    return email