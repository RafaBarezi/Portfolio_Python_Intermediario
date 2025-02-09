# Existem os erros que ocorrem em tempo de execução do programa, que não se devem a uma instrução escrita errada, e sim ao fato de que o programa entrou em um estado indevido.

# Elencamos os seguintes exemplos:

# A divisão por 0.
# A tentativa de acessar um índice indevido em uma lista.
# Um nome de variável não atribuído.
# Um erro causado por tipos incorretos de operando.

# Em cada caso, quando o programa atinge um estado inválido, é dito que o interpretador Python levanta uma exceção. Isso significa que é criado um objeto que contém as informações relevantes sobre o erro.

# KeyboardInterrupt: Levantado quando o usuário pressiona CTRL+C, a combinação de interrupção.
# OverflowError: Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
# ZeroDivisionError: Levantado quando se tenta dividir por 0.
# IOError: Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
# IndexError: Levantado quando um índice sequencial está fora do intervalo de índices válidos.
# NameError: Levantado quando se tenta avaliar um identificador (nome) não atribuído.
# TypeError: Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
# ValueError: Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.

# As exceções são objetos. A classe Exception é derivada de BaseException, classe base de todas as classes de exceção. BaseException fornece alguns serviços úteis para todas as classes de exceção, mas normalmente não se torna uma subclasse diretamente.