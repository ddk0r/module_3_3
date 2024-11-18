def print_params(a=2, b='строка', c=True):
    print(a, b, c)  # Функция должна выводить эти параметры.

# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(5, 'SMS')
print_params(7, None, False)
print_params(26)
print_params()

# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print('Функция print_params(b=25) работает')
print_params(c=[1, 2, 3])
print('Функция print_params(c = [1,2,3]), работает')
# Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
values_list = [125, None, 'Текст']
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 1256.7891, 'b': "Снег", 'c': False}
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = ['Туапсинская', 45]
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 31)
print('Функция print_params(*values_list_2, 42), работает')