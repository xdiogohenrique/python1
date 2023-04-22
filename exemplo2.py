lista = []

for i in range (1,10,1):
    numero = int(input("Insira o número: "))
    lista.append(numero) 
    
print("\n \n")


for num in lista:
        numero_por = num + (0.1*num) 
        print(numero_por)