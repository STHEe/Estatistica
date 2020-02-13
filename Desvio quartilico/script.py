array = [-1, -8,-20, -12, 0, 5, 7, 14, 25]

def calcularMedia(array):
      return round(sum(array) / len(array) , 2)

def calcularAmplitudeTotal(array):
      maior = max(array)
      menor = min(array)

      return maior - menor

def calcularDesvioQuartilico(array):
      arrayOrdenado = array[:]
      arrayOrdenado.sort()
      
      n = len(arrayOrdenado)

      posQ1 = (n + 1) / 4
      posQ2 = ((n + 1) * 2) / 4
      posQ3 = ((n + 1) * 3) / 4

      arrayPosicoes = [posQ1, posQ2, posQ3]
      arrayDiferencas = []
      finalPos = []

      for c in range(3):
            diferencaQ = arrayPosicoes[c] - int(arrayPosicoes[c])
            posQ = arrayPosicoes[c] - 1
            diferenca = 0

            if (diferencaQ == 0):
                  diferenca = arrayOrdenado[int(posQ)]

            else:
                  posAnterior = arrayOrdenado[int(posQ)]
                  posSeguinte = arrayOrdenado[int(posQ) + 1]
                  diferenca = abs(posAnterior - posSeguinte)
                  
            finalPos.append(arrayOrdenado[int(posQ)] + diferenca / 2)

      return finalPos

def calcularDesvioInterQuartilico(array):
      desvioQuartilico = calcularDesvioQuartilico(array)

      Q1 = desvioQuartilico[0]
      Q3 = desvioQuartilico[2]

      return Q3 - Q1

arrayOrdenado = array[:]
arrayOrdenado.sort()

print(f'Array Inicial: {array}\n' +
      f'Array ordenado: {arrayOrdenado}\n' +
      f'Média: {calcularMedia(array)}\n' +
      f'Amplitude Total: {calcularAmplitudeTotal(array)}\n' +
      f'Desvio Quartílico: {calcularDesvioQuartilico(array)}\n' +
      f'Desvio Interquartílico: {calcularDesvioInterQuartilico(array)}')
