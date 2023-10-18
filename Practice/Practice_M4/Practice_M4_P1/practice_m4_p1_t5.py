def replace_word(user_string, target_word, replacement_word):
    words = user_string.split() # Разбиваем строку на слова
    print(words)
    replaced_words = [] # створюємо новий порожній список, щоб до нього додавати слова, що знайшли та замінили у вихідному рядку
    for word in words:
        if word == target_word:
            replaced_words.append(replacement_word)
        else:  
            replaced_words.append(word)  

    replaced_string = ' '.join(replaced_words) #перетворюємо список зі слів знову у рядок
    return replaced_string
      

user_string = input('Введіть рядок: ')
target_word = input('Введіть слово для пошуку в рядку: ')
replacement_word = input('Введіть слово для заміни: ')

result_string = replace_word(user_string, target_word, replacement_word)
print('Результат заміни:')
print(result_string)