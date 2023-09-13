from is_prime import is_prime

n =  int (input("Ange talen n"))
if n<=99:
    for i in range(2,n+1):
     if is_prime(i):
            print(i, end=', ')
