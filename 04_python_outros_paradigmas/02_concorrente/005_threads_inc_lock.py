from threading import Thread, Lock
from multiprocessing import Process
import time

contador = 0
lock = Lock() #  definimos a variável global lock utilizando o construtor lock()
print_lock = Lock()

def funcao_a(indice):
    global contador
    for i in range(1000000):
        lock.acquire() #  antes de incrementar o contador, chamamos o método acquire() da variável lock, de forma a garantir exclusividade na operação de incremento
        contador += 1
        lock.release() # após o incremento, liberamos a trava utilizando o método release
    print_lock.acquire()
    print("Termino thread ", indice) # aqui corrigimos o problema de impressão no console de forma desordenada. Esse problema ocorria, pois o print não é uma operação atômica. Para resolver, envolvemos o print com outra trava, print_lock.
    print_lock.release()

if __name__ == '__main__':
    tarefas = []
    for indice in range(10):
        tarefa = Thread(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador)  