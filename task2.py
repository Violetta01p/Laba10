def fibonacci_recursive(n):
   if not isinstance(n, int) or n < 0:
       raise ValueError("Аргумент має бути цілим невід'ємним числом")
   if n == 0:
       return 0
   if n == 1:
       return 1
   return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


try:
   n = int(input("Введіть номер числа Фібоначчі: "))
   print(f"{n}-те число Фібоначчі:", fibonacci_recursive(n))
except Exception as e:
   print("Помилка:", e)
