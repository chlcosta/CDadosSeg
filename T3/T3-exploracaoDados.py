# TAREFA PRÁTICA 3
# ALUNO: CARLOS HUMBERTO / LAERCIO
# Requisitos: 
#    pip install pandas


import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-editado.csv" 

#df = pd.read_csv(DATAFILE_IN,sep=';', encoding='iso-8859-1', low_memory=False) 
df = pd.read_csv(DATAFILE_IN,sep=',', low_memory=False) 

#Remove linha depois do cabecalho com "-----"
df.drop(df.index[0:1], inplace=True)


print('\n################################################')
print('           EXPLORAÇÃO DO DATASET')
print('################################################\n')

qtdRegistros = '{:,}'.format(df.shape[0]).replace(',','.')

print(f'Quantidade registros: ' + qtdRegistros)
print('Qtd colunas/atributos: ' + str(len(df.columns)))


columnsName = df.columns

print('\nCOLUNAS/ATRIBUTOS ORIGINAIS')
print('=========================================')

for n, i in enumerate(columnsName,1):
    print(n, i)


print('\nDISTRIBUIÇÃO DAS AMOSTRAS')
print('=========================================')


#ATENDIMENTO POR ANO
df2 = df.fillna('VAZIO').sort_values(by='ATENDIMENTO_ANO',ascending=False).groupby('ATENDIMENTO_ANO').size().to_frame('QTD')
print(df2)

#Gera grafico
#plt.yticks(np.arange(0, 1000, step=50))
#plt.xticks(np.arange(df2.shape[0]),list(df2.index), rotation=90)
#plt.savefig("grafico01.png")

#OCORRENCIA_DIA_SEMANA
df2 = df.fillna('VAZIO').groupby('OCORRENCIA_DIA_SEMANA').size().to_frame('QTD').sort_values(by='QTD',ascending=False)
pd.set_option('display.max_rows', None)
print('\n')
print(df2)


#ATENDIMENTO POR BAIRRO
df2 = df.fillna('VAZIO').groupby('ATENDIMENTO_BAIRRO_NOME').size().to_frame('QTD').sort_values(by='QTD',ascending=False)
pd.set_option('display.max_rows', None)
print('\n')
print(df2)


#NATUREZA
df2 = df.fillna('VAZIO').groupby('NATUREZA1_DESCRICAO').size().to_frame('QTD').sort_values(by='QTD',ascending=False)
pd.set_option('display.max_rows', None)
print('\n')
print(df2)


#NATUREZA
df2 = df.fillna('VAZIO').groupby('SUBCATEGORIA1_DESCRICAO').size().to_frame('QTD').sort_values(by='QTD',ascending=False)
pd.set_option('display.max_rows', None)
print('\n')
print(df2)




