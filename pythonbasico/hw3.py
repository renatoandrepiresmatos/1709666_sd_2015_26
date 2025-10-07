

n = int(input("Introduz um numero inteiro: "))

print(f"Númros primos até {n}: ")

for numero in range(2, n +1):
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
     primo = False
     break

 if primo:
     print(numero)