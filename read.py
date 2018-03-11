from scipy.io import arff
import pandas as pd
import math

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


def desviacionEstandar(media, totalValores, acumulado):
        
    desviacion = math.sqrt((((1/(totalValores))*acumulado)-(media ** 2))*(-1))
    return desviacion
#leer el dataset
data = arff.loadarff('clasificacion-drug.arff')
df = pd.DataFrame(data[0])

#seleccionar la columna de clases y convertirla en una lista
listaDrogas = df['Drug'].tolist()

listaSexos = df['Sex'].tolist()
listaBP = df['BP'].tolist()
listaCh = df['Cholesterol'].tolist()

listaEdades = df['Age'].tolist()
listaNa = df['Na'].tolist()
listaK = df['K'].tolist()


totalValores=len(listaDrogas)


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

pA = float(contA)/totalValores
pB = float(contB)/totalValores
pC = float(contC)/totalValores
pX = float(contX)/totalValores
pY = float(contY)/totalValores

osfa=osma=obha=obna=obla=ocha=ocna=ocla=0
osfb=osmb=obhb=obnb=oblb=ochb=ocnb=oclb=0
osfc=osmc=obhc=obnc=oblc=ochc=ocnc=oclc=0
osfx=osmx=obhx=obnx=oblx=ochx=ocnx=oclx=0
osfy=osmy=obhy=obny=obly=ochy=ocny=ocly=0
veda=[]
vedb=[]
vedc=[]
vedx=[]
vedy=[]
vnaa=[]
vnab=[]
vnac=[]
vnax=[]
vnay=[]

contEdadA=0
contNaA=0
contKA=0
contDesvEdadA=0
contDesvNaA=0
contDesvKA=0

contEdadB=0
contNaB=0
contKB=0
contDesvEdadB=0
contDesvNaB=0
contDesvKB=0

contEdadC=0
contNaC=0
contKC=0
contDesvEdadC=0
contDesvNaC=0
contDesvKC=0

contEdadX=0
contNaX=0
contKX=0
contDesvEdadX=0
contDesvNaX=0
contDesvKX=0

contEdadY=0
contNaY=0
contKY=0
contDesvEdadY=0
contDesvNaY=0
contDesvKY=0

for i in range(0, totalValores):
    if listaDrogas[i]=="drugA":
         
        contEdadA = contEdadA + listaEdades[i]
        contNaA = contNaA + listaNa[i]
        contKA = contKA + listaK[i]
        contDesvEdadA = contDesvEdadA + (listaEdades[i] ** 2)
        contDesvNaA = contDesvNaA + (listaNa[i] ** 2)
        contDesvKA = contDesvKA + (listaK[i] ** 2)
        
        ppa = condDiscreta(listaSexos, listaBP, listaCh, i)
        osfa=osfa+ppa[0]
        osma=osma+ppa[1]
        obha=obha+ppa[2]
        obna=obna+ppa[3]
        obla=obla+ppa[4]
        ocha=ocha+ppa[5]
        ocna=ocna+ppa[6]
        ocla=ocla+ppa[7]
        
    elif listaDrogas[i]=="drugB":
        
        contEdadB = contEdadB + listaEdades[i]
        contNaB = contNaB + listaNa[i]
        contKB = contKB + listaK[i]
        contDesvEdadB = contDesvEdadB + (listaEdades[i] ** 2)
        contDesvNaB = contDesvNaB + (listaNa[i] ** 2)
        contDesvKB = contDesvKB + (listaK[i] ** 2)
        
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
        contNaC = contNaC + listaNa[i]
        contKC = contKC + listaK[i]
        contDesvEdadC = contDesvEdadC + (listaEdades[i] ** 2)
        contDesvNaC = contDesvNaC + (listaNa[i] ** 2)
        contDesvKC = contDesvKC + (listaK[i] ** 2)
        
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
        contNaX = contNaX + listaNa[i]
        contKX = contKX + listaK[i]
        contDesvEdadX = contDesvEdadX + (listaEdades[i] ** 2)
        contDesvNaX = contDesvNaX + (listaNa[i] ** 2)
        contDesvKX = contDesvKX + (listaK[i] ** 2)
        
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
        contNaY = contNaY + listaNa[i]
        contKY = contKY + listaK[i]
        contDesvEdadY = contDesvEdadY + (listaEdades[i] ** 2)
        contDesvNaY = contDesvNaY + (listaNa[i] ** 2)
        contDesvKY = contDesvKY + (listaK[i] ** 2)
        
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

#MEDIA
mediaEdadA = contEdadA/contA
mediaNaA = contNaA/contA
mediaKA = contKA/contA

mediaEdadB = contEdadB/contB
mediaNaB = contNaB/contB
mediaKB = contKA/contB

mediaEdadC = contEdadC/contC
mediaNaC = contNaC/contC
mediaKC = contKC/contC

mediaEdadX = contEdadX/contX
mediaNaX = contNaX/contX
mediaKX = contKX/contX

mediaEdadY = contEdadY/contY
mediaNaY = contNaA/contY
mediaKY = contKY/contY

desvEstEdadA = desviacionEstandar(mediaEdadA, contA, contDesvEdadA)
desvEstNaA = desviacionEstandar(mediaNaA, contA, contDesvNaA)
desvEstKA = desviacionEstandar(mediaKA, contA, contDesvKA)

desvEstEdadB = desviacionEstandar(mediaEdadB, contB, contDesvEdadB)
desvEstNaB = desviacionEstandar(mediaNaB, contB, contDesvNaB)
desvEstKB = desviacionEstandar(mediaKB, contB, contDesvKB)

desvEstEdadC = desviacionEstandar(mediaEdadC, contC, contDesvEdadC)
desvEstNaC = desviacionEstandar(mediaNaC, contC, contDesvNaC)
desvEstKC = desviacionEstandar(mediaKC, contC, contDesvKC)

desvEstEdadX = desviacionEstandar(mediaEdadX, contX, contDesvEdadX)
desvEstNaX = desviacionEstandar(mediaNaX, contX, contDesvNaX)
desvEstKX = desviacionEstandar(mediaKX, contX, contDesvKX)

desvEstEdadY = desviacionEstandar(mediaEdadY, contY, contDesvEdadY)
desvEstNaY = desviacionEstandar(mediaNaY, contY, contDesvNaY)
desvEstKY = desviacionEstandar(mediaKY, contY, contDesvKY)


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
    listaEd[j] = math.floor(listaEd[j]/precision)  * precision
    



