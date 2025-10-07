
# Programa para mostrar todos os números primos até um número dado

# Ler número inteiro do utilizador
n = int(input("Introduz um número inteiro: "))

print(f"Números primos até {n}:")

# Percorrer todos os números de 2 até n
for num in range(2, n + 1):
    # Verificar se 'num' é primo
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num)
