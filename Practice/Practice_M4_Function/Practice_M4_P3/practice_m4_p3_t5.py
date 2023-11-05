import random
import math

def find_min_subsequence_start(numbers, subsequence_ofnumbers_length=10, current_position=0, min_position=0, min_sum= math.inf):
    
    if current_position == len(numbers):
        return min_position

    if current_position <= len(numbers) - subsequence_ofnumbers_length:
        print(numbers[current_position:current_position + subsequence_ofnumbers_length])
        current_sum = sum(numbers[current_position:current_position + subsequence_ofnumbers_length])
        print ('current sum= ',current_sum)

        if current_sum < min_sum:
            min_sum = current_sum
            min_position = current_position
            print('current position with min current summa  =', min_position)
    
    return find_min_subsequence_start(numbers, subsequence_ofnumbers_length, current_position + 1, min_position, min_sum)

random_numbers = [random.randint(1, 500) for _ in range(100)]
print('Сформаваний список випадкових чисел: ')
print(random_numbers)
print()
print('Формуємо списки із послідовності 10 чисел: ')
start_position = find_min_subsequence_start(random_numbers)
print()
print('Позиція, з якої починається послідовність з мінімальною сумою: '+str(start_position))