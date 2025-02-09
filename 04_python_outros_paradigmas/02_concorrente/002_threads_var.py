from threading import Thread, Lock
from multiprocessing import Process
import time

minha_lista = []

def funcao_a(indice):
    for i in range(100000):
        minha_lista.append(1)
    print("\nTérmino thread", indice)

def main():
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("\nAntes de aguardar o termino!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print("\nApós aguardar o termino!", len(minha_lista),"\n")
    
if __name__ == '__main__':
    main()