# TAREFA 3

## Dataset

1. Dataset escolhido (tema):
SiGesGuarda - Base contendo os dados das ocorrências atendidas pela Guarda Municipal de Curitiba. 
Espectro temporal: De 2009 até 01/02/2021.
https://www.curitiba.pr.gov.br/dadosabertos/busca/

2. Dataset: 
https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/2021-02-01_sigesguarda_-_Base_de_Dados.csv


3. Campos/atributos do seu dataset:
https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/2015-11-25_sigesguarda_-_Dicionario_de_Dados.xlsx



## Exploração de dados

Equipe: Carlos e Laércio

**Que tipos de dados você tem, majoritariamente (atributos numéricos, textuais)?**
 - Os dados são majoritariamente **textuais**, no entanto, há dados temporais como data, hora e dia da semana.

**Qual seu objetivo com esse dataset?**

 - Realizar análises sobre as ocorrências atendidas pela Guarda Municipal de Curitiba;
 - Quais as ocorrências mais comuns?
 - Quais os tipos de ocorrências que mais ocorrem em determinadas regiões?
 - Os tipos de ocorrências variam conforme hora, dia da semana, mês, ano?
 - É verificada alguma tendência de crescimento/diminuição de determinado tipo de ocorrência?

**Seu dataset é rotulado de que maneira?**

 - O dataset, após tratamento nos dados, possui as seguintes colunas:
  - *1 N*
  - *2 ATENDIMENTO_ANO*
  - *3 ATENDIMENTO_BAIRRO_NOME*
  - *4 EQUIPAMENTO_URBANO_NOME*
  - *5 LOGRADOURO_NOME*
  - *6 NATUREZA1_DESCRICAO*
  - *7 SUBCATEGORIA1_DESCRICAO*
  - *8 OCORRENCIA_ANO*
  - *9 OCORRENCIA_CODIGO*
  - *10 OCORRENCIA_DATA*
  - *11 OCORRENCIA_DIA_SEMANA*
  - *12 OCORRENCIA_HORA*
  - *13 OCORRENCIA_MES*
  - *14 ORIGEM_CHAMADO_DESCRICAO*
  - *15 REGIONAL_FATO_NOME*
 - Foi utilizado o script **T3-formataDataset.py** para realizar o tratamento no dataset;

**Como é a distribuição dos dados do dataset?**

    - O dataset possui 327.409 registros e 15 atributos;
    - Foi utilizado o script **T3-exploracaoDados.py** para realizar a exploração do dataset;
    - Distribuição das Amostras de ATENDIMENTO_ANO X QTD:
        - *2009, 24897*
        - *2010, 22517*
        - *2011, 21455*
        - *2012, 19761*
        - *2013, 24453*
        - *2014, 25260*
        - *2015, 25540*
        - *2016, 21460*
        - *2017, 22133*
        - *2018, 24155*
        - *2019, 33754*
        - *2020, 57457*
        - *2021,  4567*


**Quais colunas/atributos você julga ser interessante manter e remover? Por quê?**

    - Foram mantidos 14 atribudos dos 21 que originalmente faziam parte do dataset.
    - Considerou-se que os atributos removidos não contribuiriam para o tipo de análise proposta;


