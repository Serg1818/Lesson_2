def month_to_season():
   month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
   season = ['Зима', 'Весна', 'Лето', 'Осень'] 
   month = int(input())
   if month == 12 or month == 1 or month== 2:
      print(season[0])
   elif 3 <= month <= 5:
      print(season[1])
   elif 6 <= month <= 8:
      print(season[2])
   elif 9 <= month <= 11:
      print(season[3])      
   else:
      print('Введите номер месяца в диапазоне 1 - 12')
month_to_season()
