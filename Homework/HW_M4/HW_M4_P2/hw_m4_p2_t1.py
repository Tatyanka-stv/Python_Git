user_text = input('Введіть арифметичний вираз (наприклад, 23+12 або 12-10 або 20*5 або 14/2): ')
user_text = str(user_text) #приймаємо введену дію як рядок
length = len(user_text)
operand1=''
operator=''
operand2=''
index_diya=0
for ch in user_text:
    if ch not in '+-*/':
        operand1 = operand1+''.join(ch)  # з рядка user_text формуємо підрядок operand1 як посимвольне додадваня при перевірці умови, що символ, що додається не є +-*/
    else:
        break     

for ch in user_text:
    if ch != '+':
       continue
    else:
        if ch == '+': #визначаємо для себе яка саме дія буде відбуватися, а саме +
            operator='+'
            index_diya=user_text.index(ch) #визначили індекс символа +

for ch in user_text:
    if ch != '-':
       continue
    else:
        if ch == '-':   #визначаємо для себе яка саме дія буде відбуватися, а саме -
            operator='-'
            index_diya=user_text.index(ch)  #визначили індекс символа -

for ch in user_text:
    if ch != '*':
       continue
    else:
        if ch == '*': #визначаємо для себе яка саме дія буде відбуватися, а саме *
            operator='*'
            index_diya=user_text.index(ch) #визначили індекс символа *

for ch in user_text:
    if ch != '/':
       continue
    else:
        if ch == '/': #визначаємо для себе яка саме дія буде відбуватися, а саме /
            operator='/'
            index_diya=user_text.index(ch) #визначили індекс символа /           

operand2 = ''.join(user_text[index_diya+1:]) # з рядка user_text формуємо підрядок operand2 як зріз рядка від индекса+1 до кінця рядка
print('number1=', operand1)
print('diya=', operator)
print('number2=', operand2)
number1=float(operand1) #перетворюємо рядок на число
number2=float(operand2)
if operator =='+':
    print(operand1+'+'+operand2+'='+str(number1+number2)) #рахуємо сумму чисел

if operator =='-':
    print(operand1+'-'+operand2+'='+str(number1-number2))   #рахуємо різницю чисел

if operator =='*':
    print(operand1+'*'+operand2+'='+str(number1*number2)) #рахуємо добуток чисел

if operator =='/':
    if number2==0:
        print('Ділити на 0 неможливо!')
    else:
        print(operand1+'/'+operand2+'='+str(number1/number2))    #рахуємо ділення чисел