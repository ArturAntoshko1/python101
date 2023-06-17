summa = 0
a = None 
my_list = []
while a != 0:
    a = int(input("Введите число: "))
    my_list.append(a)


summa = sum(my_list)
print(summa)