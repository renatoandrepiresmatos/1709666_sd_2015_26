
"""
O programa bloqueia aqui e o scheduler espera 10 segundos.
Quando o tempo passa, ele executa a função addition(5, 6).
s.enter(delay, priority, func, argument) agenda uma função.
--> delay=10 → o evento ocorrerá 10 segundos depois;
--> priority=1 → define a prioridade (usada se houver eventos simultâneos);
--> addition → função a executar;
--> argument=(5, 6) → argumentos da função.
O event1 é um objeto de evento, que o scheduler usa internamente (contém o tempo e a ação agendada)
"""


import sched
from datetime import datetime
import time
def addition(a,b):
    print("Performing Addition : ", datetime.now())
    print("Time : ", time.monotonic())
    print("Result : ", a+b)
s = sched.scheduler()
print("Start Time : ", datetime.now())
event1 = s.enter(10, 1, addition, argument = (5,6))
print("Event Created : ", event1)
s.run()
print("End Time : ", datetime.now())
