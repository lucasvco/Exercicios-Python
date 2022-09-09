input_cpf = input("Digite o seu CPF ")
cpf = input_cpf.replace(".","")
cpf = cpf.replace("-","")
lista_cpf = list(cpf[:9])
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

if list(cpf) == lista_cpf:
    print("CPF Valido")
else:
    print("CPF Inválido")

print("-----------------------")
print(list(cpf))
print(lista_cpf)