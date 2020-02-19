def media(lista):
    soma = sum(lista)
    soma /= len(lista)
    return round(soma,2)

def desvioMedio(lista):
    avg = media(lista)
    soma = 0
    for c in range(len(lista)):
        soma += abs(lista[c] - avg)
    soma /= len(lista)
    return round(soma,2)

def desvioPadrao(lista):
    avg = media(lista)
    soma = 0
    for c in range(len(lista)):
        soma += (lista[c] - avg)**2
    soma /= len(lista)
    soma = soma **(1/2)
    return round(soma,2)

def variancia(lista):
    avg = media(lista)
    soma = 0
    for c in range(len(lista)):
        soma += (lista[c] - avg)**2
    soma /= len(lista)
    return round(soma,2)

lista = [2,3,6,8,11]
dvMedio = desvioMedio(lista)
dvPadrao = desvioPadrao(lista)
vrc = variancia(lista)
print("Lista: ", lista)
print("Média: ", media(lista))
print("Desvio Médio: ", dvMedio)
print("Desvio Padrão: ", dvPadrao)
print("Variancia2: ", vrc)
print()