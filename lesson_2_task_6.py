lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
l= len(lst)
for i in range(l):
  if 30 > lst[i] and lst[i]%3 == 0:
   print(lst[i])
