import os
import numpy as np
from multiprocessing import Process, Manager

def _child(fun, elementos, i, fator, outputs ):
    '''
    Parametros:
        fun        : funcao a ser aplicada para os pixels (transformar em escala de cinza/verde/azul/vermelho)
        elementos  : lista de pixels originais
        i          : identificador do filho (ex: se sao 4 filhos, i vai de 0 a 3)
        fator      : ajuda a calcular a faixa da lista original
        outputs    : saida do processamento

    '''
    print('\nA new child ',  os.getpid())

    _elementos = (elementos[(i*fator):(i*fator)+fator])

    for elemento in range(len(_elementos)):
        outputs[elemento + (i*fator)  ] = ((fun(_elementos[elemento])))
        

    print("Child ended")

    os._exit(0)

def _parent(fun, elementos, processos=4):
    with Manager() as manager: 

        # quebrar elementos em x listas. Cada um vai rodar em um processo
        fator = int(len(elementos)/processos)
        outputs = manager.list([None]*len(elementos)) # lista compartilhada entre os processos com a quantidade de elementos da lista original
        
        processos_array = []

        for i in range(processos):
            
            # para cada input, prepara o processo
            tempProcess = Process(target=_child, args=(fun, elementos, i, fator, outputs ))

            # coloca os processos numa lista para poder referencia-los
            processos_array.append(tempProcess)

            # inicia eles
            tempProcess.start()


        # espera os processos acabarem
        for processo in processos_array:
            processo.join()

        # import pdb; pdb.set_trace()

        # print("concatenando resultados")
        # concatenar os resultados
        # output = np.asarray(inputs).reshape(len(elementos), 3)
    
        print("Parent ended")
        return outputs[:] # por enquanto nao sei retornar o resultado do processamento (esse valor sao os elementos originais)


def foreach(fun, tempArray, threads=4, return_=True):
    return _parent(fun, tempArray, threads)





