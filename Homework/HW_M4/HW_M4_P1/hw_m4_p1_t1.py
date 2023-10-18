import string

def check_palindrome(s):
    s = s.lower() 
    s = ''.join(ch for ch in s if ch not in string.punctuation and ch != ' ') 
    return s == s[::-1] 

user_input = input('Введіть рядок: ')
if check_palindrome(user_input):
    print('Рядок є паліндромом.')
else:
    print('Рядок не є паліндромом.')