import os


def _child(fun, elementos):
    print('\nA new child ',  os.getpid())

    response = []
    for elemento in elementos:
        response.append(fun(elemento))
    
    
    
    # Como retornar o response ???


    print("Child ended")

    os._exit(0)

def parent(fun, elementos, processos=4):
    number_of_child = 0
    
    pidList = []
    fator = len(elementos)/processos
    inputs = []
    
    # quebrar elementos em x listas. Cada um vai rodar em um processo
    # dividir array entre os processos
    for i in range(processos):
        inputs.append(elementos[i*fator:(i*fator)+fator-1])

    # construir os processos
    while number_of_child < processos:

        newpid = os.fork()

        # processo filho
        if newpid == 0:
            _child(fun, inputs[number_of_child])
        
        # processo principal
        else:
            pidList.append(newpid)

            # pids = (os.getpid(), newpid)
            # print("parent: %d, child: %d\n" % pids)
        
            number_of_child+=1



    # esperar os processos acabarem (join)
    for p in pidList:
        os.waitpid(p, 0)

    print("Parent ended")
    return elementos


def foreach(fun, tempArray, threads=4, return_=True):
    return parent(fun, tempArray, threads)





