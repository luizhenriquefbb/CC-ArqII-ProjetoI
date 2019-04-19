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
    
    # quebrar elementos em x listas. Cada um vai rodar em um processo
    fator = len(elementos)/processos
    inputs=[]
    response = []
    
    while True:
        for i in range(processos):
            inputs.append(elementos[i*fator:(i*fator)+fator-1])



        newpid = os.fork()
        if newpid == 0:
            _child(fun, inputs[number_of_child])
        else:
            pids = (os.getpid(), newpid)
            # print("parent: %d, child: %d\n" % pids)
        if number_of_child < processos: 
            number_of_child+=1
            continue
        else:
            break

    print("Parent ended")


def foreach(fun, tempArray, threads=4, return_=True):
    parent(fun, tempArray, threads)





