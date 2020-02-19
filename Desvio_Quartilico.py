array = [-1, -8, -20, -12, 0, 5, 7, 14, 25, 30]


def calcularMedia(array):
    return round(sum(array) / len(array), 2)


def calcularAmplitudeTotal(array):
    maior = max(array)
    menor = min(array)

    return maior - menor


def calcularDesvioQuartilico(array):
    arrayOrdenado = array[:]
    arrayOrdenado.sort()
    listaAux = []

    n = len(arrayOrdenado)

    posQ1 = (n + 1) / 4
    posQ2 = ((n + 1) * 2) / 4
    posQ3 = ((n + 1) * 3) / 4

    arrayPosicoes = [posQ1, posQ2, posQ3]
    arrayDiferencas = []
    finalPos = []

    for c in range(3):
        deltaQ1 = arrayPosicoes[c] - int(arrayPosicoes[c])
        posQ = arrayPosicoes[c] - 1
        diferenca = 0

        if (deltaQ1 == 0):
            diferenca = arrayOrdenado[int(posQ)]

        else:
            posAnterior = arrayOrdenado[int(posQ)]
            posSeguinte = arrayOrdenado[int(posQ) + 1]
            diferenca = abs(posAnterior - posSeguinte)

        finalPos.append(arrayOrdenado[int(posQ)] + diferenca)

        listaAux.append({
            "PosicaoAnterior": posAnterior,
            "PosicaoSeguinte": posSeguinte,
            "PosicaoFinal": finalPos,
            "Diferenca": diferenca,
            "Delta": deltaQ1,
            "PosicaoQ": int(posQ)
        })

    return listaAux

def calcularDesvioInterQuartilico(array):
    desvioQuartilico = calcularDesvioQuartilico(array)["PosicaoFinal"]

    Q1 = desvioQuartilico[0]
    Q3 = desvioQuartilico[2]

    return Q3 - Q1


arrayOrdenado = array[:]
arrayOrdenado.sort()

# print(arrayOrdenado)


dQ = calcularDesvioQuartilico(array)

posicoesEncontradas = []
for i in dQ:
    # print(i)
    # print(i["Diferenca"] * i["Delta"])
    # print((i["Diferenca"] * i["Delta"]) + i["PosicaoAnterior"])
    posicoesEncontradas.append({
        "Valor": (i["Diferenca"] * i["Delta"]) + i["PosicaoAnterior"],
        "Index": i["PosicaoQ"]
    })


aux = arrayOrdenado[:]
for i in range(len(arrayOrdenado)):
    item = arrayOrdenado[i]

    #CORRIGIR ORDENACAO NA LISTA
    for pos in posicoesEncontradas:
        val = pos["Valor"]
        aux.insert(pos["Index"], f'-{val}-')

    break
print(aux)

# print(f'Array Inicial: {array}\n' +
#       f'Array ordenado: {arrayOrdenado}\n' +
#       f'Média: {calcularMedia(array)}\n' +
#       f'Amplitude Total: {calcularAmplitudeTotal(array)}\n' +
#       f'Desvio Quartílico: {dQ["PosicaoFinal"]}\n' +
#       f'Desvio Interquartílico: {calcularDesvioInterQuartilico(array)}\n' +
#       f'Valor máximo: {max(array)}\n' +
#       f'Valor Mínimo: {min(array)}\n')
