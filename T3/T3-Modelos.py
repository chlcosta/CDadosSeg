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


#KNN
#----------------------------------------
def executeKNN(x_train, x_test, y_train, y_test, k):

    print('\n----------------------------------------------------')
    print('KNN (K = %s) - PERCENTAGE SPLIT' % k)
    print('----------------------------------------------------')    

    model = KNeighborsClassifier(n_neighbors=k)
    model = OneVsRestClassifier(model)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print("Precisão Geral: %.3f" % precision_score(y_test, y_pred, average='macro',zero_division=0))

    precisaoByClass = precision_score(y_test, y_pred,average=None,zero_division=0)    
    count = 1
    for p in precisaoByClass:
        print("  Precisão por Classe %s: %.3f" % (count, p))
        count = count + 1

    print("Mean Absolute Error: %.3f" % mean_absolute_error(y_test, y_pred))
    print("Acurácia: %.3f" % accuracy_score(y_test, y_pred))
    print("Matriz de confusão:")
    print(confusion_matrix(y_test, y_pred))

    #Cria Curva ROC para o Modelo
    y_test_b = label_binarize(y_test, classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_pred_prob = model.predict_proba(x_test)
    criaCurvaROC(y_test_b,y_pred_prob,'KNN-K'+str(k))


#KNN COM K-FOLD=5 e K1
#----------------------------------------
def executeKNNcomKfold(xtrain, xtest, ytrain, ytest):

    print('\n----------------------------------------------------')
    print('KNN (K=1) - CROSS VALIDATION (K-FOLD=5)')
    print('----------------------------------------------------')    


    model = KNeighborsClassifier(n_neighbors=1)

    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)
    i = 1

    for train_index, test_index in kf.split(xtrain, ytrain):
        X_train = xtrain[train_index]
        X_test = xtrain[test_index]
        y_train = ytrain[train_index]
        y_test = ytrain[test_index]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print('\n--> FOLD = %s' % i)
        print("Precisão Geral: %.3f" % precision_score(y_test, y_pred, average='macro',zero_division=0))

        precisaoByClass = precision_score(y_test, y_pred,average=None,zero_division=0)    
        count = 1
        for p in precisaoByClass:
            print("  Precisão por Classe %s: %.3f" % (count, p))
            count = count + 1

        print("Mean Absolute Error: %.3f" % mean_absolute_error(y_test, y_pred))
        print("Acurácia: %.3f" % accuracy_score(y_test, y_pred))
        print("Matriz de confusão:")
        print(confusion_matrix(y_test, y_pred))

        i=i+1


#RandomForestClassifier  (Estimadores = 10)
#----------------------------------------
def executeRandomForest(x_train, x_test, y_train, y_test):

    print('\n----------------------------------------------------')
    print('RandomForestClassifier (Estimadores = 10)')
    print('----------------------------------------------------')    

    model = RandomForestClassifier(n_estimators=10)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    print("Precisão Geral: %.3f" % precision_score(y_test, y_pred, average='macro',zero_division=0))

    precisaoByClass = precision_score(y_test, y_pred,average=None,zero_division=0)    
    count = 1
    for p in precisaoByClass:
        print("  Precisão por Classe %s: %.3f" % (count, p))
        count = count + 1

    print("Mean Absolute Error: %.3f" % mean_absolute_error(y_test, y_pred))
    print("Acurácia: %.3f" % accuracy_score(y_test, y_pred))
    print("Matriz de confusão:")
    print(confusion_matrix(y_test, y_pred))

    #Cria Curva ROC para o Modelo
    y_test_b = label_binarize(y_test, classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_pred_prob = model.predict_proba(x_test)
    criaCurvaROC(y_test_b,y_pred_prob,'RandomForest')    


#RandomForestClassifier(Estimadores = 10) COM K-FOLD=5
#----------------------------------------
def executeRandomForestKFold(xtrain, xtest, ytrain, ytest):

    print('\n----------------------------------------------------')
    print('RandomForestClassifier (Estimadores = 10) COM CROSS VALIDATION (K-FOLD=5)')
    print('----------------------------------------------------')    


    model = RandomForestClassifier(n_estimators=10)

    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)
    i = 1

    for train_index, test_index in kf.split(xtrain, ytrain):
        X_train = xtrain[train_index]
        X_test = xtrain[test_index]
        y_train = ytrain[train_index]
        y_test = ytrain[test_index]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print('\n--> FOLD = %s' % i)
        print("Precisão Geral: %.3f" % precision_score(y_test, y_pred, average='macro',zero_division=0))

        precisaoByClass = precision_score(y_test, y_pred,average=None,zero_division=0)    
        count = 1
        for p in precisaoByClass:
            print("  Precisão por Classe %s: %.3f" % (count, p))
            count = count + 1

        print("Mean Absolute Error: %.3f" % mean_absolute_error(y_test, y_pred))
        print("Acurácia: %.3f" % accuracy_score(y_test, y_pred))
        print("Matriz de confusão:")
        print(confusion_matrix(y_test, y_pred))

        i=i+1


#SVM (Kernel = Linear)
#----------------------------------------
def executeSVM(x_train, x_test, y_train, y_test):

    print('\n----------------------------------------------------')
    print('SVM (Kernel = Linear)')
    print('----------------------------------------------------')    

    model = SVC(kernel="linear")
    model = OneVsRestClassifier(model)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print("Precisão Geral: %.3f" % precision_score(y_test, y_pred, average='macro',zero_division=0))

    precisaoByClass = precision_score(y_test, y_pred,average=None,zero_division=0)    
    count = 1
    for p in precisaoByClass:
        print("  Precisão por Classe %s: %.3f" % (count, p))
        count = count + 1

    print("Mean Absolute Error: %.3f" % mean_absolute_error(y_test, y_pred))
    print("Acurácia: %.3f" % accuracy_score(y_test, y_pred))
    print("Matriz de confusão:")
    print(confusion_matrix(y_test, y_pred))

    #Cria Curva ROC para o Modelo
    y_test_b = label_binarize(y_test, classes=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    y_pred_prob = model.decision_function(x_test)
    criaCurvaROC(y_test_b,y_pred_prob,'SVM')        



#SVM (Kernel = Linear) COM K-FOLD=5
#----------------------------------------
def executeSVMKFold(xtrain, xtest, ytrain, ytest):

    print('\n----------------------------------------------------')
    print('SVM (Kernel = Linear) COM K-FOLD=5 COM CROSS VALIDATION (K-FOLD=5)')
    print('----------------------------------------------------')    


    model = SVC(kernel="linear")

    kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=12)
    i = 1

    for train_index, test_index in kf.split(xtrain, ytrain):
        X_train = xtrain[train_index]
        X_test = xtrain[test_index]
        y_train = ytrain[train_index]
        y_test = ytrain[test_index]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print('\n--> FOLD = %s' % i)
        print("Precisão Geral: %.3f" % precision_score(y_test, y_pred, average='macro',zero_division=0))

        precisaoByClass = precision_score(y_test, y_pred,average=None,zero_division=0)    
        count = 1
        for p in precisaoByClass:
            print("  Precisão por Classe %s: %.3f" % (count, p))
            count = count + 1

        print("Mean Absolute Error: %.3f" % mean_absolute_error(y_test, y_pred))
        print("Acurácia: %.3f" % accuracy_score(y_test, y_pred))
        print("Matriz de confusão:")
        print(confusion_matrix(y_test, y_pred))

        i=i+1


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
        plt.close('all')




#Leitura do Dataset
df = pd.read_csv(DATAFILE_20,sep=',', low_memory=False) 


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


#Separa os dados em Treino e Treinamento (80/20)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print(x_train)

#Normaliza os dados
scaler = StandardScaler()  
scaler.fit(x_train)
x_train = scaler.transform(x_train)  
x_test = scaler.transform(x_test) 

#Executa KNN com valores variados
executeKNN(x_train, x_test, y_train, y_test, 1)
executeKNN(x_train, x_test, y_train, y_test, 3)
executeKNN(x_train, x_test, y_train, y_test, 5)
executeKNN(x_train, x_test, y_train, y_test, 10)

#EXECUTA KNN (K=1) - CROSS VALIDATION (K-FOLD=5)
executeKNNcomKfold(x_train, x_test, y_train, y_test)

#EXECUTA RandomForestClassifier (Estimadores = 10)
executeRandomForest(x_train, x_test, y_train, y_test)

#EXECUTA RandomForestClassifier (Estimadores = 10) COM CROSS VALIDATION (K-FOLD=5)
executeRandomForestKFold(x_train, x_test, y_train, y_test)

#EXECUTA SVM (Kernel = Linear)
executeSVM(x_train, x_test, y_train, y_test)

#EXECUTA SVM (Kernel = Linear) COM CROSS VALIDATION (K-FOLD=5)
executeSVMKFold(x_train, x_test, y_train, y_test)






