import os
import numpy as np
from multiprocessing import Process, Manager

def _child(fun, elementos):
    print('\nA new child ',  os.getpid())

    for elemento in range(len(elementos)):
        elementos[elemento] = (fun(elementos[elemento]))
        

    print("Child ended")

    os._exit(0)

def _parent(fun, elementos, processos=4):
    with Manager() as manager: 

        # quebrar elementos em x listas. Cada um vai rodar em um processo
        fator = int(len(elementos)/processos)
        inputs = [] # lista compartilhada entre os processos
        
        processos_array = []


        for i in range(processos):
            # cada input eh uma parte da imagem
            inputs.append(manager.list(elementos[(i*fator):(i*fator)+fator]))
            
            # para cada input, prepara o processo
            tempProcess = Process(target=_child, args=(fun, inputs[i]))

            # coloca os processos numa lista para poder referencia-los
            processos_array.append(tempProcess)

            # inicia eles
            tempProcess.start()


        # espera os processos acabarem
        for processo in processos_array:
            processo.join()

        print("concatenando resultados")
        # concatenar os resultados
        output = np.asarray(inputs).reshape(len(elementos), 3)
    
        print("Parent ended")
        return output # por enquanto nao sei retornar o resultado do processamento (esse valor sao os elementos originais)


def foreach(fun, tempArray, threads=4, return_=True):
    return _parent(fun, tempArray, threads)





