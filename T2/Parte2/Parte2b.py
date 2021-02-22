# TAREFA PRÁTICA 2 - PARTE 2b
# ALUNO: CARLOS HUMBERTO
# Requisitos: 
#    pip install pefile

import pefile
import os, sys
from os.path import basename

debug = False


# RECUPERA SECOES PE DOS DOIS ARQUIVOS
# ================================================================
def getSecoesPE(b1, b2):
    global debug

    rs = dict()

    pe1 = pefile.PE(b1)
    pe2 = pefile.PE(b2)

    # Cria uma lista com os respectivos nomes
    list_name_sections_a = [name.Name.decode("utf-8").replace("\x00",'') for name in pe1.sections]
    list_name_sections_b = [name.Name.decode("utf-8").replace("\x00",'') for name in pe2.sections]

    rs["intersection"] = []

    # Intersecção
    for item in list_name_sections_a:
        if item in list_name_sections_b:
            rs["intersection"].append(item)

    # Remove as intersecções
    for item in rs["intersection"]:
        list_name_sections_a.remove(item)
        list_name_sections_b.remove(item)

    rs[basename(b1)] = list_name_sections_a
    rs[basename(b2)] = list_name_sections_b

    return rs


# ================================================================
# INICIO DO PROGRAMA
# ================================================================

if __name__ == '__main__':

  # Verifica parametros de entrada
    if len(sys.argv) < 3:
        print("\n!! Erro: Parâmetro inválido!")
        print("Informe os dois arquivos binários (Ex. python3 Parte2b.py bin1.exe bin2.exe)")
    else:

        # Binarios
        b1 = sys.argv[1]
        b2 = sys.argv[2]

        if len(sys.argv) == 4:
            if sys.argv[3] == 'debug':
                debug = True

        rs = getSecoesPE(b1, b2)

        print('\nBinários - Seções Comuns')
        print('====================================================')       
        print(str(rs['intersection']))

        print('\nBinários - Seções únicas - ' + basename(b1))
        print('====================================================')       
        print(str(rs[basename(b1)]))

        print('\nBinários - Seções únicas - ' + basename(b2))
        print('====================================================')       
        print(str(rs[basename(b2)]))

        print("\n")
