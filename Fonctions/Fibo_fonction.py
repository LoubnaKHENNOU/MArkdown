#Implémenter la suite Fibonacci

def fibonacci(n):
  a=0
  b=1
  print("La suite Fibonacci est: ")
  print(a, ",", b, end= ", ")
  for i in range(2,n):
    c = a + b
    print(c, end = ", " )
    a = b
    b = c

fibonacci(6)
