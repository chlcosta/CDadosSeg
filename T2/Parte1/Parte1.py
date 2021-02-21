# TAREFA PRÁTICA 2 - PARTE 1
# ALUNO: CARLOS HUMBERTO
# Requisitos: 
#    pip install lxml
#    pip install beautifulsoup4
#    pip install pandas


import os, sys
from os.path import basename
from bs4 import BeautifulSoup 
import pandas as pd

debug = False


# LEITURA DOS ANDROID MANIFEST
# ================================================================
def getListAndroidManifest(dir):
    global debug

    rs = []
    with os.scandir(dir) as dirs:
        for entry in dirs:
            if(entry.is_file() and entry.name.startswith("AndroidManifest")):
                rs.append(entry.path)
    
    if debug == True:
        print('\nArquivos no diretório: ' + dir)
        print(rs)
        print('\n')

    return rs


# PERMISSOES DOS APKS
# ================================================================
def getListPermissions(files):
    rs = dict()

    for i in files:

        appName = basename(i.replace('AndroidManifest_','').replace('.xml',''))

        #Le arquivo XML
        with open(i, 'r') as f: data = f.read() 
        xml = BeautifulSoup(data, "xml")

        #Busca todas as permissoes
        permissionsTmp = xml.find_all('uses-permission')

        #Adiciona cada atributo da permissao ao dicionario
        permission = ''
        for p in permissionsTmp:
            temp = p.get('android:name').split(".") 
            permission = temp[len(temp) - 1]

            if appName in rs.keys():
                rs[appName].append(permission)
            else:
                rs[appName] = [permission]


    #Monta o DataFrame
    dff = pd.DataFrame()
    for key in rs:
        index = [key] * len(rs[key])
        lista = rs[key]

        s1 = pd.Series(index,name='app')
        s2 = pd.Series(lista,name='permissao')
        df1 = pd.concat([s1, s2], axis=1)
        dff = pd.concat([df1,dff])


    print('=================================')
    print('Permissões por APK')
    print('=================================')
    df2 = dff.groupby('app')['permissao'].apply(list).reset_index(name='permissoes')

    if debug == True:
        print('\nPermissoes por APK: ')
        print(df2)
        print('\n')

    #SAIDA das permissoes por APK
    for i, r in df2.iterrows():
        print(r['app'] + ': ' + str(r['permissoes']))

    dff.drop_duplicates(subset=['app', 'permissao'], keep='first',inplace=True)  
    return dff


# PERMISSOES UNICAS
# ================================================================
def getListUniquePermissions(df): 

    global debug   

    print('\n=================================')
    print('Permissões únicas por APK')
    print('=================================')    

    #pd.set_option('display.max_rows', df.shape[0]+1)                      
    df['count'] = df.groupby(['permissao'])['permissao'].transform('count')

    df = df.loc[df['count'] == 1]

    df2 = df.groupby('app')['permissao'].apply(list).reset_index(name='permissoes')

    if debug == True:
        print('\nPermissoes únicas por APK: ')
        print(df2)
        print('\n')

    #SAIDA das permissoes unicas APK
    for i, r in df2.iterrows():
        print(r['app'] + ': ' + str(r['permissoes']))
   

# PERMISSOES COMUNS
# ================================================================
def getListCommonPermissions(df): 

    print('\n=================================')
    print('Permissões comuns das APKs')
    print('=================================')       

    global debug   

    numApps = df['app'].nunique()

    df = df.loc[df['count'] >= numApps]
    df = df.reset_index(drop=True)
    df2 = df.drop_duplicates(subset ="permissao", keep = 'first') 
    
    if debug == True:
        print('\nPermissoes comuns da APK: ')
        print(df2)
        print('\n')    


    df2 = df2.groupby('app')['permissao'].apply(list).reset_index(name='permissoes')

    #SAIDA das permissoes comuns APK
    for i, r in df2.iterrows():
        print(str(r['permissoes']))    
        



# ================================================================

# INICIO DO PROGRAMA

# ================================================================

if __name__ == '__main__':
    # Verifica parametros de entrada
    if len(sys.argv) < 2:
        print("\n!! Erro: Parâmetro inválido!")
        print("Informe o diretório com arquivos AndroidManifest.xml (Ex. python3 Parte1.py manifest)")
    else:

        if not os.path.isdir(sys.argv[1]):
            print("\n!! Erro: Parâmetro não é um diretorio válido!")
            print("Informe o diretório com arquivos AndroidManifest.xml (Ex. python3 Parte1.py manifest)")
        else:

            if len(sys.argv) == 3:
                if sys.argv[2] == 'debug':
                    debug = True

            listAM = getListAndroidManifest(sys.argv[1])
            permissions = getListPermissions(listAM)
            getListUniquePermissions(permissions)
            getListCommonPermissions(permissions)          

