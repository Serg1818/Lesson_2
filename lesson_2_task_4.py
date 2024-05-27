fizz_buzz = int(input())
if fizz_buzz % 3 == 0 and fizz_buzz % 5 !=0:
     print('Fizz')
elif fizz_buzz % 5 == 0 and fizz_buzz % 3 != 0:
   print('Buzz')
elif (fizz_buzz % 3 and fizz_buzz % 5) == 0:
   print('FizzBuzz') 
else:
  print(fizz_buzz)