# escreva  um programa que leia 5 numeros , informe os pares e os ímpares e por fim a soma deles

pares = []
impares = []
soma = 0

for i in range(1, 6):
    numero = int(input(f' Digite o {i}° numero: '))
    soma += numero

    if numero % 2  == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'\nnumeros pares são: {pares}')
print(f'numeros impares são: {impares}')     
print(f' o total dos numeros: {soma}')   




