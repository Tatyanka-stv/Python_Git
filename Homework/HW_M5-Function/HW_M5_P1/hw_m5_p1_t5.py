def calculate_product_of_numbers(start, end):#добуток чисел
    start = int(start)
    end = int(end)
    if start > end:
        start, end = end, start
        product_of_numbers = 1
        for number in range(start, end + 1,1):
            product_of_numbers =  product_of_numbers * number

    else:
         product_of_numbers = 1
         for number in range(start, end + 1,1):
            product_of_numbers =  product_of_numbers * number

    return product_of_numbers

start = float(input('Введіть першу межу діапазона чисел: '))
end = float(input('Введіть другу межу діапазона чисел: '))

if abs(start)-int(abs(start)) == 0 and abs(end)-int(abs(end)) == 0:
    print('Добуток чисел в діапазоні від '+str(int(start))+' до '+str(int(end))+' дорівнює '+str(calculate_product_of_numbers(start, end))) 
else:
    print('Ви ввели не ціле число.')