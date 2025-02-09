from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []

def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
    print("\nTérmino processo ", indice)

if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice,))
        tarefas.append(tarefa) # É função do programador armazenar uma referência para as suas threads ou processos, de maneira que possamos verificar seu estado ou interrompê-las. Para isso, armazenamos cada thread ou processo criado em uma lista chamada tarefas 
        tarefa.start()

    print("\nAntes de aguardar o término!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print("\nApós aguardar o término!", len(minha_lista))