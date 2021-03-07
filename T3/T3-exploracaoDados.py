# TAREFA PRÁTICA 3
# ALUNO: CARLOS HUMBERTO / LAERCIO
# Requisitos: 
#   pip install pandas
#   pip install matplotlib
#   pip install humanize


import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


#Arquivo a explorar
#DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-originalcsv" 
DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-editado.csv" 



# EXIBE DISTRIBUICAO POR ATRIBUTO
# ----------------------------------------------------------------
def showDistribuicao(df, atributo, orderByQtd = False, qtdMin = 0):

    if(orderByQtd == False):
        df2 = df.sort_values(by=atributo,ascending=False).groupby(atributo).size().to_frame('QTD')
    else:
        df2 = df.sort_values(by=atributo,ascending=False).groupby(atributo).size().to_frame('QTD').sort_values(by='QTD',ascending=False)
    
    if(qtdMin != 0):
        df2 = df2[df2.QTD > qtdMin]


    pd.set_option('display.max_rows', None)
    print(df2)

# EXIBE REGISTROS DE DETERMINADO BAIRRO
# ----------------------------------------------------------------
def showRegistrosbyBairro(df, bairro):
    df2 = df.loc[df['ATENDIMENTO_BAIRRO_NOME'] == bairro]
    pd.set_option('display.max_rows', None)
    print(df2)


# EXIBE REGISTROS DE DETERMINADA NATUREZA DE OCORRENCIA
# ----------------------------------------------------------------
def showRegistrosbyNatureza(df, n):
    df2 = df.loc[df['NATUREZA1_DESCRICAO'] == n]
    pd.set_option('display.max_rows', None)
    print(df2)    







# ================================================================
# INICIO DO PROGRAMA
# ================================================================

if __name__ == '__main__':

    df = pd.read_csv(DATAFILE_IN,sep=',', low_memory=False) 


    print('\n################################################')
    print('           EXPLORAÇÃO DO DATASET')
    print('################################################\n')

    #Preview de registros e colunas
    qtdRegistros = '{:,}'.format(df.shape[0]).replace(',','.')
    print('Quantidade registros: ' + qtdRegistros)
    print('Qtd colunas/atributos: ' + str(len(df.columns)))


    #Exibe atributos do dataset
    print('\nCOLUNAS/ATRIBUTOS ORIGINAIS')
    print('=========================================')
    for n, i in enumerate(df.columns,1):
        print(n, i)



    print('\nDISTRIBUIÇÃO DAS AMOSTRAS')
    print('=========================================')

    showDistribuicao(df, 'ATENDIMENTO_ANO')
    showDistribuicao(df, 'OCORRENCIA_MES')
    showDistribuicao(df, 'OCORRENCIA_DIA_SEMANA')
    showDistribuicao(df, 'OCORRENCIA_PERIODO')
    showDistribuicao(df, 'OCORRENCIA_DIA')
    showDistribuicao(df, 'ATENDIMENTO_BAIRRO_NOME',True)
    showDistribuicao(df, 'REGIONAL_FATO_NOME')
    showDistribuicao(df, 'NATUREZA1_DESCRICAO', True)
    showDistribuicao(df, 'SUBCATEGORIA1_DESCRICAO', True)
    showDistribuicao(df, 'EQUIPAMENTO_URBANO_NOME', True, 500)    
    showDistribuicao(df, 'ORIGEM_CHAMADO_DESCRICAO')
    


    
    #df['OCORRENCIA_DATA'] = df.loc[df.OCORRENCIA_DATA != '']['OCORRENCIA_DATA'].apply(lambda x: datetime.datetime.strptime(x[:-4], '%Y-%m-%d %H:%M:%S'))
    #df['OCORRENCIA_HORA'] = df.loc[df.OCORRENCIA_HORA != '']['OCORRENCIA_HORA'].apply(lambda x: datetime.datetime.strptime(x, '%H:%M:%S'))    
    
    
    #showRegistrosbyNatureza(df,'Sedução')
    #print(df.loc[244158])
    #print(df.loc[130098])
    #showRegistrosbyBairro(df, 'ÁGUAS BELAS')
    
    

'''

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

valueY = df2.index.tolist()[:30]
valueX = df2['QTD'].tolist()[:30]

# Figure Size 
fig, ax = plt.subplots(figsize =(12, 16)) 

# Horizontal Bar Plot 
ax.barh(valueY, valueX) 

# Remove axes splines 
for s in ['top', 'bottom', 'left', 'right']: 
    ax.spines[s].set_visible(False) 
  
# Remove x, y Ticks 
ax.xaxis.set_ticks_position('none') 
ax.yaxis.set_ticks_position('none') 
  
# Add padding between axes and labels 
ax.xaxis.set_tick_params(pad = 5) 
ax.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines 
ax.grid(b = True, color ='grey', 
        linestyle ='-.', linewidth = 0.5, 
        alpha = 0.2) 
  
# Show top values  
ax.invert_yaxis() 

# Add annotation to bars 
for i in ax.patches: 
    plt.text(i.get_width()+1500, i.get_y()+0.5,  
             str(round((i.get_width()),2)), 
             fontsize = 10, fontweight ='bold', 
             color ='grey') 

plt.savefig("grafico01.png")
exit()

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


'''

