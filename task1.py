import sys

def get_min_element(arr):
    """
    Знаходить мінімальний елемент масиву.
    Згідно з завданням, оформлено як окрему функцію.
    """
    if not arr:
        return None
    
    # Можна використати вбудовану функцію min(arr), 
    # але для навчальних цілей показуємо алгоритм:
    minimum = arr[0]
    for x in arr:
        if x < minimum:
            minimum = x
    return minimum

def calc_sum_between_positives(arr):
    """
    Обчислює суму елементів, розташованих між першим 
    і останнім додатними елементами.
    """
    first_pos_index = -1
    last_pos_index = -1

    # Знаходимо індекси першого та останнього додатного елемента
    for i, x in enumerate(arr):
        if x > 0:
            if first_pos_index == -1:
                first_pos_index = i
            last_pos_index = i
    
    # Перевірка: якщо додатних елементів менше двох або їх немає
    if first_pos_index == -1 or last_pos_index == -1 or first_pos_index == last_pos_index:
        return 0.0
    
    # Обчислюємо суму строго МІЖ цими індексами
    # Слайсинг (зріз) у Python бере елементи від start до end-1
    elements_between = arr[first_pos_index + 1 : last_pos_index]
    
    return sum(elements_between)

def move_zeros_to_front(arr):
    """
    Перетворює масив: спочатку всі нулі, потім усі інші елементи.
    Повертає новий відсортований список.
    """
    # Використовуємо генератори списків для чистоти коду
    zeros = [x for x in arr if x == 0]
    others = [x for x in arr if x != 0]
    
    # З'єднуємо списки: спочатку нулі, потім інші
    return zeros + others

def main():
    print("=== Екзаменаційний білет №13 (Python) ===")
    print("Виконав: Студент групи (Ваше Прізвище)")
    
    # 1. Введення даних з перевіркою
    while True:
        try:
            user_input = input("Введіть елементи масиву через пробіл (наприклад: -2 0 5.5 0 3): ")
            # Конвертуємо введені рядки у дійсні числа (float)
            # Також замінюємо кому на крапку, якщо користувач ввів дробові числа через кому
            str_list = user_input.replace(',', '.').split()
            arr = [float(x) for x in str_list]
            
            if len(arr) == 0:
                print("Масив не може бути порожнім. Спробуйте ще раз.")
                continue
            break
        except ValueError:
            print("Помилка! Введіть коректні дійсні числа.")

    print(f"\nВаш масив: {arr}")
    print("-" * 30)

    # 2. Виклик функції пошуку мінімуму
    min_val = get_min_element(arr)
    print(f"1. Мінімальний елемент: {min_val}")

    # 3. Виклик функції суми між додатними
    total_sum = calc_sum_between_positives(arr)
    print(f"2. Сума між першим і останнім додатними: {total_sum}")

    # 4. Виклик функції перестановки нулів
    sorted_arr = move_zeros_to_front(arr)
    print(f"3. Перетворений масив (нулі спочатку): {sorted_arr}")
    
    print("-" * 30)
    input("Натисніть Enter, щоб завершити роботу...")

if __name__ == "__main__":
    main()