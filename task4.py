def is_palindrome_recursive(s):
   if not isinstance(s, str):
       raise ValueError("Аргумент має бути рядком")
   s = ''.join(c.lower() for c in s if c.isalnum())
   if len(s) <= 1:
       return True
   if s[0] != s[-1]:
       return False
   return is_palindrome_recursive(s[1:-1])


try:
   s = input("Введіть рядок для перевірки на паліндром: ")
   print("Це паліндром?" , is_palindrome_recursive(s))
except Exception as e:
   print("Помилка:", e)
