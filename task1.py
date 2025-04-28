def factorial_recursive(n):
   if not isinstance(n, int) or n < 0:
       raise ValueError("Аргумент має бути цілим невід'ємним числом")
   if n == 0:
       return 1
   return n * factorial_recursive(n - 1)


try:
   n = int(input("Введіть число для обчислення факторіалу: "))
   print("Факторіал:", factorial_recursive(n))
except Exception as e:
   print("Помилка:", e)
