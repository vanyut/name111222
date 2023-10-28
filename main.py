def get_even(number):
    if number % 2 == 0:
        return True
    return False
    
print(get_even(7))
print(get_even(26))


def counter_symbol(s):
    temp = "aeiou"
    s = s.lower()
    count_lit = 0
    for lit in temp:
        count_lit += s.count(lit)
    return count_lit

s = "Weather in Odesa for today accurate weather forecast for today for Odesa Odeskyi district Odessa Oblast Ukraine"
print(counter_symbol(s))


def get_factorial(number):
    factorial = 1
    if number == 0:
        print("error")
    while number > 0:
        factorial *= number
        number -= 1
    return factorial

print(get_factorial(6))