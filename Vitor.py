# vitor = [-20,-1,-8,-12,0,5,7,14,25]
vitor = [-50,10,30,25,2,-6,-3,-15,20,15,50]
vitor.sort()

N = len(vitor)
Qi = (N + 1) / 4
Qii = ((N + 1) * 2) / 4
Qiii = ((N + 1) * 3) / 4

if int(Qi) < Qi :
    ArrayQi = [int(Qi)-1,int(Qi)]
    FlagQi = True
else :
    ArrayQi = Qi
    FlagQi = False

if int(Qii) < Qii :
    ArrayQii = [int(Qii)-1,int(Qii)]
    FlagQii = True
else :
    ArrayQii = Qii
    FlagQii = False

if int(Qiii) < Qiii :
    ArrayQiii = [int(Qiii) -1 ,int(Qiii)]
    FlagQiii = True
else :
    ArrayQiii = Qiii
    FlagQiii = False

DecimalQi = Qi - int(Qi)
DecimalQii = Qii - int(Qii)
DecimalQiii = Qiii - int(Qiii)

# ESPACO PARA CALCULAR O DESVIO

if(FlagQi == True):
    DesvioQi = (vitor[ArrayQi[1]] + vitor[ArrayQi[0]]) * DecimalQi
else:
    DesvioQi = vitor[int(Qi-1)]
    
if(FlagQii == True):
    DesvioQii = (vitor[ArrayQii[1]] + vitor[ArrayQii[0]])  * DecimalQii
else:
    DesvioQii =  vitor[int(Qii-1)]

if(FlagQiii == True):
    DesvioQiii = (vitor[ArrayQiii[1]] + vitor[ArrayQiii[0]])  * DecimalQiii
else:
    DesvioQiii = vitor[int(Qiii-1)]
     
DesvioInterQuartilico = (DesvioQiii - DesvioQi)

print(vitor)
print('Qi: ' + str(DesvioQi))
print('Qii: ' + str(DesvioQii))
print('Qiii: ' + str(DesvioQiii))
print('Desvio Interquartilico: ' + str(DesvioInterQuartilico))


# print (ArrayQi)
# print (ArrayQii)
# print (ArrayQiii)
# print('---')
# print(ArrayQi)
# print(ArrayQii)
# print(ArrayQiii)

# print (Qi)
# print(DecimalQi)
# print (Qii)
# print(DecimalQii)
# print (Qiii)
# print(DecimalQiii)


# num = 2.9

# print (int(num))
    