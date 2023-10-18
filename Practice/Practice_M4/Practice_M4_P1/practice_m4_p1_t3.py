def count_occurrences(user_string, user_char):
    count = 0
    for char in user_string:
        if char == user_char:
            count = count + 1
    return count


user_string = input('Введіть рядок: ')

user_char = input('Введіть символ для пошуку у рядку: ')

count = count_occurrences(user_string, user_char)

print('Символ ('+user_char+') входить '+str(count)+' раз(а) у введеному рядку.')