# TAREFA PRÁTICA 3
# ALUNO: CARLOS HUMBERTO / LAERCIO
# Requisitos: 
#   pip install pandas
#   pip install matplotlib
#   pip install humanize
#   pip install xlsxwriter

import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime


#Arquivo a explorar
#DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-originalcsv" 
DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-editado-10OC.csv" 

#Arquivo XLS com as saidas
xlsOut = pd.ExcelWriter('relatorios.xlsx', engine='xlsxwriter')




# EXIBE DISTRIBUICAO POR ATRIBUTO
# ----------------------------------------------------------------
def showDistribuicao(df, atributo, orderByQtd = False, qtdMin = 0):

    global xlsOut

    if(orderByQtd == False):
        df2 = df.sort_values(by=atributo,ascending=False).groupby(atributo).size().to_frame('QTD')
    else:
        df2 = df.sort_values(by=atributo,ascending=False).groupby(atributo).size().to_frame('QTD').sort_values(by='QTD',ascending=False)
    
    if(qtdMin != 0):
        df2 = df2[df2.QTD > qtdMin]

    pd.set_option('display.max_rows', None)

    df2.to_excel(xlsOut, sheet_name=atributo)

    print(df2)



# EXIBE REGISTROS DE DETERMINADO BAIRRO
# ----------------------------------------------------------------
def showRegistrosbyBairro(df, bairro):
    df2 = df.loc[df['OC_BAIRRO'] == bairro]
    pd.set_option('display.max_rows', None)
    print(df2)


# EXIBE REGISTROS DE DETERMINADA NATUREZA DE OCORRENCIA
# ----------------------------------------------------------------
def showRegistrosbyNatureza(df, n):
    df2 = df.loc[df['OC_CATEGORIA'] == n]
    pd.set_option('display.max_rows', None)
    print(df2)    


# EXIBE HEATMAP DIA X ANO
# ----------------------------------------------------------------
def showHeatmapDiaAno(df):

    global xlsOut

    pd.set_option('display.max_rows', None)
    
    df1 = df.loc[df['OC_MES'] == 1].groupby('OC_DIA').size().to_frame('JAN')        
    df2 = df.loc[df['OC_MES'] == 2].groupby('OC_DIA').size().to_frame('FEV')            
    df3 = df.loc[df['OC_MES'] == 3].groupby('OC_DIA').size().to_frame('MAR')            
    df4 = df.loc[df['OC_MES'] == 4].groupby('OC_DIA').size().to_frame('ABR')
    df5 = df.loc[df['OC_MES'] == 5].groupby('OC_DIA').size().to_frame('MAI')
    df6 = df.loc[df['OC_MES'] == 6].groupby('OC_DIA').size().to_frame('JUN')
    df7 = df.loc[df['OC_MES'] == 7].groupby('OC_DIA').size().to_frame('JUL')
    df8 = df.loc[df['OC_MES'] == 8].groupby('OC_DIA').size().to_frame('AGO')
    df9 = df.loc[df['OC_MES'] == 9].groupby('OC_DIA').size().to_frame('SET')
    df10 = df.loc[df['OC_MES'] == 10].groupby('OC_DIA').size().to_frame('OUT')
    df11 = df.loc[df['OC_MES'] == 11].groupby('OC_DIA').size().to_frame('NOV')
    df12 = df.loc[df['OC_MES'] == 12].groupby('OC_DIA').size().to_frame('DEZ')

    dff = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12], axis=1)
    dff = dff.fillna(0).astype(int)

    print('HEATMAP DIA X ANO')
    print(dff)

    dff.to_excel(xlsOut, sheet_name='HEATMAP-DIA-ANO') 
    

# EXIBE TENDENCIAS DAS PRINCIPAIS OCORRÊNCIAS
# ----------------------------------------------------------------
def showTendenciasOcorrencias(df):

    global xlsOut

    lista = sorted(df['OC_SUBCATEGORIA_TXT'].unique().tolist())

    dfs = []
    for i in lista:
        dfs.append(df.loc[df['OC_SUBCATEGORIA_TXT'] == i].groupby('OC_ANO').size().to_frame(i))

    
    pd.set_option('display.max_rows', None)

    dff = pd.concat(dfs, axis=1)
    dff = dff.fillna(0).astype(int)

    print('TENDENCIAS DAS PRINCIPAIS OCORRÊNCIAS')
    print(dff)

    dff.to_excel(xlsOut, sheet_name='TENDENCIAS-OCORRENCIAS')    

    #Forma mais imples
    #df.pivot_table(index='OC_ANO', columns='OC_SUBCATEGORIA_TXT',aggfunc='size',fill_value=0)

        


# EXIBE TENDENCIA ANUAL DE DETERMINADA OCORRENCIA
# ----------------------------------------------------------------
def showTendenciaByOcorrencia(df,subcat):

    global xlsOut

    pd.set_option('display.max_rows', None)
    
    df1 = df.loc[df['OC_SUBCATEGORIA'] == subcat].groupby('OC_ANO').size().to_frame('QTD')        
    df1 = df1.fillna(0).astype(int)

    print('TENDENCIAS POR OCORRENCIA: ' + subcat)
    print(df1)
    


# EXIBE TENDENCIA DE CADA OCORRENCIA POR ANO E PERIODO DO DIA
# ----------------------------------------------------------------
def showTendenciasOcorrenciasAnoPeriodoDia(df):

    global xlsOut

    df1 = df.pivot_table(index='OC_ANO', 
               columns=['OC_SUBCATEGORIA_TXT','OC_PERIODO_DIA_TXT'],
               aggfunc='size',
               fill_value=0)

    print('TENDENCIAS DE OCORRENCIAS POR ANO E PERIODO DO DIA: ')
    print(df1)

    df1.to_excel(xlsOut, sheet_name='TENDENCIAS-OC-ANO-PERIODO')    



# EXIBE A CLASSE DE VALORES DE TODAS AS COLUNAS
# ----------------------------------------------------------------
def showClassesColunas():
    global df

    print('\n> EXIBE AS CLASSES DAS COLUNAS...')

    for n, i in enumerate(df.columns,1):
        lista = sorted(df[i].unique().tolist())
        print('\n%s - %s (Qtd:%s)' % (n, i, len(lista)))      
        print('  %s' % lista)





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
    showDistribuicao(df, 'OC_ANO')
    showDistribuicao(df, 'OC_MES')
    showDistribuicao(df, 'OC_DIA_SEMANA_TXT')
    showDistribuicao(df, 'OC_PERIODO_DIA_TXT')
    showDistribuicao(df, 'OC_DIA')
    showDistribuicao(df, 'OC_BAIRRO_TXT',True)
    showDistribuicao(df, 'OC_SUBCATEGORIA_TXT', True)
    #showDistribuicao(df, 'OC_EQUIPAMENTO_URBANO', True, 500)    
    #showDistribuicao(df, 'OC_ORIGEM_CHAMADO')
    #showHeatmapDiaAno(df)
    #showTendenciasOcorrencias(df)
    showTendenciasOcorrencias(df)
    showTendenciasOcorrenciasAnoPeriodoDia(df)
    showClassesColunas()

    #Salva relatorio
    xlsOut.save()


    #showTendenciaByOcorrencia(df,'Pichação')
    #showRegistrosbyNatureza(df,'Natureza da Ocorrencia')
    #print(df.loc[244158])
    #print(df.loc[130098])
    #showRegistrosbyBairro(df, 'ÁGUAS BELAS')
    
  
