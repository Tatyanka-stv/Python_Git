def check_is_palindrome(number):
    number_as_string = str(number)
    # порівнюємо вихідний рядок з перевернутим рядком
    count = 0
    for symbol in number_as_string:
        if symbol.isdigit():
            count = count +1
        else:
            print('Введений рядок не є числом')
            break    
    
    if count == len(number_as_string):
        if number_as_string == number_as_string[::-1]:
            return True
        else:
            return False

number=input('Введіть число: ')
result = check_is_palindrome(number)
print(result)
