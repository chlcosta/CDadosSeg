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
DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-editado.csv" 

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
    df2 = df.loc[df['ATENDIMENTO_BAIRRO_NOME'] == bairro]
    pd.set_option('display.max_rows', None)
    print(df2)


# EXIBE REGISTROS DE DETERMINADA NATUREZA DE OCORRENCIA
# ----------------------------------------------------------------
def showRegistrosbyNatureza(df, n):
    df2 = df.loc[df['NATUREZA1_DESCRICAO'] == n]
    pd.set_option('display.max_rows', None)
    print(df2)    


# EXIBE HEATMAP DIA X ANO
# ----------------------------------------------------------------
def showHeatmapDiaAno(df):

    global xlsOut

    pd.set_option('display.max_rows', None)
    
    df1 = df.loc[df['OCORRENCIA_MES'] == 1].groupby('OCORRENCIA_DIA').size().to_frame('JAN')        
    df2 = df.loc[df['OCORRENCIA_MES'] == 2].groupby('OCORRENCIA_DIA').size().to_frame('FEV')            
    df3 = df.loc[df['OCORRENCIA_MES'] == 3].groupby('OCORRENCIA_DIA').size().to_frame('MAR')            
    df4 = df.loc[df['OCORRENCIA_MES'] == 4].groupby('OCORRENCIA_DIA').size().to_frame('ABR')
    df5 = df.loc[df['OCORRENCIA_MES'] == 5].groupby('OCORRENCIA_DIA').size().to_frame('MAI')
    df6 = df.loc[df['OCORRENCIA_MES'] == 6].groupby('OCORRENCIA_DIA').size().to_frame('JUN')
    df7 = df.loc[df['OCORRENCIA_MES'] == 7].groupby('OCORRENCIA_DIA').size().to_frame('JUL')
    df8 = df.loc[df['OCORRENCIA_MES'] == 8].groupby('OCORRENCIA_DIA').size().to_frame('AGO')
    df9 = df.loc[df['OCORRENCIA_MES'] == 9].groupby('OCORRENCIA_DIA').size().to_frame('SET')
    df10 = df.loc[df['OCORRENCIA_MES'] == 10].groupby('OCORRENCIA_DIA').size().to_frame('OUT')
    df11 = df.loc[df['OCORRENCIA_MES'] == 11].groupby('OCORRENCIA_DIA').size().to_frame('NOV')
    df12 = df.loc[df['OCORRENCIA_MES'] == 12].groupby('OCORRENCIA_DIA').size().to_frame('DEZ')

    dff = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12], axis=1)
    dff = dff.fillna(0).astype(int)

    print('HEATMAP DIA X ANO')
    print(dff)

    dff.to_excel(xlsOut, sheet_name='HEATMAP-DIA-ANO')


# EXIBE TENDENCIAS DAS PRINCIPAIS OCORRÊNCIAS
# ----------------------------------------------------------------
def showTendenciasOcorrencias(df):

    global xlsOut

    pd.set_option('display.max_rows', None)
    
    df1 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Uso de substância ilícita'].groupby('ATENDIMENTO_ANO').size().to_frame('Uso Subs.Ilícitas')        
    df2 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Apoio ao cidadão - PRESTAÇÃO DE SOCORRO/SALVAMENTO'].groupby('ATENDIMENTO_ANO').size().to_frame('Apoio Socorro/Salvamento')            
    df3 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Vandalismo'].groupby('ATENDIMENTO_ANO').size().to_frame('Vandalismo')            
    df4 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Pichação'].groupby('ATENDIMENTO_ANO').size().to_frame('Pichação')
    df5 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Disparo de Alarme (violação)'].groupby('ATENDIMENTO_ANO').size().to_frame('Disparo Alarme')
    df6 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Cão solto em via pública'].groupby('ATENDIMENTO_ANO').size().to_frame('Cão solto')
    df7 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Transeunte'].groupby('ATENDIMENTO_ANO').size().to_frame('Transeunte')
    df8 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Transporte Coletivo'].groupby('ATENDIMENTO_ANO').size().to_frame('Transporte Coletivo')
    df9 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'ORIENTAÇÃO COVID-19'].groupby('ATENDIMENTO_ANO').size().to_frame('Orientação Covid')
    df10 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Apoio ao SAMU'].groupby('ATENDIMENTO_ANO').size().to_frame('Apoio SAMU')
    df11 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Invasão de equipamento/patrimônio público'].groupby('ATENDIMENTO_ANO').size().to_frame('Invasão patrimônio público')
    df12 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Desordem'].groupby('ATENDIMENTO_ANO').size().to_frame('Desordem')
    df13 = df.loc[df['SUBCATEGORIA1_DESCRICAO'] == 'Arrombamento'].groupby('ATENDIMENTO_ANO').size().to_frame('Arrombamento')

    dff = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13], axis=1)
    dff = dff.fillna(0).astype(int)

    print('TENDENCIAS DAS PRINCIPAIS OCORRÊNCIAS')
    print(dff)

    dff.to_excel(xlsOut, sheet_name='TENDENCIAS-OCORRENCIAS')    
    








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
    showHeatmapDiaAno(df)
    showTendenciasOcorrencias(df)
    
    #Salva relatorio
    xlsOut.save()


    #showRegistrosbyNatureza(df,'Natureza da Ocorrencia')
    #print(df.loc[244158])
    #print(df.loc[130098])
    #showRegistrosbyBairro(df, 'ÁGUAS BELAS')
    
  
