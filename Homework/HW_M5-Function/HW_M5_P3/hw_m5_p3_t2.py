import random


def generate_secret_number():
    digits = random.sample(range(10), 4)
    return ''.join(map(str, digits))
    


def check_number(secret_number, input_number_letters):
    bulls = 0
    cows = 0
    i = 0
    while i <=3:
        if input_number_letters[i] == secret_number[i]:
            cows += 1
            i =i +1 
        else:
            i=i+1

    j = 0
    while j<=3:        
        if (input_number_letters[j] in secret_number):
            bulls += 1
            j = j+1
        else:
            j = j+1
     
    return bulls, cows


def play_game(secret_number, attempts=1):
    input_number = input('Введіть 4-значне число: ') 
    
    input_number_letters = list(input_number) 
   

    if not input_number.isdigit() or len(input_number) != 4:
        print('Введіть коректне 4-значне число.')
    
        play_game(secret_number, attempts)
        return 
    
    bulls, cows = check_number(secret_number, input_number_letters)

    if cows == 4:
        print('Вітаємо! Ви вгадали число '+str(secret_number)+' за '+str(attempts)+' спроб.')
    else:
        print('Бики: '+str(bulls)+', Корови: '+str(cows))
        play_game(secret_number, attempts + 1)


secret_number = generate_secret_number()
print(secret_number)
print('Вітаємо у грі ''"''Бики та корови''"''! Спробуйте вгадати 4-значне число.')
play_game(secret_number)

