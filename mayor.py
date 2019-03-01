contadorpositivo=0
contadornegativo=0
contadorcero=0
for n in range(1,11):
    n=int(input('Ingrese los número'))
    if n>0:
        contadorpositivo=contadorpositivo+1
    elif n<0:
        contadornegativo=contadornegativo+1
    else:
        contadorcero=contadorcero+1
print(contadorpositivo)
print(contadornegativo)
print(contadorcero)






