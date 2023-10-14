import random
import time

# Загадываем число в диапазоне от 1 до 500
secret_number = random.randint(1, 500)
attempts = 0 #количество попыток
start_time = time.time()
    
print('Пограємо у гру Вгадай число?')
    
while True:
    
    user_guess = int(input('Введіть ваш здогад (або 0 для виходу): '))

    if user_guess == 0:
        print('Кінець гри.')
        break
        
    attempts = attempts + 1
        
    if user_guess < secret_number:
        print('Загадане число більше.')
    elif user_guess > secret_number:
        print('Загадане число менше.')
    else:
        print('Вітаємо! Ви вгадали число '+str(secret_number)+'!')
        break
    
end_time = time.time()
result_time = end_time - start_time
    
print('Статистика:')
print('Кількість спроб: '+str(attempts))
print('Витрачений час: '+str(round(result_time,2))+'секунд')