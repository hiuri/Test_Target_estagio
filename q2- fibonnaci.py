number = int(input("Digite um número: "))
atual=1
anterior=0
while(number>atual):
  aux = atual
  atual = atual + anterior
  anterior = aux
  print(atual)
if(atual == number):
  print("o numero " + str(number) + " pertence a sequencia")
else:
  print("o numero " + str(number) +  " nao pertence a sequencia")
    
