# TAREFA PRÁTICA 3
# ALUNO: CARLOS HUMBERTO / LAERCIO
# Requisitos: 
#    pip install pandas


import os, sys
from pathlib import Path
import pandas as pd
import humanize 

DATAFILE_IN  = "dataset/2021-02-01-sigesguarda-original.csv" 
DATAFILE_OUT = "dataset/2021-02-01-sigesguarda-editado.csv" 

df = pd.read_csv(DATAFILE_IN,sep=';', encoding='iso-8859-1', low_memory=False) 


print('\n################################################')
print('           FORMATA DATASET')
print('################################################\n')

print('Aquivo de entrada: ' + DATAFILE_IN)

qtdRegistros = '{:,}'.format(df.shape[0]).replace(',','.')
sizeIn = Path(DATAFILE_IN).stat().st_size
print('\nENTRADA:')
print(f'Quantidade registros: ' + qtdRegistros)
print('Qtd colunas/atributos: ' + str(len(df.columns)))
print('Tamnho arquivo:' + str(humanize.naturalsize(sizeIn)))

#Remove linha depois do cabecalho com "-----"
print('Remove linha abaixo do cabeçalho')
df.drop(df.index[0:1], inplace=True)

#REMOVE COLUNAS
colunasRemover = ['NATUREZA2_DESCRICAO', 'NATUREZA3_DESCRICAO','NATUREZA4_DESCRICAO', 'NATUREZA5_DESCRICAO',
'SUBCATEGORIA2_DESCRICAO', 'SUBCATEGORIA3_DESCRICAO','SUBCATEGORIA4_DESCRICAO', 'SUBCATEGORIA5_DESCRICAO',
'NATUREZA1_DEFESA_CIVIL', 'NATUREZA2_DEFESA_CIVIL','NATUREZA3_DEFESA_CIVIL', 'NATUREZA4_DEFESA_CIVIL','NATUREZA5_DEFESA_CIVIL',
'FLAG_EQUIPAMENTO_URBANO', 'FLAG_FLAGRANTE','OPERACAO_DESCRICAO', 'SECRETARIA_NOME', 'SECRETARIA_SIGLA', 
'SERVICO_NOME','SITUACAO_EQUIPE_DESCRICAO', 'NUMERO_PROTOCOLO_156'
]

print('Remove ' + str(len(colunasRemover)) + ' colunas')

for v in colunasRemover:
    print('Removendo coluna: ' +  v)
    df.drop(v, axis=1, inplace=True)

print('\nColunas:')
for n, i in enumerate(df.columns,1):
    print('  %s %s' % (n, i))


print('\nMelhora valor de colunas...')
df.ORIGEM_CHAMADO_DESCRICAO.replace(['NÃO CADASTRAR "ANTIGO SIGA"'], ['ANTIGO SIGA'], inplace=True)
df.ORIGEM_CHAMADO_DESCRICAO.replace(['VAZIO "NÃO CADASTRAR" ANTIGO AOS GMS'], ['ANTIGO GMS'], inplace=True)


colunaNaoNula = ['ATENDIMENTO_ANO','ATENDIMENTO_BAIRRO_NOME', 'NATUREZA1_DESCRICAO', 'OCORRENCIA_ANO', 'OCORRENCIA_DATA']

print('\nElimina registros com valor Nulo nas colunas: ' + str(colunaNaoNula))
df.dropna(subset=colunaNaoNula, inplace=True)

qtdRegistros = '{:,}'.format(df.shape[0]).replace(',','.')
print('\nSAIDA:')
print(f'Quantidade registros: ' + qtdRegistros)
print('Qtd colunas/atributos: ' + str(len(df.columns)))

print('\nSalva arquivo de saída: ' + DATAFILE_OUT)
df.to_csv(DATAFILE_OUT, encoding="utf-8", index_label='N') 

sizeOut = Path(DATAFILE_OUT).stat().st_size
print('Tamanho arquivo:' + str(humanize.naturalsize(sizeOut)))



