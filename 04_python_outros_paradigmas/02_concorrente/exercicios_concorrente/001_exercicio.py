# Imprlementar uma solução que: a) Inicie a execução de uma Thread b) coloque ela para esperar 5 segundos c) informe seu início e final da execução

from time import sleep # Para o sistema aguardar
from threading import Thread # Precisamos para importar thread


def tarefa(tempo_espera, mensagem):
    print(f"\nIniciando a tarefa {mensagem}")
    sleep(tempo_espera)
    print(f"\nConclusão da tarefa {mensagem}")


instancia_thread = Thread(target=tarefa, args=(5, "thread em execução")) # instanciando a tarefa, onde fica a regra de negócio
instancia_thread.start() # iniciando o objeto estanciado
print("\n\nAguardando a conclusão da Thread em 5 segundos...")
instancia_thread.join() # esperando o resultado
print("\nA execução foi concluída\n")
