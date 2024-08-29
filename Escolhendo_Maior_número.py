number_1 = int(input('Digite o primeiro número: '))
number_2 = int(input('Digite o segundo número: '))
number_3 = int(input('Digite o terceiro número: '))

lista_números = [number_1,number_2, number_3]
lista_números.sort()
print('O maior número da lista é: {}'.format(lista_números[-1]))