# TAREFA PRÁTICA 3 - PRE-PROCESSAMENTO
# ALUNO: CARLOS HUMBERTO / LAERCIO
# Requisitos: 
#    pip install pandas
#
# Script gera 2 arquivos de saida, um dataset para análise e um dataset final para construção de modelos


import os, sys
from pathlib import Path
import pandas as pd
import humanize 

DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-original.csv" 
DATAFILE_OUT = "dataset/2021-02-01-sigesguarda-editado-10OC.csv" 

df = pd.read_csv(DATAFILE_IN,sep=';', encoding='iso-8859-1', low_memory=False) 




# REMOVE LINHAS ESPECIFICAS
# ----------------------------------------------------------------
def removeLinhas():
    global df
    print('\n> REMOVENDO LINHAS...')
    qtdLinhasAntes = '{:,}'.format(df.shape[0]).replace(',','.')
    print('  Linhas Antes: ' + qtdLinhasAntes)

    #DELETA linha "----"
    df.drop(df.index[0:1], inplace=True)

    #DELETA linhas de determinados bairros inconsistentes
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'BAIRRO FICTÍCIO')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'BAIRRO NAO INFORMADO')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'BAIRRO NÃO LOCALIZAD')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'NF')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'NI')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'NÃO ENCONTRADO')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'NÃO INFORMADO')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'INDICAÇÕES CANCELADA')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'MAUA')].index , inplace=True)

    #DELETA regiao metropolitana, mantem apenas Curitiba
    df.drop(df[(df['REGIONAL_FATO_NOME'] == 'REGIÃO METROPOLITANA')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'CAMPO LARGO')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'MARACANÃ')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'LOTEAMENTO SÃO GERÔN')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'COLONIA FARIA')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'COLONIA SAO VENANCIO')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'JARDIM BELA VISTA')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'JARDIM SANTA MÔNICA')].index , inplace=True)
    df.drop(df[(df['ATENDIMENTO_BAIRRO_NOME'] == 'JR TAISA')].index , inplace=True)

    #DELETA registros com valores nulos nas colunas abaixo
    colunaNaoNula = ['ATENDIMENTO_ANO','ATENDIMENTO_BAIRRO_NOME', 'SUBCATEGORIA1_DESCRICAO','REGIONAL_FATO_NOME','OCORRENCIA_HORA']
    df.dropna(subset=colunaNaoNula, inplace=True)    

    qtdLinhasDepois = '{:,}'.format(df.shape[0]).replace(',','.')
    print('  Linhas Depois: ' + qtdLinhasDepois)



# REMOVE COLUNAS ESPECIFICAS
# ----------------------------------------------------------------
def removeColunas():
    global df
    print('\n> REMOVENDO COLUNAS...')

    print('   Colunas Antes:')
    for n, i in enumerate(df.columns,1):
        print('  %s %s' % (n, i))


    #REMOVE COLUNAS desonsideradas para o tipo de analise
    colunasRemover = ['NATUREZA2_DESCRICAO', 'NATUREZA3_DESCRICAO','NATUREZA4_DESCRICAO', 'NATUREZA5_DESCRICAO',
    'SUBCATEGORIA2_DESCRICAO', 'SUBCATEGORIA3_DESCRICAO','SUBCATEGORIA4_DESCRICAO', 'SUBCATEGORIA5_DESCRICAO',
    'NATUREZA1_DEFESA_CIVIL', 'NATUREZA2_DEFESA_CIVIL','NATUREZA3_DEFESA_CIVIL', 'NATUREZA4_DEFESA_CIVIL','NATUREZA5_DEFESA_CIVIL',
    'FLAG_EQUIPAMENTO_URBANO', 'FLAG_FLAGRANTE','OPERACAO_DESCRICAO', 'SECRETARIA_NOME', 'SECRETARIA_SIGLA', 
    'SERVICO_NOME','SITUACAO_EQUIPE_DESCRICAO', 'NUMERO_PROTOCOLO_156', 'OCORRENCIA_CODIGO','OCORRENCIA_ANO',
    'LOGRADOURO_NOME', 'NATUREZA1_DESCRICAO', 'EQUIPAMENTO_URBANO_NOME', 'ORIGEM_CHAMADO_DESCRICAO',
    'REGIONAL_FATO_NOME'
    ]

    for v in colunasRemover:
        df.drop(v, axis=1, inplace=True)

    print('\n   Colunas Depois:')
    for n, i in enumerate(df.columns,1):
        print('  %s %s' % (n, i))        



#ALTERA registros inconsistentes
# ----------------------------------------------------------------
def alteraValoresInconsistentes():
    global df
    print('\n> ALTERA VALORES INCONSISTENTES...')

    #df.fillna('NAO-INFORMADO', inplace = True)

    #df.loc[119260,'ATENDIMENTO_BAIRRO_NOME'] = 'BOQUEIRÃO'
    #df.loc[119598,'ATENDIMENTO_BAIRRO_NOME'] = 'TINGUI'
    #df.loc[246657,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
    #df.loc[262558,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
    #df.loc[277992,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
    #df.loc[307562,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
    #df.loc[148557,'REGIONAL_FATO_NOME'] = 'CAJURU'
    #df.loc[127463,'REGIONAL_FATO_NOME'] = 'PINHEIRINHO'
    #df.loc[130875,'REGIONAL_FATO_NOME'] = 'PORTÃO'

    #Melhora valores da coluna ORIGEM_CHAMADO_DESCRICAO
    #df.ORIGEM_CHAMADO_DESCRICAO.replace(['NÃO CADASTRAR "ANTIGO SIGA"'], ['ANTIGO SIGA'], inplace=True)
    #df.ORIGEM_CHAMADO_DESCRICAO.replace(['SIGA'], ['ANTIGO SIGA'], inplace=True)
    #df.ORIGEM_CHAMADO_DESCRICAO.replace(['VAZIO "NÃO CADASTRAR" ANTIGO AOS GMS'], ['ANTIGO GMS'], inplace=True)
    #df.ORIGEM_CHAMADO_DESCRICAO.replace(['AOS GMS'], ['ANTIGO GMS'], inplace=True)
    #df.ORIGEM_CHAMADO_DESCRICAO.replace(['À VIATURA'], ['VIATURA'], inplace=True)
    #df.ORIGEM_CHAMADO_DESCRICAO.replace(['CIOSP (190)'], ['190'], inplace=True)



#ALTERA registros inconsistentes
# ----------------------------------------------------------------
def alteraValoresDiaSemana():
    global df

    print('\n> ALTERA VALORES INCONSISTENTES NO \'DIA DA SEMANA\'...')
    df.OCORRENCIA_DIA_SEMANA.replace(['DOMINGO'], ['1-DOMINGO'], inplace=True)
    df.OCORRENCIA_DIA_SEMANA.replace(['SEGUNDA'], ['2-SEGUNDA'], inplace=True)
    df.OCORRENCIA_DIA_SEMANA.replace(['TERÇA'], ['3-TERCA'], inplace=True)
    df.OCORRENCIA_DIA_SEMANA.replace(['QUARTA'], ['4-QUARTA'], inplace=True)
    df.OCORRENCIA_DIA_SEMANA.replace(['QUINTA'], ['5-QUINTA'], inplace=True)
    df.OCORRENCIA_DIA_SEMANA.replace(['SEXTA'], ['6-SEXTA'], inplace=True)
    df.OCORRENCIA_DIA_SEMANA.replace(['SÁBADO'], ['7-SABADO'], inplace=True)

    #Altera tambem o nome da coluna
    df.rename(columns = {"OCORRENCIA_DIA_SEMANA":'OC_DIA_SEMANA_TXT'}, inplace = True)


#CRIA coluna Dia Semana no formato Numerico
# ----------------------------------------------------------------
def criaColunaDiaSemanaNumerico():
    global df

    print('\n> CRIA ATRIBUTO \'DIA DA SEMANA\' NUMERICO...')

    df['OC_DIA_SEMANA'] = df['OC_DIA_SEMANA_TXT']
    
    df.OC_DIA_SEMANA.replace(['1-DOMINGO'], [1], inplace=True)
    df.OC_DIA_SEMANA.replace(['2-SEGUNDA'], [2], inplace=True)
    df.OC_DIA_SEMANA.replace(['3-TERCA'], [3], inplace=True)
    df.OC_DIA_SEMANA.replace(['4-QUARTA'], [4], inplace=True)
    df.OC_DIA_SEMANA.replace(['5-QUINTA'], [5], inplace=True)
    df.OC_DIA_SEMANA.replace(['6-SEXTA'], [6], inplace=True)
    df.OC_DIA_SEMANA.replace(['7-SABADO'], [7], inplace=True)
 


# FUNCAO AUXILIAR PARA DEFINIR PERIODO DO DIA
# ----------------------------------------------------------------
def auxDefinePeriodoDia(x):    
    hora = int(x[:2])
    
    if (hora >= 0) and (hora <= 6):
        return '4-MADRUGADA'
    elif (hora > 6) and (hora <= 12 ):
        return '1-MANHA'
    elif (hora > 12) and (hora <= 18):
        return'2-TARDE'
    elif (hora > 18) and (hora <= 24) :
        return '3-NOITE'



#CRIA colunas periodo do dia no formato texto e numerico 
#A madrugada vai da zero hora às 6h. A manhã, das 6h às 12h (ou ao meio-dia). 
#A tarde, das 12h às 18h. A noite, das 18h às 24h (ou meia-noite).
#https://www12.senado.leg.br/manualdecomunicacao/redacao-e-estilo/estilo/hora
# ----------------------------------------------------------------
def criaColunasPeriodoDia():
    global df

    print('\n> CRIA COLUNAS PARA PERIODO DO DIA NO FORMATO TEXTO E NUMERICO')
    df['OC_PERIODO_DIA_TXT'] = df['OCORRENCIA_HORA'].apply(auxDefinePeriodoDia)
    df['OC_PERIODO_DIA'] = df['OC_PERIODO_DIA_TXT']

    df.OC_PERIODO_DIA.replace(['4-MADRUGADA'], [4], inplace=True)
    df.OC_PERIODO_DIA.replace(['1-MANHA'], [1], inplace=True)
    df.OC_PERIODO_DIA.replace(['2-TARDE'], [2], inplace=True)
    df.OC_PERIODO_DIA.replace(['3-NOITE'], [3], inplace=True)

    #Remove coluna OCORRENCIA_DATA
    df.drop(['OCORRENCIA_HORA'], axis=1, inplace=True)



# EXIBE A CLASSE DE VALORES DE TODAS AS COLUNAS
# ----------------------------------------------------------------
def showClassesColunas():
    global df

    print('\n> EXIBE AS CLASSES DAS COLUNAS...')

    for n, i in enumerate(df.columns,1):
        print('\n%s - %s' % (n, i))      
        print('  %s' % sorted(df[i].unique().tolist()))



# CRIA colunas dia (1 a 31)
# ----------------------------------------------------------------
def criaColunaDia():
    global df

    print('\n> CRIA COLUNA DIA (1 a 31)...')
    df['OC_DIA'] = df['OCORRENCIA_DATA'].apply(lambda x: int(x[8:10]))

    #Remove coluna OCORRENCIA_DATA
    df.drop(['OCORRENCIA_DATA'], axis=1, inplace=True)



#CRIA coluna Bairro no formato Numerico
# ----------------------------------------------------------------
def criaColunaBairroNumerico():
    global df

    print('\n> CRIA ATRIBUTO \'BAIRRO\' NUMERICO...')
    bairro = df["ATENDIMENTO_BAIRRO_NOME"].unique()
    bairroDict = {}
    x = 1
    for d in bairro:
        bairroDict[d] = x
        x+=1
    
    df["OC_BAIRRO"] = df["ATENDIMENTO_BAIRRO_NOME"].replace(bairroDict)




#CRIA coluna Subcategoria da Ocorrencia no formato Numerico
# ----------------------------------------------------------------
def criaColunaSubcategoriaNumerico():
    global df

    print('\n> CRIA ATRIBUTO \'SUBCATEGORIA\' NUMERICO...')
    campo = df["SUBCATEGORIA1_DESCRICAO"].unique()
    campoDict = {}
    x = 1
    for d in campo:
        campoDict[d] = x
        x+=1
    
    df["OC_SUBCATEGORIA"] = df["SUBCATEGORIA1_DESCRICAO"].replace(campoDict)



#REORGANIZA colunas (ordem, nomes, exclui outras)
# ----------------------------------------------------------------
def reorganizaColunas():

    global df

    print('\n> REORGANIZA colunas (altera ordem e nomes de colunas)...')
    
    #Altera nomes de colunas
    nomesColunas = {
    "ATENDIMENTO_ANO": "OC_ANO",
    "ATENDIMENTO_BAIRRO_NOME": "OC_BAIRRO_TXT",
    "SUBCATEGORIA1_DESCRICAO": 'OC_SUBCATEGORIA_TXT',
    "OCORRENCIA_MES": 'OC_MES'}
    df.rename(columns = nomesColunas, inplace = True)

    #Altera ordem das colunas
    df = df[['OC_ANO', 'OC_MES', 'OC_DIA_SEMANA', 'OC_DIA_SEMANA_TXT', 'OC_DIA', 'OC_PERIODO_DIA', 'OC_PERIODO_DIA_TXT',
    'OC_BAIRRO','OC_BAIRRO_TXT','OC_SUBCATEGORIA','OC_SUBCATEGORIA_TXT']]



#FILTRA dataset com determinados parametros de Anos e Tipos de Ocorrencias
# ----------------------------------------------------------------
def filtraDataset():

    global df

    print('\n> FILTRA dataset com determinados parametros de Anos e Tipos de Ocorrencias ')

    #Exclui registros de 2021
    df.drop(df[(df['ATENDIMENTO_ANO'] == '2021')].index , inplace=True)

    #Mantem no dataset apenas registros de determinados tipos de ocorrência e que não seja de 2021
    df.drop(df[
        (df.SUBCATEGORIA1_DESCRICAO !=  'Uso de substância ilícita') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Vandalismo') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Pichação') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Disparo de Alarme (violação)') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Cão solto em via pública') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Transporte Coletivo') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Invasão de equipamento/patrimônio público') &    
        (df.SUBCATEGORIA1_DESCRICAO !=  'Desordem') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Arrombamento') &
        (df.SUBCATEGORIA1_DESCRICAO !=  'Estacionamento irregular')].index, inplace=True)

        #(df.SUBCATEGORIA1_DESCRICAO !=  'Estacionamento irregular') &
        #(df.SUBCATEGORIA1_DESCRICAO !=  'Acidente de trânsito') &
        #(df.SUBCATEGORIA1_DESCRICAO !=  'Invasão ao transporte coletivo') &
        #(df.SUBCATEGORIA1_DESCRICAO !=  'Tráfico de drogas') &
        #(df.SUBCATEGORIA1_DESCRICAO !=  'Maus tratos a animais') &
        #(df.SUBCATEGORIA1_DESCRICAO !=  'Tumulto') &
        #(df.SUBCATEGORIA1_DESCRICAO !=  'Porte de substância ilícita')].index, inplace=True)

    #Reorganiza Index
    df.reset_index(drop=True, inplace=True)




#################################################################
# INICIO - PRE-PROCESSAMENTO
#################################################################
print('\n################################################')
print('       PRE-PROCESSAMENTO DE DADOS')
print('################################################\n')

print('Aquivo de entrada: ' + DATAFILE_IN)

#Exibe preview do dataset original
qtdRegistros = '{:,}'.format(df.shape[0]).replace(',','.')
sizeIn = Path(DATAFILE_IN).stat().st_size
print('\nENTRADA:')
print(f'Quantidade registros: ' + qtdRegistros)
print('Qtd colunas/atributos: ' + str(len(df.columns)))
print('Tamanho arquivo:' + str(humanize.naturalsize(sizeIn)))

#Remove Linhas
removeLinhas()

#Remove Colunas
removeColunas()

#ALTERA valores Inconsistentes
alteraValoresInconsistentes()


#ALTERA valores para Dia da Semana
alteraValoresDiaSemana()

#CRIA coluna Dia Semana no formato Numerico
criaColunaDiaSemanaNumerico()

#CRIA colunas periodo do dia no formato 
#texto (1-manha, 2-tarde, 3-noite, 4-madrugada) e 
#numerico (1,2,3,4)
criaColunasPeriodoDia()

#CRIA coluna dia (1 a 31)
criaColunaDia()

#SHOW classes de cada coluna
showClassesColunas()


print('\n> DESCREVE os dados ANTES da filtragem ')
print(df.describe())

#FILTRA dataset com determinados parametros de Anos e Tipos de Ocorrencias
filtraDataset()

#CRIA coluna Bairro no formato Numerico
criaColunaBairroNumerico()

#CRIA coluna Subcategoria da Ocorrencia no formato Numerico
criaColunaSubcategoriaNumerico()

#REORGANIZA colunas (ordem, nomes das colunas)
reorganizaColunas()

print('\n> DESCREVE os dados APOS filtragem ')
print(df.describe())

#SHOW classes de cada coluna
showClassesColunas()


print('\n> PREVIEW dos dados')
print(df)


print('\n> INICIO DE SALVAMENTO DOS DADOS')


#Preview do dataset editado
qtdRegistros = '{:,}'.format(df.shape[0]).replace(',','.')
print('\nSAIDA:')
print(f'Quantidade registros: ' + qtdRegistros)
print('Qtd colunas/atributos: ' + str(len(df.columns)))

print('\nColunas:')
for n, i in enumerate(df.columns,1):
    print('  %s %s' % (n, i))

#Salva dataset editado no formato UTR8
print('\nSalva arquivo de saída: ' + DATAFILE_OUT)
df.to_csv(DATAFILE_OUT, encoding="utf-8", index=False) 

#Verifica se o tamanho do dataset diminuiu
sizeOut = Path(DATAFILE_OUT).stat().st_size
print('Tamanho arquivo:' + str(humanize.naturalsize(sizeOut)))

