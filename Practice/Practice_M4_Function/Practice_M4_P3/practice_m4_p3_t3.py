def print_stars(N):
    if N > 0:
        print("*", end=" ")
        print_stars(N - 1)
    
try:
    N = int(input("Введіть N: "))
    if N > 0:
         print("Ряд зірок:")
         print_stars(N)
    else:
         print('Введене число відємне або дорівнює. Ряд з * побудувати неможливо.')    

except:
    print('Ви ввели не ціле число.')    
