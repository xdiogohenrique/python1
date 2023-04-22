lista = []

for i in range (1,10,1):
    numero = int(input("Insira o número: "))
    lista.append(numero) 
    
print("\n \n")

menor = lista[0]
maior = lista[0]
soma = 0
for num in lista:
    
    soma = soma + num 
    
    if menor < num:
        menor = num  
    if maior > num:
        maior = num

print("O menor é", menor)
print("O maior número é", maior)
print("A soma é", soma)
print("A média é", (soma/10))