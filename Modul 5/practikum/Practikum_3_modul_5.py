# Проект: Генератор комбинаций карт
# Цель:
# Написать программу,
# которая создает все возможные комбинации из заданного количества карт (от 1 до 52) в стандартной колоде.
# Шаги:
#  1) Создание колоды:
#  Сгенерируйте список всех карт в стандартной колоде.
#  2) Генерация комбинаций:
#  Используйте модуль itertools, чтобы получить все комбинации из заданного числа карт.
#  3) Вывод результатов:
#  Выведите все комбинации на экран или сохраните их в файл для последующего использования.
import itertools


def create_deck():
    # Создание стандартной колоды из 52 карт
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f'{rank}{suit}' for suit in suits for rank in ranks]
    return deck


def generate_combinations(deck, num_cards):
    # Генерация всех комбинаций из заданного количества карт
    combinations = list(itertools.combinations(deck, num_cards))
    return combinations


def save_card(combinations, filename):
    # сохранение всех комбинаций карт в файле по строчно
    with open(filename, 'w', encoding='utf8') as file:
        for combo in combinations:
            file.write(', '.join(combo) + '\n')


def read(filename):
    # чтение из файла и вывод на экран
    with open(filename, "r", encoding='utf8') as file:
        return file.read()


def main():
    # Получаем количество карт от пользователя
    while True:
        try:
            num_cards = int(input("Введите количество карт для генерации комбинаций (от 1 до 52): "))
            if 1 <= num_cards <= 52:
                break
            else:
                print("Пожалуйста, введите число от 1 до 52.")
        except ValueError:
            print("Некорректный ввод, попробуйте снова.")

    deck = create_deck()
    combinations = generate_combinations(deck, num_cards)
    filename = 'cards.txt'
    save_card(combinations, filename)
    print(f"Все комбинации из {num_cards} карт сохранены в файл '{filename}'.")
    # чтение и вывод на экран содержимое
    print(read(filename))


if __name__ == "__main__":
    main()
