def change_reserved_words(text, reserved_words):
    words = text.split()  # поділ тексту на слова. орієнтир що це слово-є пробіл
    modified_text = [] #створюємо новий порожній список, куди будемо додавати змінені зарезервовані слова
    for word in words:
        if word.lower() in reserved_words:
            word = word.upper() #змінюємо слово на верхній регістр
            modified_text.append(word)  # додаємо змінене на верхній регістр слово у список  змінених слів
        else:
            modified_text.append(word)
    return ' '.join(modified_text)  # поєднуємо у текст слів зі списку


user_text = input('Введіть текст: ')
reserved_words_str = input('Введіть список зарезервованих слів через пробіл: ') #введені слова приймаються як рядок
reserved_words = reserved_words_str.split()  # переводимо у нижній регістр
reserved_words = reserved_words_str.lower() # розділяємо рядок на окремі слова

modified_text = change_reserved_words(user_text, reserved_words)

print('Змінений текст:')
print(modified_text)