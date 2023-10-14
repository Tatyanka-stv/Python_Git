def print_square_1(size): 
    for i in range(size):
        for j in range(size):
            if j >= i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def print_square_2(size): 
    for i in range(size):
        for j in range(size):
            if j > i:
                print(' ', end='')
            else:
                print('*', end='')
        print()

def print_square_3(size): 
    n=int(size/2)
    for i in range(n,1,-1):
        if i<= int(size/2):
          print(' '*(n+1-i)+'*'*(2*i)) 
    print(' '*(n)+'*'*2)    
      
    for j in range(1,n+1,1): 
        print(' '*n)    

def print_square_4(size): 
    for i in range(1,size,1):
        if i<= int(size/2):
            print(' '*size)
        else:
             break
    n=int(size/2)   
    for j in range(1,n+1): 
        print(' '*(n-j)+'*'*(2*j))  

def print_square_5(size): 
    n=int(size/2)
    for i in range(n,1,-1):
        if i<= int(size/2):
          print(' '*(n+1-i)+'*'*(2*i)) 
    print(' '*(n)+'*'*2)    
    n=int(size/2)   
    for j in range(1,n+1,1): 
        print(' '*(n+1-j)+'*'*(2*j))  

def print_square_6(size):  
    n=int(size/2)
    for i in range(1,n+1,1):
        print('*'*i+' '*(size-2*i)+'*'*i) 
    #print('*'*n)    
    for j in range(n+1,1,-1): 
         print('*'*(j-1)+' '*(size-2*j+2)+'*'*(j-1))              

def print_square_7(size):   
    n=int(round((size/2),0))
    for i in range(n,1,-1):
        if i<= int(size/2):
          print('*'*(n+1-i)+' '*(1+2*i)) 
    print('*'*n)    
    n=int(round((size/2),0))   
    for j in range(1,n+1,1): 
        print('*'*(n+1-j)+' '*(1+2*j))    

def print_square_8(size):  
    n=int(round((size/2),0))
    for i in range(1,n+1,1):
        print(' '*(2*n-i)+'*'*i)
        
    n=int(round((size/2),0))   
    for j in range(n+1,1,-1): 
        print(' '*(2*n-j+1)+'*'*(j-1))  

def print_square_9(size): 
    n=int(round((size/2),0))
    for i in range(size):
        print('*'*(size-i))   

def print_square_10(size): 
    for i in range(size+1):
        print(' '*(size-i)+'*'*i)  


try:
    print('Будуємо фігури.')
    size = int(input('Введіть довжину сторони квадрата: '))
    if size <= 0:
        print('Довжина сторони квадарата має не можу бути відємним числом або 0.')
    else:    
        while True:
            #menu
            print('Меню:')
            print('1. Фігура А.')
            print('2. Фігура Б.')
            print('3. Фігура В.')
            print('4. Фігура Г.')
            print('5. Фігура Д.')
            print('6. Фігура Е.')
            print('7. Фігура Ж.')
            print('8. Фігура З.')
            print('9. Фігура И.')
            print('10. Фігура К.')
            print('0. Вихід.')

            choice = int(input('Оберіть опцію: '))

            if choice == 1:
                print_square_1(size)

            elif choice == 2:
                print_square_2(size)

            elif choice == 3:
                print_square_3(size)

            elif choice == 4:
                print_square_4(size)

            elif choice == 5:
                print_square_5(size)

            elif choice == 6:
                print_square_6(size)

            elif choice == 7:
                print_square_7(size)

            elif choice == 8:
                print_square_8(size)

            elif choice == 9:
                print_square_9(size)

            elif choice == 10:
                print_square_10(size)

            elif choice == 0:
                print('Вихід з програми.')
                break

            else:
                print('Некоректний вибір. Спробуйте ще раз.')

except ValueError:
    print('Помилка! Введіть ціле число.')

