

#Usando método sort()
numbers = [1, 4, 8 ,0, 10, 20]
numbers.sort()
print(numbers)

#Usando For encadeados mais if 
numbers = [1, 4, 8 ,0, 10, 20]
for i in range(len(numbers)): 
  for j in range(i):
    if int(numbers[j]) > int(numbers[j+1]):
      numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
print(numbers)