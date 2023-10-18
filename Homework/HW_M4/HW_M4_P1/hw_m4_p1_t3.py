import re # re-модкль позволяет работать с сырыми строками
def count_sentences(text):
    # Предложение обычно заканчивается точкой, вопросительным или восклицательным знаком
    # Разделим текст по этим знакам и посчитаем количество элементов в списке
    sentences = re.split(r'[.!?]', text) 
    #re.split(r'[.!?]', text) позволяет задавать более сложніе условия для разбиения строк. 
    #в данном случае условие разбиения-r'[.!?]'

    # Уберем пустые строки, которые могли появиться из-за разделения
    sentences = [s.strip() for s in sentences if s.strip()] 
    #Эта строка кода фильтрует список sentences, yдаляя пустые строки и убирая лишние пробельные символы в начале и конце каждой строки. 
    return len(sentences) #возвращает кол-во предложений из списка предложений

user_text = input('Введіть текст для обробки: \n')

# Подсчет предложений в примере
sentence_count = count_sentences(user_text)

# Вывод результата
print('Кількість речень: ', sentence_count)