from scipy.io import arff
import pandas as pd
import math
import numpy as np
def probabilidad(x,mean,stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev)) * exponent


def condDiscreta(se, bl, ch, index):
    contsef=contsem=contblh=contbln=contbll=contchh=contchn=contchl=0
    if se[index]=="F":
        contsef += 1
    elif se[index]=="M":
        contsem += 1
    if bl[index]=="HIGH":
        contblh += 1
    elif bl[index]=="NORMAL":
        contbln += 1
    elif bl[index]=="LOW":
        contbll += 1
    if ch[index]=="HIGH":
        contchh += 1
    elif ch[index]=="NORMAL":
        contchn += 1
    elif ch[index]=="LOW":
        contchl += 1

    vcd=[contsef,contsem, contblh, contbln, contbll, contchh, contchn, contchl]
    return vcd

def desviacionEstandar(media, totalValor, acumulado):
    
    a = float((acumulado/(totalValor)))
    c = media*media
    b = abs(a-c)
    desviacion = math.sqrt(b)
    return desviacion

#leer el dataset
data = arff.loadarff('clasificacion-drug.arff')
df = pd.DataFrame(data[0])

#seleccionar la columna de clases y convertirla en una lista
listaDrogas = df['Drug'].tolist()
listaNa = df['Na'].tolist()
listaK = df['K'].tolist()

totalValores = len(listaDrogas)

#Agregar una nueva columna para Na/K
NaK=[]
for i in range(0, totalValores):
    NaK.append(float(listaNa[i])/float(listaK[i]))
   
df_nak = df.copy()

df_nak["Na/K"] = NaK

listaNaK = df_nak['Na/K'].tolist()

listaEdades = df['Age'].tolist()

#Calculo de precisión
df1 = df.sort_values('Age')
listaEd = df1['Age'].tolist()
ContAge1 = 0
sumalistDelta = 0
listaDelta = []
#Calcular delta:
for i in range(0, totalValores-1):
    ContAge1 = listaEd[i+1] - listaEd[i]  
    listaDelta.append(ContAge1)
    sumalistDelta = listaDelta[i] + sumalistDelta 
#Calcular distic:
ContDistic=0
for i in range(0, totalValores-1):
    if listaDelta[i] != 0:
        ContDistic = 1 + ContDistic
#Precisión
precision = sumalistDelta / ContDistic
#Cálculo Edad con Precisión
for j in range(0, totalValores-1):
    listaEdades[j] = math.ceil(listaEdades[j]/precision)  * precision


#Calculo de precisión para NaK

dfNaK1 = df_nak.sort_values('Na/K')
listaNaK1 = dfNaK1['Na/K'].tolist()
ContNaK = 0
sumalistDeltaNaK = 0
listaDeltaNaK = []

#Calcular delta:
for i in range(0, totalValores-1):
    ContNaK = listaNaK1[i+1] - listaNaK1[i]  
    listaDeltaNaK.append(ContNaK)
    sumalistDeltaNaK = listaDeltaNaK[i] + sumalistDeltaNaK 
#Calcular distic:
ContDisticNaK=0
for i in range(0, totalValores-1):
    if listaDeltaNaK[i] != 0:
        ContDisticNaK = 1 + ContDisticNaK
#Precisión
precisionNaK = sumalistDeltaNaK / ContDisticNaK
#Cálculo Edad con Precisión
for j in range(0, totalValores-1):
    listaNaK[j] = math.ceil(listaNaK[j]/precisionNaK)  * precisionNaK    
    

listaSexos = df['Sex'].tolist()
listaBP = df['BP'].tolist()
listaCh = df['Cholesterol'].tolist()


del df["Age"]
df["Na/K"] = listaNaK
df["Age"] = listaEdades

del df["Na"]
del df["K"]

columns = ['Age', 'Sex', 'BP', 'Cholesterol', 'Na/K','Drug']
df = df[columns]

#contar las veces q se repite cada clase
contA=contB=contC=contX=contY=0

for i in range(0,totalValores):
    if listaDrogas[i]=="drugA":
        contA += 1
    elif listaDrogas[i]=="drugB":
        contB += 1
    elif listaDrogas[i]=="drugC":
        contC += 1
    elif listaDrogas[i]=="drugX":
        contX += 1
    else:
        contY += 1


#CALCULO TABLA 1: Probabilidad  de cada clase
pA = float(contA)/totalValores
pB = float(contB)/totalValores
pC = float(contC)/totalValores
pX = float(contX)/totalValores
pY = float(contY)/totalValores
#PROBABILIDADES A PRIORI
df_apriori = pd.DataFrame([pA,pB,pC,pX,pY], index = ['drugA', 'drugB', 'drugC', 'drugX', 'drugY'])

datosapriori = np.asarray(df_apriori)
np.savetxt("apriori.csv",
            datosapriori,
            delimiter=",")

osfa=osma=obha=obna=obla=ocha=ocna=ocla=0
osfb=osmb=obhb=obnb=oblb=ochb=ocnb=oclb=0
osfc=osmc=obhc=obnc=oblc=ochc=ocnc=oclc=0
osfx=osmx=obhx=obnx=oblx=ochx=ocnx=oclx=0
osfy=osmy=obhy=obny=obly=ochy=ocny=ocly=0

contEdadA=0
contNaKA=0
contDesvEdadA=0
contDesvNaKA=0

contEdadB=0
contNaKB=0
contDesvEdadB=0
contDesvNaKB=0

contEdadC=0
contNaKC=0
contDesvEdadC=0
contDesvNaKC=0

contEdadX=0
contNaKX=0
contDesvEdadX=0
contDesvNaKX=0

contEdadY=0
contNaKY=0
contDesvEdadY=0
contDesvNaKY=0

for i in range(0, totalValores):
    if listaDrogas[i]=="drugA":
         
        contEdadA = contEdadA + listaEdades[i]
        contNaKA = contNaKA + listaNaK[i]

        contDesvEdadA = contDesvEdadA + (listaEdades[i]** 2)
        contDesvNaKA = contDesvNaKA + (listaNaK[i]** 2)

        #Contador de los valores de todos los atributos
        ppa = condDiscreta(listaSexos, listaBP, listaCh, i)
        osfa=osfa+ppa[0] #Contador Sexo femenino droga A
        osma=osma+ppa[1]
        obha=obha+ppa[2]
        obna=obna+ppa[3]
        obla=obla+ppa[4]
        ocha=ocha+ppa[5]
        ocna=ocna+ppa[6]
        ocla=ocla+ppa[7]#Contador Cholesterol bajo droga A
        
    elif listaDrogas[i]=="drugB":
        
        contEdadB = contEdadB + listaEdades[i]
        contNaKB = contNaKB + listaNaK[i]
        
        contDesvEdadB = contDesvEdadB + (listaEdades[i] ** 2)
        contDesvNaKB = contDesvNaKB + (listaNaK[i] ** 2)
        
        
        ppb=condDiscreta(listaSexos,listaBP,listaCh,i)
        osfb=osfb+ppb[0]
        osmb=osmb+ppb[1]
        obhb=obhb+ppb[2]
        obnb=obnb+ppb[3]
        oblb=oblb+ppb[4]
        ochb=ochb+ppb[5]
        ocnb=ocnb+ppb[6]
        oclb=oclb+ppb[7]
        
    elif listaDrogas[i]=="drugC":
        
        contEdadC = contEdadC + listaEdades[i]
        contNaKC = contNaKC + listaNaK[i]

        contDesvEdadC = contDesvEdadC + (listaEdades[i] ** 2)
        contDesvNaKC = contDesvNaKC + (listaNaK[i] ** 2)
        
        
        ppc=condDiscreta(listaSexos,listaBP,listaCh,i)
        osfc=osfc+ppc[0]
        osmc=osmc+ppc[1]
        obhc=obhc+ppc[2]
        obnc=obnc+ppc[3]
        oblc=oblc+ppc[4]
        ochc=ochc+ppc[5]
        ocnc=ocnc+ppc[6]
        oclc=oclc+ppc[7]
        
    elif listaDrogas[i]=="drugX":
        
        contEdadX = contEdadX + listaEdades[i]
        contNaKX = contNaKX + listaNaK[i]
        
        contDesvEdadX = contDesvEdadX + (listaEdades[i] ** 2)
        contDesvNaKX = contDesvNaKX + (listaNaK[i] ** 2)
        
        
        ppx=condDiscreta(listaSexos,listaBP,listaCh,i)
        osfx=osfx+ppx[0]
        osmx=osmx+ppx[1]
        obhx=obhx+ppx[2]
        obnx=obnx+ppx[3]
        oblx=oblx+ppx[4]
        ochx=ochx+ppx[5]
        ocnx=ocnx+ppx[6]
        oclx=oclx+ppx[7]
        
    elif listaDrogas[i]=="drugY":
        
        contEdadY = contEdadY + listaEdades[i]
        contNaKY = contNaKY + listaNaK[i]
        
        contDesvEdadY = contDesvEdadY + (listaEdades[i] ** 2)
        contDesvNaKY = contDesvNaKY + (listaNaK[i] ** 2)
        
        
        ppy=condDiscreta(listaSexos,listaBP,listaCh,i)
        osfy=osfy+ppy[0]
        osmy=osmy+ppy[1]
        obhy=obhy+ppy[2]
        obny=obny+ppy[3]
        obly=obly+ppy[4]
        ochy=ochy+ppy[5]
        ocny=ocny+ppy[6]
        ocly=ocly+ppy[7]
        

#CALCULAMOS LA PROBABILIDAD PARA CADA SITUACION CONDICIONAL
probsfda=(float(osfa)+1)/(contA+5)
probsmda=(float(osma)+1)/(contA+5)
probsfdb=(float(osfb)+1)/(contB+5)
probsmdb=(float(osmb)+1)/(contB+5)
probsfdc=(float(osfc)+1)/(contC+5)
probsmdc=(float(osmc)+1)/(contC+5)
probsfdx=(float(osfx)+1)/(contX+5)
probsmdx=(float(osmx)+1)/(contX+5)
probsfdy=(float(osfy)+1)/(contY+5)
probsmdy=(float(osmy)+1)/(contY+5)
probbhda=(float(obha)+1)/(contA+5)
probbnda=(float(obna)+1)/(contA+5)
probblda=(float(obla)+1)/(contA+5)
probbhdb=(float(obhb)+1)/(contB+5)
probbndb=(float(obnb)+1)/(contB+5)
probbldb=(float(oblb)+1)/(contB+5)
probbhdc=(float(obhc)+1)/(contC+5)
probbndc=(float(obnc)+1)/(contC+5)
probbldc=(float(oblc)+1)/(contC+5)
probbhdx=(float(obhx)+1)/(contX+5)
probbndx=(float(obnx)+1)/(contX+5)
probbldx=(float(oblx)+1)/(contX+5)
probbhdy=(float(obhy)+1)/(contY+5)
probbndy=(float(obny)+1)/(contY+5)
probbldy=(float(obly)+1)/(contY+5)
probchda=(float(ocha)+1)/(contA+5)
probcnda=(float(ocna)+1)/(contA+5)
probclda=(float(ocla)+1)/(contA+5)
probchdb=(float(ochb)+1)/(contB+5)
probcndb=(float(ocnb)+1)/(contB+5)
probcldb=(float(oclb)+1)/(contB+5)
probchdc=(float(ochc)+1)/(contC+5)
probcndc=(float(ocnc)+1)/(contC+5)
probcldc=(float(oclc)+1)/(contC+5)
probchdx=(float(ochx)+1)/(contX+5)
probcndx=(float(ocnx)+1)/(contX+5)
probcldx=(float(oclx)+1)/(contX+5)
probchdy=(float(ochy)+1)/(contY+5)
probcndy=(float(ocny)+1)/(contY+5)
probcldy=(float(ocly)+1)/(contY+5)

#CREAMOS VECTORES PARA EVITAR GRANDES FILAS DE DATOS
vectorcondicionalA=[probsfda, probsmda, probbhda, probbnda, probblda, probchda, probcnda, probclda]
vectorcondicionalB=[probsfdb, probsmdb, probbhdb, probbndb, probbldb, probchdb, probcndb, probcldb]
vectorcondicionalC=[probsfdc, probsmdc, probbhdc, probbndc, probbldc, probchdc, probcndc, probcldc]
vectorcondicionalX=[probsfdx, probsmdx, probbhdx, probbndx, probbldx, probchdx, probcndx, probcldx]
vectorcondicionalY=[probsfdy, probsmdy, probbhdy, probbndy, probbldy, probchdy, probcndy, probcldy]    

#EXPORTAR
df_condicional = pd.DataFrame([vectorcondicionalA, vectorcondicionalB, vectorcondicionalC, vectorcondicionalX, vectorcondicionalY], index = ['drugA', 'drugB', 'drugC', 'drugX', 'drugY'])

datosCondicional = np.asarray(df_condicional)
np.savetxt("condicional.csv",
            datosCondicional,
            delimiter=",")
#MEDIA
mediaEdadA = contEdadA/contA
mediaNaKA = contNaKA/contA


mediaEdadB = contEdadB/contB
mediaNaKB = contNaKB/contB


mediaEdadC = contEdadC/contC
mediaNaKC = contNaKC/contC


mediaEdadX = contEdadX/contX
mediaNaKX = contNaKX/contX


mediaEdadY = contEdadY/contY
mediaNaKY = contNaKY/contY


desvEstEdadA = desviacionEstandar(mediaEdadA, contA, contDesvEdadA)
desvEstNaKA = desviacionEstandar(mediaNaKA, contA, contDesvNaKA)


desvEstEdadB = desviacionEstandar(mediaEdadB, contB, contDesvEdadB)
desvEstNaKB = desviacionEstandar(mediaNaKB, contB, contDesvNaKB)


desvEstEdadC = desviacionEstandar(mediaEdadC, contC, contDesvEdadC)
desvEstNaKC = desviacionEstandar(mediaNaKC, contC, contDesvNaKC)


desvEstEdadX = desviacionEstandar(mediaEdadX, contX, contDesvEdadX)
desvEstNaKX = desviacionEstandar(mediaNaKX, contX, contDesvNaKX)


desvEstEdadY = desviacionEstandar(mediaEdadY, contY, contDesvEdadY)
desvEstNaKY = desviacionEstandar(mediaNaKY, contY, contDesvNaKY)


continuasA =[mediaEdadA, desvEstEdadA, mediaNaKA, desvEstNaKA]
continuasB =[mediaEdadB, desvEstEdadB, mediaNaKB, desvEstNaKB]
continuasC =[mediaEdadC, desvEstEdadC, mediaNaKC, desvEstNaKC]
continuasX =[mediaEdadX, desvEstEdadX, mediaNaKX, desvEstNaKX]
continuasY =[mediaEdadY, desvEstEdadY, mediaNaKY, desvEstNaKY]

df_continuas = pd.DataFrame([continuasA, continuasB, continuasC, continuasX, continuasY], index = ['drugA', 'drugB', 'drugC', 'drugX', 'drugY'])

datosCont = np.asarray(df_continuas)
np.savetxt("continuas.csv",
            datosCont,
            delimiter=",")