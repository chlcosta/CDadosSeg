# TAREFA PRÁTICA 2 - PARTE 2a
# ALUNO: CARLOS HUMBERTO
# Requisitos: 
#    pip install pefile

import pefile
import os, sys
from os.path import basename

debug = False


# RECUPERA OS ARQUIVOS BINARIOS
# ================================================================
def getBinarios(path):

    global debug

    rs = []

    if os.path.isdir(path):
        
        with os.scandir(path) as dirs:
            for entry in dirs:
                if(entry.is_file()):
                    rs.append(entry.path)
    else:
        rs.append(path)

    if debug == True:
        print('\nArquivo(s) binários em: ' + path)
        print(rs)
        print('\n')

    return rs


# RECUPERA OS ARQUIVOS BANCARIOS
# ================================================================
def getSecoesPE(files):
    rs = dict()

    for f in files:

        pe = pefile.PE(f)

        for i in pe.sections:
            # A secao eh executavel?
            if i.IMAGE_SCN_MEM_EXECUTE is True:
                if basename(f) in rs.keys():
                    rs[basename(f)].append(str(i.Name.decode('utf-8').replace("\x00",'')))
                else:
                    rs[basename(f)] = [str(i.Name.decode('utf-8').replace("\x00",''))]

    return rs


# ================================================================
# INICIO DO PROGRAMA
# ================================================================
if __name__ == '__main__':

    # Verifica parametros de entrada
    if len(sys.argv) < 2:
        print("\n!! Erro: Parâmetro inválido!")
        print("Informe o diretorio de binários ou o caminho de um binario (Ex. python3 Parte2a.py bin/)")
    else:

        if len(sys.argv) == 3:
            if sys.argv[2] == 'debug':
                debug = True

        binarios = getBinarios(sys.argv[1])
        secoes = getSecoesPE(binarios)

        if len(secoes.keys()) == 0:
            print('\n !! Erro: Não foram localizadas seções!')
            exit()

        print('\nBinário: Seção Executável')
        print('=================================')       

        for i in secoes.keys():           
            print(basename(i) + ": " + str(secoes[i]))