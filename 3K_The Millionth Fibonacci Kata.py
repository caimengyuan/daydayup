'''
In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fin(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.
'''

def fib(n):
  if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
  a = b = x = 1
  c = y = 0
  while n:
    if n % 2 == 0:
      (a, b, c) = (a * a + b * b,
                   a * b + b * c,
                   b * b + c * c)
      n /= 2
    else:
      (x, y) = (a * x + b * y,
                b * x + c * y)
      n -= 1
  return y


def fib(n):
  """I love this solution from SICP and have been 
  practicing it from memory for the last year.
  """
  a, b, p, q = 1, 0, 0, 1
  sign = -1 if (n < 0) & (abs(n) % 2 == 0) else 1
  n = abs(n)
  while True:
      if n == 0:
          return b * sign
      elif n % 2 == 0:
          p, q = (p**2 + q**2), (q**2 + 2*p*q)
          n /= 2
      else:
          a, b = (b*q + a*q + a*p), (b*p + a*q)
          n -= 1

print(fib(8))