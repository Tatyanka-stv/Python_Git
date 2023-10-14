num = float(input('Введіть число: '))
if abs(num)-int(abs(num))==0 :
     num=int(num)
     if num < 0:
         print('Факторіал відємного числа невизнаений.')
     if num==0 or num==1:
             print(str(num)+'!=1.') 
     if num>1:
         result=1
         for num in range(2, num + 1):
             result=result*num
         print(str(num)+'!='+str(result))
else:
    print('Число введено невірно. Воно є дійсним.')