import random
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    """Генерує відсортований список унікальних випадкових чисел для лотереї."""
    # Перевірка вхідних параметрів на відповідність лімітам:
    # 1. min >= 1, max <= 1000, min <= max
    # 2. 1 <= quantity <= загальний розмір діапазону (max - min + 1)
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= (max - min + 1)):
        return []
    # Генерація унікальних чисел у заданому діапазоні
    numbers = random.sample(range(min, max + 1), quantity)
    # Повернення відсортованого списку
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)