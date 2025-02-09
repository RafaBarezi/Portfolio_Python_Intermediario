# Programa x processo: Programa é algo estático e permanente. Contém um conjunto de instruções e é percebido pelo sistema operacional como passivo. Em contrapartida, o processo é dinâmico e tem uma vida curta. Ao longo da sua execução, tem seu estado alterado. O processo é um programa em execução.

# Concorrência e paralelismo: O termo concorrente se refere a uma técnica para tornar os programas mais usáveis. Ela pode ser alcançada mesmo em processadores de apenas um núcleo, pois permite compartilhar o processador de forma a rodar vários processos. Já o paralelismo permite que programas rodem mais rápido, executando várias operações ao mesmo tempo. Ela requer várias máquinas ou um processador com mais de um núcleo.

# A thread pertence a um determinado processo. Múltiplas threads podem ser executadas dentro de um mesmo processo. As de um mesmo processo compartilham a área de memória e podem acessar os mesmos dados de forma transparente.

# Normalmente, utilizamos thread para interface gráfica, acesso ao banco de dados, acesso à rede etc., pois o programa não pode parar, ou a interface congelar, enquanto esperamos baixar um arquivo, por exemplo.

from threading import Thread
from multiprocessing import Process

def funcao_a(nome):
    print(nome)

def main():
    t = Thread(target = funcao_a, args = ("\nMinha Thread",))
    t.start()

    p = Process(target = funcao_a, args = ("\nMeu Processo\n",))
    p.start()

if __name__ == "__main__":
    main()