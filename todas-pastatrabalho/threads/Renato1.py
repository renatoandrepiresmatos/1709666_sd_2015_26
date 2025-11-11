"""
ex2.py
exercício: 

- crie um programa em python com uma única função,
mult(nome,x). 

- A função mult(nome,x) é usadapro duas threads, th1, th2.

- Ath1 usa mult(nome, x) para imprimir os primeiros 100 múltiplos de 2,

- Ath2 usa mult(nome, x) para imprimir os primeiros 100 múltiplos de 3,

- o programa a principal no fim tem uma linha com print("FINAL")
"""

def mult(nome, x):
    for i in range(1, 101):
        print(f"{nome}: {i} x {x} = {i * x}")
       

th1 = threading.Thread(target=mult, args=("Thread 1", 2))
th2 = threading.Thread(target=mult, args=("Thread 2", 3))
th1.start()
th2.start()
th1.join()
th2.join()
print("FINAL")