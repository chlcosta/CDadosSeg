# TRABALHO FINAL - CIENCIA DE DADOS PARA SEGURANCA
# ALUNO: CARLOS HUMBERTO / LAERCIO
#
# Aplicação dos modelos
# - KNN
# - Random Forest
# - SVM

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import confusion_matrix, precision_score, mean_absolute_error,accuracy_score, roc_curve, auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler  
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

DATAFILE_80  = "dataset/sigesguarda-dataset-80.csv" 
DATAFILE_20  = "dataset/sigesguarda-dataset-20.csv" 
GRAFICOS_DIR = './graficos/'

N_CLASSES = 10



#GERA CURVA ROC PARA MODELO, UMA CURVA PARA CADA CLASSE
#---------------------------------------------------------
def criaCurvaROC(y_test_b, y_pred_prob,modelo):

    global N_CLASSES

    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    for i in range(N_CLASSES):
        fpr[i], tpr[i], _ = roc_curve(y_test_b[:, i], y_pred_prob[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    #Cria diretorio para graficos, se nao existir
    try:
        Path(GRAFICOS_DIR).mkdir(parents=False,exist_ok=True)
    except:
        print('ERRO! Não foi possível criar diretório de graficos.')
        exit()

    #PLOT Curva Roc
    for i in range(N_CLASSES):        
        plt.figure()
        plt.plot(fpr[i], tpr[i], label='ROC curve (area = %0.2f)' % roc_auc[i])
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.0])
        i2=i+1
        plt.xlabel('Taxa Falso Positivo (FP)')
        plt.ylabel('Taxa Verdadeiro Positivo (VP)')
        plt.title('Curva ROC - %s - Ocorrencia ID: %s' % (modelo,i2))
        plt.legend(loc="lower right")
        plt.savefig(GRAFICOS_DIR+'ROC-Curve-%s-Classe-%s.png' % (modelo,i2))





#KNN
#----------------------------------------
def executeKNN(x_train, x_test, y_train, y_test, k):

    global N_CLASSES

    print('\n----------------------------------------------------')
    print('KNN (K = %s) - PERCENTAGE SPLIT' % k)
    print('----------------------------------------------------')    

    model = KNeighborsClassifier(n_neighbors=k)
    model = OneVsRestClassifier(model)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print("Precisão Geral: %.3f" % precision_score(y_test, y_pred, average='macro'))
    print("Mean Absolute Error: %.3f" % mean_absolute_error(y_test, y_pred))
    print("Acurácia: %.3f" % accuracy_score(y_test, y_pred))
    print("Matriz de confusão:")
    print(confusion_matrix(y_test, y_pred))

    precisaoByClass = precision_score(y_test, y_pred,average=None)    
    count = 1
    for p in precisaoByClass:
        print("Precisão Classe %s: %.3f" % (count, p))
        count = count + 1
    
    exit(0)
    #Cria Curva ROC para o Modelo
    y_test_b = label_binarize(y_test, classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_pred_prob = model.predict_proba(x_test)
    criaCurvaROC(y_test_b,y_pred_prob,'KNN-K'+str(k))






#Leitura do Dataset
df = pd.read_csv(DATAFILE_80,sep=',', low_memory=False) 


#Exibe informações do dataset
print('\n DATASET INFO:')
print(df.info())


#Define Atributos 
x = df.iloc[:, :-1].values
#Define Classes
y = df.iloc[:, 6].values

#Exibe Atributos e Classes
print('\nAtributos:')
print(x)
print('\nClasses:')
print(y)



print('\nINICIO DA CONSTRUÇÃO DOS MODELOS...')
print('---------------------------------------------------\n')


print('\nNormal:')
print(y)
print('--------')

#Binarizado
print('\nBinarizado:')
#y = label_binarize(y, classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(y)
print('--------')

#Separa os dados em Treino e Treinamento (80/20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print(y_train)

#y_train = label_binarize(y_train, classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(y_train)


#Normaliza os dados
scaler = StandardScaler()  
scaler.fit(x_train)
x_train = scaler.transform(x_train)  
x_test = scaler.transform(x_test) 

#Executa KNN com valores variados
executeKNN(x_train, x_test, y_train, y_test, 1)
