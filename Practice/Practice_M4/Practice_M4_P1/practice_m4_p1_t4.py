def count_word_occurrences(input_str, target_word):
    # Преобразуем строку к нижнему регистру для учета всех возможных вариантов написания слова
    input_str_lower = input_str.lower()
    target_word_lower = target_word.lower()
    
    # Подсчитываем количество вхождений искомого слова
    return input_str_lower.count(target_word_lower)

# Получаем строку от пользователя
user_string = input('Введіть рядок: ')
user_word = input('Введіть слово для пошуку: ')
user_string_lower = user_string.lower() # переводимо усі символи у нижній регістр. щоб правильно порахувати слова з символмаии різними регістрами
user_word_lower = user_word.lower()
occurrences = user_string_lower.count(user_word_lower)
print('Слово '+user_word+' входить '+str(occurrences)+' раз(а) у введений рядок.')