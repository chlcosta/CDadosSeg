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

#### II. ANÁLISE DOS DADOS

a)	Fonte de Dados

O conjunto de dados foi obtido do portal de dados abertos da Prefeitura de Curitiba/PR . Esse dataset conta com dados  do sistema “SiGesGuarda” - sistema contendo os dados das ocorrências atendidas pela Guarda Municipal de Curitiba/PR. O dataset está no formato CSV e o espectro temporal é de 2009 até 01/02/2021. O dataset fornece informações como: categoria, subcategoria, data, hora, bairro e origem da ocorrência.
  
b)	Pré-Processamento

O dataset foi pré-processamento para remoção de registros vazios, remoção de atributos desnecessários, correção de inconsistências e criação de novos atributos. Foi criado o script Python “PreProcessamento.py” para realização dessa tarefa, sendo o script disponibilizado o GitHub “https://github.com/chlcosta/CdadosSeg/tree/main/T3”.
Originalmente o dataset possui 35 colunas/atributos, após o pré-processamento ficou com 11 atributos, apresentados na Tabela 1 a seguir.

<table>
  <tr>
    <td colspan="2" style="width:100%;align=center"><b> Tabela 1 – Colunas/Atributos do Dataset <b/></td>
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
	</tr>
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
	  <td colspan="4" style="width:100%;align=center"><b> Tabela 2 – Resultados KNN (80%) </b></td>
  </tr>
   <tr>
    <td></td>
    <td><b>K =1</b></td>
    <td><b>K = 3</b></td>
	<td><b>K = 5</b></td>
  </tr>
  <tr>
	  <td><b>Precisão</b></td>
    <td>0.195</td>
    <td>0.203</td>
	<td>0.217</td>
  </tr>
  <tr>
	  <td><b>Acurácia</B></td>
    <td>0.256</td>
    <td>0.266</td>
	<td>0.296</td>
  </tr>	
<tr>
	<td><b>Erro</B></td>
    <td>2.565</td>
    <td>2.847</td>
	<td>2.695</td>
	</tr>
</table>


Abaixo é apresentada a Matriz de Confusão aplicando K = 1. E na sequência as Curvas ROC das ocorrências tipo 1 e tipo 10, mostrando a variação na curva.

Matriz de Confusão

![image](https://user-images.githubusercontent.com/63817167/111012046-4f066500-837a-11eb-8786-9d91bcdaf1b8.png)

![image](https://user-images.githubusercontent.com/63817167/111014583-22a31680-8383-11eb-9233-0778a0c0ba5a.png)

Fig. 8 – Curva ROC – KNN (K=1) – Ocorrência Tipo 1

![image](https://user-images.githubusercontent.com/63817167/111014595-2e8ed880-8383-11eb-863c-b8f4c92910e1.png)

Fig. 9 – Curva ROC – KNN (K=1) – Ocorrência Tipo 10

Observou-se que a precisão geral é bastante baixa para o caso em questão. No entanto, a precisão pode ser melhor para determinado tipo de ocorrência.

Na sequência são apresentadas as Curvas ROC da ocorrência tipo 1 e 10 utilizando KNN (K=1) com Validação Cruzada com 5 pastas (k-fold = 5).

![image](https://user-images.githubusercontent.com/63817167/111014603-3f3f4e80-8383-11eb-9656-007c33e33179.png)

Fig. 10 – Curva ROC – KNN (K=1) com Validação Cruzada (K-fold=5)  – Ocorrência Tipo 1

![image](https://user-images.githubusercontent.com/63817167/111014608-46665c80-8383-11eb-8dc4-16c2ea5aaab7.png)

Fig. 11 – Curva ROC – KNN (K=1) com Validação Cruzada (K-fold=5)  – Ocorrência Tipo 10

O log completo da execução do modelo, com as precisões gerais, precisões utilizando validação cruzada e matrizes de confusão pode ser visto no arquivo           “log-Modelos-80.txt” no GitHub do trabalho.

Em seguida, foi realizado o teste com os outros 20% dos dados do dataset e se obteve uma precisão bastante próxima, conforme observado na tabela 3.

<table>
  <tr>
	  <td colspan="4" style="width:100%;align=center"><b> Tabela 3 – Resultados KNN (20%) </b></td>
  </tr>
   <tr>
    <td></td>
    <td><b>K =1</b></td>
    <td><b>K = 3</b></td>
	<td><b>K = 5</b></td>
  </tr>
  <tr>
	  <td><b>Precisão</b></td>
    <td>0.219</td>
    <td>0.217</td>
	<td>0.193</td>
  </tr>
  <tr>
	  <td><b>Acurácia</b></td>
    <td>0.266</td>
    <td>0.279</td>
	<td>0.289</td>
  </tr>	
<tr>
	<td><b>Erro</b></td>
    <td>2.631</td>
    <td>2.666</td>
	<td>2.664</td>
	</tr>
</table>

b) Random Forests

Aplicou-se também o modelo RandomForest, que utiliza o conceito de árvores de decisão. O algoritmo cria uma estrutura similar a um fluxograma, com “nós” onde uma condição é verificada, e se atendida o fluxo segue por um ramo, caso contrário, por outro, sempre levando ao próximo nó, até a finalização da árvore.

O algoritmo foi parametrizado com 10 árvores, antes de tomar uma votação ou fazer uma média de predições. A precisão, erro e a Matriz de Confusão são apresentados abaixo.

<table>
  <tr>
	  <td colspan="4" style="width:100%;align=center"><b> Tabela 4 – Resultados RandomForests (80%) </b></td>
  </tr>
   <tr>
    <td></td>
	   <td><b>n_estimators = 10</b></td>	
  </tr>
  <tr>
	  <td><b>Precisão</b></td>
    <td>0.270</td>
    /td>
  </tr>
  <tr>
	  <td><b>Acurácia</b></td>
    <td>0.333</td>
    /td>
  </tr>	
<tr>
	<td><b>Erro</b></td>
    <td>2.426</td>    
	</tr>
</table>



![image](https://user-images.githubusercontent.com/63817167/111015585-55034280-8388-11eb-9002-59b7ef9361ac.png)

Apesar a precisão se manter baixa, para o caso em análise, já se mostrou melhor que a classificação com KNN.

![image](https://user-images.githubusercontent.com/63817167/111015169-3ef48280-8386-11eb-8d23-08edaf6afa89.png)

Fig. 12 – Curva ROC – RandomForest –  Ocorrência Tipo 1

![image](https://user-images.githubusercontent.com/63817167/111015177-4caa0800-8386-11eb-90e5-9b8b92a37ffb.png)

Fig. 13 – Curva ROC – RandomForest –  Ocorrência Tipo 10

Assim como no algoritmo KNN, observamos forte discrepâncias nas precisões dos tipos de Ocorrências.

Na sequência são apresentadas as Curvas ROC da ocorrência tipo 1 e 10 utilizando RandomForest com Validação Cruzada com 5 pastas (k-fold = 5).

![image](https://user-images.githubusercontent.com/63817167/111015189-5d5a7e00-8386-11eb-8627-f22ae6283cf2.png)

Fig. 14 – Curva ROC – RandomForests com Validação Cruzada (K-fold=5)  – Ocorrência Tipo 1

![image](https://user-images.githubusercontent.com/63817167/111015195-64818c00-8386-11eb-8501-7ec2ae4b0c9c.png)

Fig. 15 – Curva ROC – RandomForests com Validação Cruzada (K-fold=5)  – Ocorrência Tipo 10

<table>
  <tr>
	  <td colspan="4" style="width:100%;align=center"><b> Tabela 5 – Resultados RandomForests (20%) </b></td>
  </tr>
   <tr>
    <td></td>	
	   <td><b>n_estimators = 10</b></td>	
  </tr>
  <tr>
	  <td><b>Precisão</b></td>
    <td>0.267</td>
    /td>
  </tr>
  <tr>
	  <td><b>Acurácia</b></td>
    <td>0.327</td>
    /td>
  </tr>	
<tr>
	<td><b>Erro</b></td>
    <td>2.468</td>    
	</tr>
</table>


c) Support Vector Machine (SVM)

O último algoritmo analisado foi o Support Vector Machines (SVM). O algoritmo foi utilizado com o parâmetro Kernel =  “Linear’.
Os resultados são apresentados abaixo:

<table>
  <tr>
	  <td colspan="4" style="width:100%;align=center"><b> Tabela 6 – Resultados SVM (80%) </b></td>
  </tr>
   <tr>
    <td></td>	
	   <td><b>Kernel = Linear</b></td>	
  </tr>
  <tr>
	  <td><b>Precisão</b></td>
    <td>0.144</td>
    /td>
  </tr>
  <tr>
	  <td><b>Acurácia</b></td>
    <td>0.212</td>
    /td>
  </tr>	
<tr>
	<td><b>Erro</b></td>
    <td>3.103</td>    
	</tr>
</table>



![image](https://user-images.githubusercontent.com/63817167/111015481-b8d93b80-8387-11eb-9217-d677e738ffe6.png)

Esse modelo apresentou a pior precisão dentre os demais modelos, para todos os tipos de ocorrências.

Abaixo são apresentadas as Curvas ROC para o modelo.

![image](https://user-images.githubusercontent.com/63817167/111015489-c4c4fd80-8387-11eb-9f7e-981c0bb36abc.png)

Fig. 16 – Curva ROC – SVM –  Ocorrência Tipo 1

![image](https://user-images.githubusercontent.com/63817167/111015497-cd1d3880-8387-11eb-827f-8d11aa4d1c24.png)

Fig. 17 – Curva ROC – SVM –  Ocorrência Tipo 10

Na sequência são apresentadas as Curvas ROC da ocorrência tipo 1 e 10 utilizando SVM com Validação Cruzada com 5 pastas (k-fold = 5).

![image](https://user-images.githubusercontent.com/63817167/111015505-d7d7cd80-8387-11eb-979b-614e73bd1718.png)

Fig. 18 – Curva ROC – SVM com Validação Cruzada ](K-fold=5)  – Ocorrência Tipo 1

![image](https://user-images.githubusercontent.com/63817167/111015511-de664500-8387-11eb-8a64-17b5d1d416f8.png)

Fig. 19 – Curva ROC – SVM com Validação Cruzada ](K-fold=5)  – Ocorrência Tipo 10

Em seguida, foi realizado o teste com os outros 20% dos dados do dataset e se obteve uma precisão bastante próxima, conforme observado na tabela 7.

<table>
  <tr>
	  <td colspan="4" style="width:100%;align=center"><b> Tabela 7 – Resultados SVM (20%) </b></td>
  </tr> 
   <tr>
    <td></td>	
	   <td><b>Kernel = Linear</b></td>	
  </tr>
  <tr>
	  <td><b>Precisão</b></td>
    <td>0.137</td>
    /td>
  </tr>
  <tr>
	  <td><b>Acurácia</b></td>
    <td>0.219</td>
    /td>
  </tr>	
<tr>
	<td><b>Erro</b></td>
    <td>2.933</td>    
	</tr>
</table>


### IV.	CONCLUSÃO

Nesta trabalho foram utilizados dados de atendimento de ocorrências da Guarda Municipal de Curitiba/PR nos últimos 6 anos (2015 a 2020) e com as 10 ocorrências  com maior frequência no período. Os dados foram divididos na proporção “80/20”, criando conjunto de treinamento e teste. 

As precisões dos modelos foram bastante baixas para o conjunto de dados, o melhor resultado obtido foi com RandomForest que obteve precisão de 27% e o pior resultado foi com SVM, que obteve precisão de 14%. O modelo KNN apresentou precisão muito parecidas para K=1, 3 e 5, entre 19% e 21%. Embora este modelo tenha baixa precisão como modelo de previsão, ele fornece uma estrutura preliminar para análises futuras.

### V.	REFERÊNCIAS

[1]	Ceschin, F.; Oliveira, L. E. S.; Grégio, A. R. A. Aprendizado de Máquina para Segurança: Algoritmos e Aplicações. Capítulo 2 do Livro de Minicursos do XIX Simpósio Brasileiro de Segurança da Informação e de Sistemas Computacionais, 2019. https://sbseg2019.ime.usp.br/minicursos.pdf




