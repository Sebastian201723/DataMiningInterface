# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:53:31 2018

@author: LONOVO
"""
import pandas as pd
import math 
#import numpy as np

dfApriori = pd.read_csv('apriori.csv')
dfCondicional = pd.read_csv('condicional.csv')
dfContinuas = pd.read_csv('continuas.csv')

def distNormal(x,mean,stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev)) * exponent

def ProbTotal(ProbApriori, ProbCondS, ProbCondBP, ProbCondCh, ProbNormalEdad,ProbNormalNak):
        return 10**(math.log10(ProbApriori)+math.log10(ProbCondS)+math.log10(ProbCondBP)+math.log10(ProbCondCh)+math.log10(ProbNormalEdad)+math.log10(ProbNormalNak))
    

#List Recovery
DrugACond = dfCondicional.iloc[0].tolist()
DrugBCond = dfCondicional.iloc[1].tolist()
DrugCCond = dfCondicional.iloc[2].tolist()
DrugXCond = dfCondicional.iloc[3].tolist()
DrugYCond = dfCondicional.iloc[4].tolist()


ContDrugA = dfContinuas.iloc[0].tolist()
ContDrugB = dfContinuas.iloc[1].tolist()
ContDrugC = dfContinuas.iloc[2].tolist()
ContDrugX = dfContinuas.iloc[3].tolist()
ContDrugY = dfContinuas.iloc[4].tolist()

#with open("AgeText.txt") as f:
 #   VEdad = map(float,f)   
#VEdad = int(open("AgeText.txt","r"))
ValorRes = open("rest.txt","r")
#contenido = ValorRes.read()
cont = 0
for linea in ValorRes:
    if cont == 0:
        VEdad = float(linea[:-1])
        print("Edad: ", VEdad)
    if cont == 1:
        VSexo = linea[:-1]
    if cont  == 2:
        VBP = linea[:-1]
    if cont == 3:
        VCh = linea[:-1]
    if cont == 4:
        VNaK = float(linea[:-1])
        print("VNak: ", VNaK)
    cont = cont + 1
Valores = [VEdad, VSexo, VBP, VCh, VNaK]

#SEXO
probSA=0
probSB=0
probSC=0
probSX=0
probSY=0

#BP
probBPA=0
probBPB=0
probBPC=0
probBPX=0
probBPY=0

#CH ALTO
probCHA=0
probCHB=0
probCHC=0
probCHX=0
probCHY=0

if (VSexo) == 'F':
    #SEXO CONDICIONAL FEMENINO
    probSA=DrugACond[1]
    probSB=DrugBCond[1]
    probSC=DrugCCond[1]
    probSX=DrugXCond[1]
    probSY=DrugYCond[1]

elif (VSexo)=='M':
    #SEXO CONDICIONAL MASCULINO
    probSA=DrugACond[2]
    probSB=DrugBCond[2]
    probSC=DrugCCond[2]
    probSX=DrugXCond[2]
    probSY=DrugYCond[2]

if (VBP) == 'HIGH':
    #BP CONDICIONAL ALTA
    probBPA=DrugACond[3]
    probBPB=DrugBCond[3]
    probBPC=DrugCCond[3]
    probBPX=DrugXCond[3]
    probBPY=DrugYCond[3]
    
elif (VBP) == 'NORMAL':
    #VP COND NORMAL
    probBPA=DrugACond[4]
    probBPB=DrugBCond[4]
    probBPC=DrugCCond[4]
    probBPX=DrugXCond[4]
    probBPY=DrugYCond[4]
    
elif(VBP) == 'LOW':
    #VP COND BAJA
    probBPA=DrugACond[5]
    probBPB=DrugBCond[5]
    probBPC=DrugCCond[5]
    probBPX=DrugXCond[5]
    probBPY=DrugYCond[5]

if (VCh) == 'HIGH':
    #CH COND ALTA
    probCHA=DrugACond[6]
    probCHB=DrugBCond[6]
    probCHC=DrugCCond[6]
    probCHX=DrugXCond[6]
    probCHY=DrugYCond[6]
elif (VCh) == 'NORMAL':
    #CH COND NORMAL
    probCHA=DrugACond[7]
    probCHB=DrugBCond[7]
    probCHC=DrugCCond[7]
    probCHX=DrugXCond[7]
    probCHY=DrugYCond[7]
elif (VCh) == 'LOW':
    #CH COND BAJA
    probCHA=DrugACond[8]
    probCHB=DrugBCond[8]
    probCHC=DrugCCond[8]
    probCHX=DrugXCond[8]
    probCHY=DrugYCond[8]
# Valores TABLA 3
MediaEdadDA = ContDrugA[1]
MediaNaKDA  = ContDrugA[3]
VarEdadDA = ContDrugA[2]
VarNakDA = ContDrugA[4]

MediaEdadDB = ContDrugB[1]
MediaNaKDB  = ContDrugB[3]
VarEdadDB = ContDrugB[2]
VarNakDB = ContDrugB[4]

MediaEdadDC = ContDrugC[1]
MediaNaKDC  = ContDrugC[3]
VarEdadDC = ContDrugC[2]
VarNakDC = ContDrugC[4]

MediaEdadDX = ContDrugX[1]
MediaNaKDX  = ContDrugX[3]
VarEdadDX = ContDrugX[2]
VarNakDX = ContDrugX[4]

MediaEdadDY = ContDrugY[1]
MediaNaKDY  = ContDrugY[3]
VarEdadDY = ContDrugY[2]
VarNakDY = ContDrugY[4]    

#DistNormal

ProbDistNormalDAEdad = distNormal(VEdad, MediaEdadDA, VarEdadDA )
ProbDistNormalDANak = distNormal(VNaK, MediaNaKDA, VarNakDA )
ProbDistNormalDBEdad = distNormal(VEdad, MediaEdadDB, VarEdadDB )
ProbDistNormalDBNak = distNormal(VNaK, MediaNaKDB, VarNakDB )
ProbDistNormalDCEdad = distNormal(VEdad, MediaEdadDC, VarEdadDC )
ProbDistNormalDCNak = distNormal(VNaK, MediaNaKDC, VarNakDC )
ProbDistNormalDXEdad = distNormal(VEdad, MediaEdadDX, VarEdadDX )
ProbDistNormalDXNak = distNormal(VNaK, MediaNaKDX, VarNakDX )
ProbDistNormalDYEdad = distNormal(VEdad, MediaEdadDY, VarEdadDY )
ProbDistNormalDYNak = distNormal(VNaK, MediaNaKDY, VarNakDY )

#Valores a priori
p1 = dfApriori.iloc[0].tolist()
p2 = dfApriori.iloc[1].tolist()
p3 = dfApriori.iloc[2].tolist()
p4 = dfApriori.iloc[3].tolist()
p5 = dfApriori.iloc[4].tolist()

#Recuperamos ProbApriori, quitamos columnas de drogas
probAprioriA = p1[1]
probAprioriB = p2[1]
probAprioriC = p3[1]
probAprioriX = p4[1]
probAprioriY = p5[1]

#Calculamos la probabilidad total:
ProbTotal1 = ProbTotal(probAprioriA,probSA,probBPA,probCHA,ProbDistNormalDAEdad,ProbDistNormalDANak)
ProbTotal2 = ProbTotal(probAprioriB,probSB,probBPB,probCHB,ProbDistNormalDBEdad,ProbDistNormalDBNak)
ProbTotal3 = ProbTotal(probAprioriC,probSC,probBPC,probCHC,ProbDistNormalDCEdad,ProbDistNormalDCNak)
ProbTotal4 = ProbTotal(probAprioriX,probSX,probBPX,probCHX,ProbDistNormalDXEdad,ProbDistNormalDXNak)
ProbTotal5 = ProbTotal(probAprioriY,probSY,probBPY,probCHY,ProbDistNormalDYEdad,ProbDistNormalDYNak)

#Normalizacion de la prob total
SumTotal = ProbTotal1 + ProbTotal2 +ProbTotal3 +ProbTotal4 +ProbTotal5 
TOTALProbTotal1N = ProbTotal1 *100/ SumTotal
TOTALProbTotal2N = ProbTotal2 *100/ SumTotal
TOTALProbTotal3N = ProbTotal3 *100/ SumTotal
TOTALProbTotal4N = ProbTotal4 *100/ SumTotal
TOTALProbTotal5N = ProbTotal5 *100/ SumTotal

#Determinamos la prob mas alta
ClassResul = 0
if TOTALProbTotal1N>TOTALProbTotal2N and TOTALProbTotal1N>TOTALProbTotal2N and TOTALProbTotal1N>TOTALProbTotal3N and TOTALProbTotal1N>TOTALProbTotal4N and TOTALProbTotal1N>TOTALProbTotal5N:
    ClassResul = TOTALProbTotal1N
if TOTALProbTotal2N>TOTALProbTotal3N and TOTALProbTotal2N>TOTALProbTotal4N and TOTALProbTotal2N>TOTALProbTotal5N:
    ClassResul = TOTALProbTotal2N
if TOTALProbTotal3N>TOTALProbTotal4N and TOTALProbTotal3N>TOTALProbTotal5N:
    ClassResul = TOTALProbTotal3N
if TOTALProbTotal4N>TOTALProbTotal5N:
    ClassResul = TOTALProbTotal4N
if TOTALProbTotal5N>TOTALProbTotal4N:
    classResul = TOTALProbTotal5N
    
print("Probabilidades: ", TOTALProbTotal1N )
