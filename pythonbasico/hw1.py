print("ola Mundo")
x=input("Escreva o seu o nome: ")
print("Olá,",x,"Como estás ?")
u=(1,"A","Andre",1.23,1.23)#tuple
# u[0]=10 não é permitido nos tuplos alterror os seus valores
v=(1,"A","Andre",1.23,1.23)#tuple
v[0]="Coca-Cola"
w=(1,"A","Andre",1.23,1.23)
print("u é uma tuplo", u,u[0])
print("u é uma lista", v,v[0])
print("u é um conjunto",w)
# w[0] operacao 