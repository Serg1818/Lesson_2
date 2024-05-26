def month_to_season():
   month = ['Зима', 'Весна', 'Лето', 'Осень'] 
   a = int(input())
   if 0 <= a <= 3:
      print(month[a])
   else:
        print('Введите номер месяца в диапазоне 0 - 3')
month_to_season()
