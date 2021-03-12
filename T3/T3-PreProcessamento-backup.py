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
DATAFILE_OUT = "dataset/2021-02-01-sigesguarda-editado.csv" 

df = pd.read_csv(DATAFILE_IN,sep=';', encoding='iso-8859-1', low_memory=False) 


# EXIBE REGISTROS DE DETERMINADO BAIRRO
# ----------------------------------------------------------------
def definePeriodoDia(x):
    hora = int(x[:2])
    if (hora > 0) and (hora <= 6):
        return '1-MADRUGADA'
    elif (hora > 8) and (hora <= 12 ):
        return '2-MANHA'
    elif (hora > 12) and (hora <= 18):
        return'3-TARDE'
    elif (hora > 18) and (hora <= 24) :
        return '4-NOITE'



# INICIO - PRE-PROCESSAMENTO
# ----------------------------------------------------------------
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
print('Tamnho arquivo:' + str(humanize.naturalsize(sizeIn)))

#Remove linha depois do cabecalho com "-----"
print('Remove linha abaixo do cabeçalho')
df.drop(df.index[0:1], inplace=True)

#REMOVE COLUNAS desonsideradas para o tipo de analise
colunasRemover = ['NATUREZA2_DESCRICAO', 'NATUREZA3_DESCRICAO','NATUREZA4_DESCRICAO', 'NATUREZA5_DESCRICAO',
'SUBCATEGORIA2_DESCRICAO', 'SUBCATEGORIA3_DESCRICAO','SUBCATEGORIA4_DESCRICAO', 'SUBCATEGORIA5_DESCRICAO',
'NATUREZA1_DEFESA_CIVIL', 'NATUREZA2_DEFESA_CIVIL','NATUREZA3_DEFESA_CIVIL', 'NATUREZA4_DEFESA_CIVIL','NATUREZA5_DEFESA_CIVIL',
'FLAG_EQUIPAMENTO_URBANO', 'FLAG_FLAGRANTE','OPERACAO_DESCRICAO', 'SECRETARIA_NOME', 'SECRETARIA_SIGLA', 
'SERVICO_NOME','SITUACAO_EQUIPE_DESCRICAO', 'NUMERO_PROTOCOLO_156', 'OCORRENCIA_CODIGO','OCORRENCIA_ANO'
]

print('Remove ' + str(len(colunasRemover)) + ' colunas')

for v in colunasRemover:
    print('Removendo coluna: ' +  v)
    df.drop(v, axis=1, inplace=True)

print('\nColunas:')
for n, i in enumerate(df.columns,1):
    print('  %s %s' % (n, i))


#Melhora valores da coluna ORIGEM_CHAMADO_DESCRICAO
print('\nMelhora valores da coluna ORIGEM_CHAMADO_DESCRICAO...')
df.ORIGEM_CHAMADO_DESCRICAO.replace(['NÃO CADASTRAR "ANTIGO SIGA"'], ['ANTIGO SIGA'], inplace=True)
df.ORIGEM_CHAMADO_DESCRICAO.replace(['SIGA'], ['ANTIGO SIGA'], inplace=True)
df.ORIGEM_CHAMADO_DESCRICAO.replace(['VAZIO "NÃO CADASTRAR" ANTIGO AOS GMS'], ['ANTIGO GMS'], inplace=True)
df.ORIGEM_CHAMADO_DESCRICAO.replace(['AOS GMS'], ['ANTIGO GMS'], inplace=True)
df.ORIGEM_CHAMADO_DESCRICAO.replace(['À VIATURA'], ['VIATURA'], inplace=True)
df.ORIGEM_CHAMADO_DESCRICAO.replace(['CIOSP (190)'], ['190'], inplace=True)

#Melhora valores da coluna OCORRENCIA_DIA_SEMANA
print('\nMelhora valores da coluna OCORRENCIA_DIA_SEMANA...')
df.OCORRENCIA_DIA_SEMANA.replace(['DOMINGO'], ['1-DOMINGO'], inplace=True)
df.OCORRENCIA_DIA_SEMANA.replace(['SEGUNDA'], ['2-SEGUNDA'], inplace=True)
df.OCORRENCIA_DIA_SEMANA.replace(['TERÇA'], ['3-TERCA'], inplace=True)
df.OCORRENCIA_DIA_SEMANA.replace(['QUARTA'], ['4-QUARTA'], inplace=True)
df.OCORRENCIA_DIA_SEMANA.replace(['QUINTA'], ['5-QUINTA'], inplace=True)
df.OCORRENCIA_DIA_SEMANA.replace(['SEXTA'], ['6-SEXTA'], inplace=True)
df.OCORRENCIA_DIA_SEMANA.replace(['SÁBADO'], ['7-SABADO'], inplace=True)

#Melhora valores da coluna EQUIPAMENTO_URBANO_NOME, preenche valores vazios
print('\nMelhora valores da coluna EQUIPAMENTO_URBANO_NOME...')
df['EQUIPAMENTO_URBANO_NOME'].fillna('NAO-INFORMADO', inplace = True) 


#Exibe registros de determinado index
#print(df.loc[253206])
#Exibe registros por coluna=valor
#print(df.loc[(df['REGIONAL_FATO_NOME'] == 'Portão')])


#ALTERA valores invalidos
print('\nAltera valor inválido de determinados registros...')
df.loc[119260,'ATENDIMENTO_BAIRRO_NOME'] = 'BOQUEIRÃO'
df.loc[119598,'ATENDIMENTO_BAIRRO_NOME'] = 'TINGUI'
df.loc[246657,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
df.loc[262558,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
df.loc[277992,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
df.loc[307562,'ATENDIMENTO_BAIRRO_NOME'] = 'CIDADE INDUSTRIAL'
df.loc[148557,'REGIONAL_FATO_NOME'] = 'CAJURU'
df.loc[127463,'REGIONAL_FATO_NOME'] = 'PINHEIRINHO'
df.loc[130875,'REGIONAL_FATO_NOME'] = 'PORTÃO'


#Classifica as horas em periodos
#A madrugada vai da zero hora às 6h. A manhã, das 6h às 12h (ou ao meio-dia). 
#A tarde, das 12h às 18h. A noite, das 18h às 24h (ou meia-noite).
#https://www12.senado.leg.br/manualdecomunicacao/redacao-e-estilo/estilo/hora
print('\nCria coluna OCORRENCIA_PERIODO com periodo do dia da ocorrencia')
df['OCORRENCIA_PERIODO'] = df['OCORRENCIA_HORA'].apply(definePeriodoDia)


#Cria coluna com dia do mês
print('\nCria coluna OCORRENCIA_DIA com dia de cada ocorrencia')
df['OCORRENCIA_DIA'] = df['OCORRENCIA_DATA'].apply(lambda x: x[8:10])


#DELETA registros de determinados bairros inconsistentes
print('\nDeleta registros com determinados valores...')
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


#Remove registros com atributos nulos no campos abaixo
colunaNaoNula = ['ATENDIMENTO_ANO','ATENDIMENTO_BAIRRO_NOME', 'NATUREZA1_DESCRICAO', 'OCORRENCIA_DATA']
print('\nElimina registros com valor Nulo nas colunas: ' + str(colunaNaoNula))
df.dropna(subset=colunaNaoNula, inplace=True)


#Renomeia colunas
nomesColunas = {
  "ATENDIMENTO_ANO": "OC_ANO",
  "ATENDIMENTO_BAIRRO_NOME": "OC_BAIRRO",
  "EQUIPAMENTO_URBANO_NOME": 'OC_EQUIPAMENTO_URBANO',
  "LOGRADOURO_NOME": 'OC_LOGRADOURO',
  "NATUREZA1_DESCRICAO": 'OC_CATEGORIA',
  "SUBCATEGORIA1_DESCRICAO": 'OC_SUBCATEGORIA',
  "OCORRENCIA_DATA": 'OC_DATA',
  "OCORRENCIA_DIA": 'OC_DIA',
  "OCORRENCIA_MES": 'OC_MES',
  "OCORRENCIA_HORA": 'OC_HORA',
  "OCORRENCIA_PERIODO": 'OC_PERIODO_DIA',
  "OCORRENCIA_DIA_SEMANA": 'OC_DIA_SEMANA',
  "REGIONAL_FATO_NOME": 'OC_REGIONAL_BAIRRO',
  "ORIGEM_CHAMADO_DESCRICAO": 'OC_ORIGEM_CHAMADO'
}
print('\nRenomeia colunas:')
df.rename(columns = nomesColunas, inplace = True)

df = df[['OC_ANO', 'OC_DIA', 'OC_MES', 'OC_HORA', 'OC_PERIODO_DIA', 'OC_DIA_SEMANA', 'OC_DATA', 'OC_CATEGORIA',
'OC_SUBCATEGORIA','OC_BAIRRO', 'OC_REGIONAL_BAIRRO', 'OC_EQUIPAMENTO_URBANO', 'OC_LOGRADOURO', 'OC_ORIGEM_CHAMADO' ]]

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
df.to_csv(DATAFILE_OUT, encoding="utf-8", index_label='N') 

#Verifica se o tamanho do dataset diminuiu
sizeOut = Path(DATAFILE_OUT).stat().st_size
print('Tamanho arquivo:' + str(humanize.naturalsize(sizeOut)))


#########################################################################
# 
#           CRIACAO DO DATASET FINAL
#
#########################################################################

print('\n\n###################################')
print('     CRIACAO DO DATASET FINAL')
print('###################################\,')



