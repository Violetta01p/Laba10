def sum_list_recursive(lst):
   if not isinstance(lst, list):
       raise ValueError("Аргумент має бути списком")
   if not lst:
       return 0
   return lst[0] + sum_list_recursive(lst[1:])


try:
   nums = input("Введіть числа через пробіл: ").split()
   lst = [float(x) for x in nums]
   print("Сума списку:", sum_list_recursive(lst))
except Exception as e:
   print("Помилка:", e)
