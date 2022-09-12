from random import randint
numero = str(randint(100000000,999999999))

lista_cpf = list(numero)
print(lista_cpf)

def soma_lista(lista):
    soma = []
    contador = len(lista_cpf) + 1
    for numero in lista_cpf:
        print("{} x {} = {}".format(numero, contador, (int(numero) * contador)))
        soma.append(int(numero) * contador)
        contador -= 1
    soma_lista = sum(soma)
    calculo_digito = 11 - (soma_lista % 11)
    if calculo_digito > 9:
        lista_cpf.append("0")
    else:
        lista_cpf.append(str(calculo_digito))
    print("-----------------------")
soma_lista(lista_cpf)
soma_lista(lista_cpf)
print("-----------------------")
print(lista_cpf)

novo_CPF = ""
for numero in lista_cpf:
    novo_CPF += numero
print(novo_CPF)

