n = int(input("Insira um número qualquer:"))

for x in range(1, n + 1):
    if n % x == 0:
        print(x)
