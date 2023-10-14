while True:
    #menu
    print('Конвертер валют:')
    print('1. UAH в USD')
    print('2. UAH в EUR')
    print('3. USD в UAH')
    print('4. EUR в UAH')
    print('5. USD в EUR')
    print('6. EUR в USD')
    print('0. Вихід')
    print()

    choice = input('Оберіть операцію: ')

    if choice == '1':
         # 1 UAH = 0.0265 USD.
        uah_amount = float(input('Введіть суму в гривнях: '))
        usd_amount = 0.0265 * uah_amount
        print('Результат конвертації: '+str(uah_amount)+' UAH = '+str(round(usd_amount,2))+' USD\n')

    elif choice == '2':
        # 1 UAH = 0.025 EUR
        uah_amount = float(input('Введіть суму в гривнях: '))
        eur_amount = 0.025 * uah_amount
        print('Результат конвертації: '+str(uah_amount)+' UAH = '+str(round(eur_amount,2))+' EUR\n')

    elif choice == '3':
        # 1 USD = 37.7 UAH
        usd_amount = float(input('Введіть суму в доларах: '))
        uah_amount = 37.7 * usd_amount
        print('Результат конвертації: '+str(usd_amount)+' USD = '+str(round(uah_amount,2))+' UAH\n')

    elif choice == '4':
        # 1 EUR = 40.07 UAH
        eur_amount = float(input('Введіть суму в євро: '))
        uah_amount = 40.07 * eur_amount
        print('Результат конвертації: '+str(eur_amount)+' EUR = '+str(round(uah_amount,2))+' UAH\n')

    elif choice == '5':
        # 1 USD = 0.9263 EUR
        usd_amount = float(input('Введіть суму в доларах: '))
        eur_amount = 0.9263 * usd_amount
        print('Результат конвертації: '+str(usd_amount)+' USD = '+str(round(eur_amount,2))+' EUR\n')


    elif choice == '6':
        # 1 EUR = 1.049 USD
        eur_amount = float(input('Введіть суму в євро: '))
        usd_amount = 1.049 * eur_amount
        print('Результат конвертації: '+str(eur_amount)+' EUR = '+str(round(usd_amount,2))+' USD\n')

    elif choice == "0":
        print('Роботу закінчено.')
        break
    else:
        print("Некоректний вибір. Спробуйте ще раз.\n")