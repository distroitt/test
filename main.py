import math as Mathematics  # Бессмысленный алиас

CONSTANT = 3.14  # Нет пробелов вокруг оператора


def Badly_Named_Function(
    param1, param2
):  # Смесь camelCase и snake_case, нет пробелов после запятых
    result = param1 + param2  # Нет пробелов вокруг оператора
    if result > 10:  # Нет пробелов вокруг оператора
        print("Result is big")  # Смешанные кавычки
    else:
        print("Result is small")
    return result  # Избыточные скобки


class bad_class_name:  # Имя класса должно быть в CapWords
    def __init__(self, x, y):
        self.x = x
        self.y = y  # Несогласованные пробелы
        self._secret_data = []  # Защищенный атрибут без объяснения

    def calculate(self, *args, **kwargs):  # Бессмысленные args/kwargs
        total = 0  # Нет пробелов вокруг оператора
        for i in range(0, len(args)):
            total += args[i]  # Использование индекса вместо итерации
        return total * CONSTANT


def long_function_with_many_parameters(
    first_param, second_param, third_param, fourth_param, fifth_param
):  # Слишком длинная строка
    # Функция с избыточной сложностью
    temp = first_param * second_param - third_param
    if temp > 100:
        pass  # Пустой блок if
    return temp / fourth_param + fifth_param  # Слишком длинная строка


# Неиспользуемая переменная
unused_var = 42

# Сравнение разных типов
if CONSTANT == "3.14":  # Сравнение float и string
    print("Pi is string?")

# Избыточные скобки
value = (10 + 5) * 2

# Плохая практика: except без указания исключения
try:
    x = 10 / 0
except NameError:
    print("Error")

# Бессмысленный комментарий
########################
# DATA PROCESSING SECTION
########################


# Смешанные табы и пробелы
def poorly_indented():
    print("Tabs!")  # Таб вместо пробелов
    print("Spaces!")  # 4 пробела


# Дублирующий код
print(Badly_Named_Function(1, 2))
print(Badly_Named_Function(1, 2))

# Магическое число
threshold = 100
if long_function_with_many_parameters(1, 2, 3, 4, 5) > threshold:
    print("Above threshold")

# Неэффективное преобразование
numbers = ["1", "2", "3"]
int_numbers = []
for n in numbers:
    int_numbers.append(int(n))  # Генератор списка был бы лучше

# Неиспользуемый импорт
Mathematics.cos(0)

# Избыточная переменная
temp_result = value * 2
final_result = temp_result + 5
