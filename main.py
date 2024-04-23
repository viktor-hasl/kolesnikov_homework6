import random
from time import sleep


# Задача 1 ________________________________________________________________________________________________________________________


LIST_CARDS = ['Т♣', 'Т♠', 'Т♥', 'Т♦', 'K♣', 'K♠', 'K♥', 'K♦',
             'Д♣', 'Д♠', 'Д♥', 'Д♦', 'В♣', 'В♠', 'В♥', 'В♦',
             '10♣', '10♠', '10♥', '10♦', '9♣', '9♠', '9♥', '9♦',
             '8♣', '8♠', '8♥', '8♦', '7♣', '7♠', '7♥', '7♦', '6♣', '6♠', '6♥', '6♦']

# Класс колоды
class BlackJackDeck:
    def __init__(self):
        self.list_card = ['Т♣', 'Т♠', 'Т♥', 'Т♦', 'K♣', 'K♠', 'K♥', 'K♦',
                          'Д♣', 'Д♠', 'Д♥', 'Д♦', 'В♣', 'В♠', 'В♥', 'В♦',
                          '10♣', '10♠', '10♥', '10♦', '9♣', '9♠', '9♥', '9♦',
                          '8♣', '8♠', '8♥', '8♦', '7♣', '7♠', '7♥', '7♦', '6♣', '6♠', '6♥', '6♦']

        random.shuffle(self.list_card)

    # метод которй достает карту из колоды
    def get_card(self):
        self.card = random.choice(self.list_card)
        self.list_card.remove(self.card)
        return self.card

# Игрок с победными очками и рукой
class Gamer:
    def __init__(self):
        self.name = 'You'
        self.wins = 0
        self.hand = ''
    # Добавление карты в руку
    def hand_gamer(self, card):
        self.hand += f" {card}"
    # Очистка руки, для новой партии
    def clear_hand(self):
        self.hand = ''
    # Расчет очков в руке
    def calculation(self):
        hand_calc = self.hand.strip().split(' ')
        self.points = 0
        for i in hand_calc:
            card_nomen = i[:-1]
            if card_nomen == "Т":
                self.points += 11
            elif card_nomen == "K":
                self.points += 4
            elif card_nomen == "Д":
                self.points += 3
            elif card_nomen == "В":
                self.points += 2
            else:
                self.points += int(card_nomen)

        return self.points
    # Отображение руки иргоку
    def hand_show(self):
        print(f'В вашей руке:{self.hand} \n {self.points} очков')

# Создаем класс соперника, наследую от игрока
class Computer(Gamer):
    def __init__(self, ):
        super().__init__()
        self.name = 'computer'

    def hand_show(self):
        print(f'В руке компьютера было:{self.hand} \n {self.points} очков')


if __name__ == '__main__':
    # Создаем игрока и компьютера
    gamer = Gamer()
    comp = Computer()
    print("Карточная игра 'Двадцать одно', игра проходит с колодой в 36 карт, игроку на руку выдается по две карты, каждая карта"
          "имеет свое количество очков: \n"
          "T - 11 \n"
          "K - 4 \n"
          "Д - 3 \n"
          "В - 2 \n"
          "Числовые равны значению их номиналу\n"
          "Нужно собрать 21 очко , и не перебрав иначе сразу будет проигрыш, побеждает тот у кого будет ближе к 21")
    while True:
        # Создаем колоду
        deck = BlackJackDeck()
        # Даем вае карты игроку
        gamer.hand_gamer(deck.get_card())
        gamer.hand_gamer(deck.get_card())
        gamer.calculation()
        # Даем две карты компьютеру
        comp.hand_gamer(deck.get_card())
        comp.hand_gamer(deck.get_card())
        comp.calculation()
        # показываем игроку его карты, и даем выбор будет ли он ещё набирать
        gamer.hand_show()
        # Делаем задержки для более приятного отображения для человека
        sleep(0.5)
        while True:
            gamer_input = input('Ещё одну карту?(+/-): ')
            sleep(0.5)
            if gamer_input == '+':
                # даем ещё карту и рассчитывае и показываем, что в руке
                gamer.hand_gamer(deck.get_card())
                gamer.calculation()
                gamer.hand_show()
            elif gamer_input == '-':
                print(f'Ваши очки: {gamer.calculation()}')
                sleep(0.5)
                break
            else:
                print('Некорректный ввод, можно либо + либо -')
                sleep(0.5)
                # Если 21 то продолжать нет смысла
            if gamer.calculation() == 21:
                print('У вас очко!')
                sleep(0.5)
                break
                # И если перебор, тоже нет смысла в продолжении
            if gamer.calculation() > 21:
                print('У вас перебор!')
                sleep(0.5)
                break

        sleep(1)
        # Задаем, что компьютер берет, пока не будет больше 17 очков
        while comp.calculation() <= 17:
            comp.hand_gamer(deck.get_card())
        # Теперь проверяем все возможные условия, в соответствии с условием, добавляем очко победы, тому кто победдил
        if gamer.calculation() > 21 and comp.calculation() > 21:
            print(f"У вас и у компьютера перебор")
            sleep(0.5)
            comp.hand_show()
        elif gamer.calculation() > 21:
            print("У вас перебор победил компьютер")
            sleep(0.5)
            comp.hand_show()
            comp.wins += 1
        elif comp.calculation() > 21:
            print(f"У компьютер перебор {comp.calculation()} вы побудили")
            sleep(0.5)
            gamer.wins += 1
            comp.hand_show()
        elif gamer.calculation() == 21 and comp.calculation() == 21:
            print(f"У вас и у компьютер ничья")
            sleep(0.5)
            comp.hand_show()
        elif gamer.calculation() == 21:
            print("У вас 21 вы победили ")
            sleep(0.5)
            comp.hand_show()
            gamer.wins += 1
        elif comp.calculation() == 21:
            print(f"У компьютера {comp.calculation()} он победил")
            sleep(0.5)
            comp.wins += 1
            comp.hand_show()
        elif gamer.calculation() < 21 and comp.calculation() < 21:
            if gamer.calculation() > comp.calculation():
                print(f"Вы победили у вас {gamer.calculation()}")
                sleep(0.5)
                comp.hand_show()
                gamer.wins += 1
            elif gamer.calculation() == comp.calculation():
                print(f"У вас и у компьютер ничья")
                sleep(0.5)
                comp.hand_show()
            else:
                print(f"Вы прогирали у вас {gamer.calculation()}")
                sleep(0.5)
                comp.hand_show()
                comp.wins += 1
        sleep(0.5)
        # Выводим таблицу побед
        print(f"{gamer.name} - {gamer.wins}")
        print(f"{comp.name} - {comp.wins}")
        sleep(0.5)
        input_gamer = input("Ещё одну игру? '-' для выхода, для продолжения Enter:")
        if input_gamer == '-':
            sleep(1)
            print('Было приятно поиграть!!')
            sleep(2)

            break
        else:
            # Если продолжаем играть, то очищаем руки игроков
            comp.clear_hand()
            gamer.clear_hand()
        sleep(2)
# Супер, одна из лучших реализаций задачи, все отлично, сложно, круто
# Задача 2 --------------------------------------------------------------------------------------------------------------

class TooManyErrors(Exception):
    pass

def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Инициализируем счетчик попыток
            attempts = 0
            while attempts < n:
                try:
                    # Вызываем задекорированную функцию
                    return func(*args, **kwargs)
                # Если возникает исключение
                except ZeroDivisionError:
                    print(f'Попытка {attempts+1}')
                    # Увеличиваем счетчик попыток
                    attempts += 1
            # Если превышено количество попыток, возбуждаем исключение TooManyErrors
            raise TooManyErrors(f"Функция {func.__name__} Провалилась {n} раз, вызвано исключание")
        return wrapper
    return decorator

# Используем декоратор retry с параметром n=3
@retry(5)
def divide(a, b):
    return a / b


# Попытаемся выполнить деление на ноль, чтобы проверить как отрабатывает счетчик
# Закомментировал, чтобы вывод не мешал тестам
# result = divide(10, 0)

# Все верно
# Задание 3 ------------------------------------------------------------------------------------------------------------------------
'''Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
Какое число является 10001-м простым числом?'''

# Функция для проверки числа, является ли оно простым
def prime(number):
    # Единица не является простым числом
    if number <= 1:
        return False
    if number <= 3:
        return True
    # пытаемся сделать функцию бысрее сократив возможные варианты
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    # Сокращаем и запускаем цикл
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        # После того как проверены делители 2 и 3, можно заметить, что все простые числа больше 3 представляют
        # собой 6k ± 1, где k - некоторое целое число.
        # Таким образом, все остальные делители, которые мы должны проверить, должны быть в форме 6k ± 1
        i += 6
    return True

def get_prime_number(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n должно быть целым положительным числом")
    count = n
    number = 1

    while count != 0:
        # Начинаем с первого простого числа
        number += 1
        # уменьшаем наш счетчик простых чисел, если нашли простое число
        if prime(number):
            count -= 1
    return number

'''
2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 2^1000?
'''
def sum_of_digits(exponent):
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError("Показатель должен быть неотрицательным целым числом")
    # получаем число в степени
    power_of_two = 2 ** exponent
    # переводим в строку
    power_str = str(power_of_two)

    digit_sum = 0
    # Прибовляем каждую цифру к сумме
    for digit in power_str:
        digit_sum += int(digit)

    return digit_sum

# все окей
