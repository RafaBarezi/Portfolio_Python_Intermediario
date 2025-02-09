from threading import Thread
from multiprocessing import Process, Value

# Para criar uma área de memória compartilhada e permitir que diferentes processos acessem a mesma variável, podemos utilizar a classe value do módulo multiprocessing.

def funcao_a(indice, cont):
    for i in range(100000):
        with cont.get_lock():  # O Python já disponibiliza essa trava nos objetos do tipo value, não sendo necessário criar uma variável específica para a trava (lock). Observe como foi realizada a trava utilizando o método get_lock().
            cont.value += 1
    print("Termino processo ", indice)

if __name__ == '__main__':
    # Para permitir que a variável seja compartilhada, declaramos uma variável chamada contador utilizando o construtor da classe value, onde passamos como primeiro argumento um caractere com o tipo da variável compartilhada (‘i’ 🡪 inteiro) e seu valor inicial (0).
    contador = Value('i', 0)
    tarefas = []
    for indice in range(10):
        # Como não temos acesso a variáveis globais entre os processos, precisamos passar esta para o construtor process por meio do parâmetro args. Como a passagem de parâmetros é posicional, o parâmetro índice da funcao_a recebe o valor da variável índice e o parâmetro cont recebe uma referência para a variável contador.
        tarefa = Process(target=funcao_a, args=(indice, contador))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", contador.value)

    for tarefa in tarefas:
        tarefa.join()

    print("Após aguardar o termino!", contador.value)