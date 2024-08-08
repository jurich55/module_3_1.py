
def count_calls():
    count_calls.counter += 1


# Создаём функцию string_info с параметром string
def string_info(string):
    count_calls()
    return (len(string), string.upper(), (string.lower()))


def is_contains(string, list_to_search):
    count_calls()
    return string in list_to_search


count_calls.counter = 0
# Вывод результата
print(string_info('Karusele'))
print(string_info('Fantasticheskiy'))
print(is_contains('Urban', ['Urban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(count_calls.counter)

