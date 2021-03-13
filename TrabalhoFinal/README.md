Ciência de Dados para Segurança (CI1030) - Trabalho Final
=================
#### Alunos:

Carlos Humberto Lopes Costa

Láercio Silva de Campos Junior

<hr >

#### I.	INTRODUÇÃO

Esse trabalho foi elaborado como Projeto Final para a disciplina “Ciência de Dados para Segurança”, professor André Grégio (Dtinf/UFPR).  O objetivo desse trabalho é aplicar as técnicas e ferramentas de Ciência de Dados para explorar um conjunto de dados específico.

Foi escolhido para análise o conjunto de dados de ocorrências atendidas pela Guarda Municipal de Curitiba/PR. Esse trabalho abordará todas as etapas do processo de Ciência de Dados – Obtenção de Dados, Limpeza, Exploração, Modelagem e Interpretação. Esse trabalho aplicou ainda os algoritmos de KNN, Random Forest e Support Vector Machine no conjunto de dados.

![image](https://user-images.githubusercontent.com/63817167/111011526-7d834080-8378-11eb-810a-0fc5ff7e7354.png)

Fig. 1 - https://towardsdatascience.com/5-steps-of-a-data-science-project-lifecycle-26c50372b492

<hr >

#### II.	ANÁLISE DOS DADOS

a)	Fonte de Dados

O conjunto de dados foi obtido do portal de dados abertos da Prefeitura de Curitiba/PR . Esse dataset conta com dados  do sistema “SiGesGuarda” - sistema contendo os dados das ocorrências atendidas pela Guarda Municipal de Curitiba/PR. O dataset está no formato CSV e o espectro temporal é de 2009 até 01/02/2021. O dataset fornece informações como: categoria, subcategoria, data, hora, bairro e origem da ocorrência.
  
b)	Pré-Processamento

O dataset foi pré-processamento para remoção de registros vazios, remoção de atributos desnecessários, correção de inconsistências e criação de novos atributos. Foi criado o script Python “PreProcessamento.py” para realização dessa tarefa, sendo o script disponibilizado o GitHub “https://github.com/chlcosta/CdadosSeg/tree/main/T3”.
Originalmente o dataset possui 35 colunas/atributos, após o pré-processamento ficou com 11 atributos, apresentados na Tabela 1 a seguir.

<table>
  <tr>
    <td colspan="2" style="width:100%;align=center"><b>Tabela 1 – Colunas/Atributos do Dataset<b/></td>
  </tr>
    <tr>
	<td>1</td>
    <td>OC_ANO – Ano da Ocorrência<br />2015, 2016, 2017, 2018, 2019, 2020</td>
	  </tr>
  <tr>
	<td>2</td>
    <td>OC_MES – Mês da Ocorrência<br />1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12</td>
  </tr>
  <tr>
	<td>3</td>
    <td>OC_DIA_SEMANA – Dia da Semana (Numérico)<br />1, 2, 3, 4, 5, 6, 7</td>
  </tr>
  <tr>
	<td>4</td>
    <td>OC_DIA_SEMANA_TXT – Dia da Semana (Textual)<br />1-DOMINGO', '2-SEGUNDA', '3-TERCA', '4-QUARTA', '5-QUINTA', '6-SEXTA', '7-SABADO'</td>
  </tr>
  <tr>
	<td>5</td>
    <td>OC_DIA – Dia do mês<br />1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31</td>
  </tr>
  <tr>
	<td>6</td>
    <td>OC_PERIODO_DIA – Período do Dia (Numérico)<br />1, 2, 3, 4</td>
  </tr>
  <tr>
	<td>7</td>
    <td>OC_PERIODO_DIA_TXT – Período do Dia (Textual)<br />'1-MANHA', '2-TARDE', '3-NOITE', '4-MADRUGADA'</td>
  </tr>
  <tr>
	<td>8</td>
    <td>OC_BAIRRO – Bairro da Ocorrência (Numérico)<br />1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,  …,  71, 72, 73, 74</td>
  </tr>
  <tr>
	<td>9</td>
    <td>OC_BAIRRO_TXT – Bairro da Ocorrência (Textual)<br />'ABRANCHES', 'ÁGUA VERDE', 'AHÚ', 'ALTO BOQUEIRÃO', 'ALTO DA GLÓRIA', 'ALTO DA RUA XV', 'ATUBA', 'AUGUSTA', 'BACACHERI', 'BAIRRO ALTO', 'BARREIRINHA', 'BATEL'...</td>
  </tr>
  <tr>
	<td>10</td>
    <td>OC_SUBCATEGORIA – Tipo da Ocorrência (Numérico)<br />1, 2, 3, 4, 5, 6, 7, 8, 9, 10</td>
  </tr>
  <tr>
	<td>11</td>
    <td>OC_SUBCATEGORIA_TXT – Tipo da Ocorrência (Textual)<br />'Arrombamento', 'Cão solto em via pública', 'Desordem', 'Disparo de Alarme (violação)', 'Estacionamento irregular', 'Invasão de equipamento/patrimônio público', 'Pichação', 'Transporte Coletivo', 'Uso de substância ilícita', 'Vandalismo'</td>
  </tr>
</table>

    
O atributo de período do dia (OC_PERIODO_DIA_TXT) foi criado utilizando as seguintes referências, A madrugada vai da zero hora às 6h. 
A manhã, das 6h às 12h (ou ao meio-dia). A tarde, das 12h às 18h. A noite, das 18h às 24h (ou meia-noite).
Para o estudo optou-se por definir o intervalo dos últimos 6 anos para análise (2020-2015) e as 10 ocorrências de maior frequência no período, totalizando 35.424 registros.

c)	Análise dos Dados

Na sequência são apresentados os gráficos de distribuição do dataset baseado no Ano, Mês e Dia da Ocorrência.

![image](https://user-images.githubusercontent.com/63817167/111011816-6abd3b80-8379-11eb-84f6-ee795c5cfad5.png)
(a)

![image](https://user-images.githubusercontent.com/63817167/111011825-71e44980-8379-11eb-867b-cba455ce4397.png)
(b)

![image](https://user-images.githubusercontent.com/63817167/111011842-7ad51b00-8379-11eb-83b7-35d59a43ebe3.png)
(c)

Fig. 2 – Distribuições por (a) Ano, (b) Mês e (c) Dia da Semana

<table>
  <tr>
    <td colspan="4" style="width:100%;align=center"></td>
  </tr>
   <tr>
    <td><b></td>
    <td><b>Ano</b></td>
    <td><b>Mês</b></td>
	<td><b>Dia Semana</b></td>
  </tr>
  <tr>
    <td>Terceiro Quartil</td>
    <td>6.797</td>
    <td>3.141</td>
	<td>5.305</td>
  </tr>
  <tr>
    <td>Mediana</td>
    <td>5.306</td>
    <td>2.984</td>
	<td>4.837</td>
  </tr>	
<tr>
    <td>Primeiro Quartil</td>
    <td>5.011</td>
    <td>2.873</td>
	<td>4.731</td>
  </tr
</table>

</table>

![image](https://user-images.githubusercontent.com/63817167/111011900-b7087b80-8379-11eb-85d5-e6d29a9a098f.png)

Fig. 3 – Número de Ocorrências por Ano

![image](https://user-images.githubusercontent.com/63817167/111011923-d3a4b380-8379-11eb-9416-22a5f544831d.png)

Fig. 4 – Tendências das “Top 10” ocorrências

A partir da análise das principais ocorrências pode-se observar um aumento de quase 1.000% nas ocorrências de “Estacionamento Irregular” entre 2019 e 2020. Com exceção da ocorrência da “Estacionamento Irregular” as demais ocorrências sofreram uma leve queda de 2019 para 2020, possivelmente devido ao efeito da pandemia do COVID-19. No entanto, o “Uso de Substância Ilícita” teve uma queda aproximada de 31% no mesmo período.

![image](https://user-images.githubusercontent.com/63817167/111011944-e0290c00-8379-11eb-8aba-9a13dae94eac.png)

Fig. 5 – Número de ocorrências por Tipo

Observou-se através das Figuras 5 e 6 que a distribuição da quantidade de ocorrências é bastante irregular entre os tipos de ocorrências e entre os bairros.

![image](https://user-images.githubusercontent.com/63817167/111011948-ea4b0a80-8379-11eb-9c89-b77fca1f4f13.png)

Fig. 6 – Número de ocorrências por Bairro

![image](https://user-images.githubusercontent.com/63817167/111011958-f1721880-8379-11eb-99dd-166434962878.png)

Fig. 7 – Número de ocorrências por Período do Dia

Conforme a Figura 7, as ocorrências atendidas pela Guarda Municipal de Curitiba, para os “Top 10” tipos de ocorrências, seguem a tendência de aumento ao longo do dia, no entanto, com redução considerável no período da madrugada.

Para essa etapa de exploração dos dados foi criado o  script Python “ExploracaoDados.py”, que também foi disponibilizado no endereço do GitHub informado.

<hr >

#### III.	CONSTRUÇÃO DO MODELO

Considerando que o propósito do presente trabalho é a classificação dos tipos de ocorrências atendidas pela Guarda Municipal de Curitiba/PR, utilizou-se para construção dos modelos os algoritmos de classificação    K-Nearest Neighbour (KNN), Random Forests e Support Vector Machine (SVM). Cada algoritmo tem suas próprias vantagens e desvantagens em termos de complexidade, precisão e tempo de treinamento, podendo prover diferentes resultados para um mesmo conjunto de dados de entrada.

Antes da construção dos modelos, os dados precisaram ser alterados para formatos compatíveis com os modelos. Os atributos categóricos foram convertidos em atributos numéricos com um único ID. Todos os tipos de ocorrências e bairros possuem um diferente ID. Os bairros são representados através de 74 IDs e os tipos de ocorrências através de 10 IDs. A relação entre os atributos textuais e numéricos podem ser visualizados na Tabela 1, apresentada anteriormente.

A etapa de pré-processamento realizou a divisão do dataset em conjunto de treinamento e teste na proporção “80/20”, respectivamente. Os algoritmos foram aplicados sobre esses mesmos conjuntos de dados. Realizou-se também a validação cruzada (Cross-Validation) com 5 pastas para cada algoritmo. A validação cruzada previne o problema de overfitting e assegura que a predição do modelo possui performance satisfatória para dados ainda não vistos.

Antes da aplicação de cada modelo, o dataset foi novamente divido na proporção “80/20”.

Para aplicação dos modelos no dataset foi criado o  script Python “Modelos.py”, que está disponível no endereço do GitHub informado.

a) K-Nearest Neighbour (KNN)

O KNN foi aplicado com os parâmetros 1, 3 e 5, sendo os resultados coletados e apresentados abaixo:

<table>
  <tr>
    <td colspan="4" style="width:100%;align=center">Tabela 2 – Resultados KNN</td>
  </tr>
   <tr>
    <td><b></td>
    <td><b>K =1</b></td>
    <td><b>K = 3</b></td>
	<td><b>K = 5</b></td>
  </tr>
  <tr>
    <td>Precisão</td>
    <td>0.195</td>
    <td>0.203</td>
	<td>0.217</td>
  </tr>
  <tr>
    <td>Acurácia</td>
    <td>0.256</td>
    <td>0.266</td>
	<td>0.296</td>
  </tr>	
<tr>
    <td>Erro</td>
    <td>2.565</td>
    <td>2.847</td>
	<td>2.695</td>
  </tr
</table>

</table>


![image](https://user-images.githubusercontent.com/63817167/111012046-4f066500-837a-11eb-8786-9d91bcdaf1b8.png)

Nova divisão

b) Random Forests

c) Support Vector Machine (SVM)


### IV.	CONCLUSÃO


### V.	REFERÊNCIAS

[1]	Ceschin, F.; Oliveira, L. E. S.; Grégio, A. R. A. Aprendizado de Máquina para Segurança: Algoritmos e Aplicações. Capítulo 2 do Livro de Minicursos do XIX Simpósio Brasileiro de Segurança da Informação e de Sistemas Computacionais, 2019. https://sbseg2019.ime.usp.br/minicursos.pdf




