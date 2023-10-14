def generate_question(difficulty):
    # Генерациія питання для завданого ріввня складности
    if difficulty == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(11, 20)
    elif difficulty == 3:
        num1 = random.randint(11, 20)
        num2 = random.randint(11, 20)
    else:
        raise ValueError('Некоректний рівень складности.')
    correct_answer = num1*num2
    return num1, num2, correct_answer

import random
try:
    print('Таблиця множення.')
    print('Меню:')
    print('1. Легкий рівень складності.')
    print('2. Середній рівень складності.')
    print('3. Високий рівень складності.')
    print('4. Вихід.')
    difficulty = int(input('Оберіть опцію: '))
    if difficulty == 4:
         print('Програма завершила свою роботу.')
    elif difficulty>=1 and difficulty<=3:     
        num_questions = int(input('Введіть кількість питань: '))
        score = 0
        for _ in range(num_questions):
            num1, num2, correct_answer = generate_question(difficulty)

            # Користувач дає відповідь 
            user_answer = int(input(str(num1)+' * '+str(num2)+ ' = '))

            # Перевірка відповіді
            if user_answer == correct_answer:
                print('Правильна відповідь!')
                score  = score + 1
            else:
                print('Помилка! Правильна відповідь: '+str(correct_answer))

        # Результат
        percent_correct = (score / num_questions) * 100
        print('Ваш результат: '+str(percent_correct)+' % вірних відповідей.')
        if percent_correct >= 90:
            print('Відмінно!')
        elif percent_correct >= 70:
            print('Добре!')
        elif percent_correct >= 50:
            ('Задовільно.')
        else:
            print('Спробуйте ще раз.')
    else:
        print('Операція вибрана неправильно.')
except ValueError:
    print('Помилка! Введіть коректне число для рівня складности та кількості питань.')