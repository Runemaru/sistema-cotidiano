from tarefas import cotidiano
contador_sistema = 1
usuario = cotidiano()

while contador_sistema == 1:
    sistema = int(input(f'''
{50 * '-'}

Seja bem-vindo ao criador de tarefas diárias
Aqui você poderá criar suas tarefas, concluir ou removê-lás.
Além de também poder ver todas as tarefas pendentes, e a serem concluídas!

Digite de acordo com as opções:1
                             
[1] - Adicionar Tarefa
[2] - Remover Tarefa                
[3] - Concluir Tarefa
[4] - Resumo de Tarefas
[5] - Encerrar sistema
{50 * '-'}                        
Digite sua opção:'''))
    

    if sistema == 1: 
        {50 * '-'}
        print(usuario.adicionar_tarefa())
        {50 * '-'}
    elif sistema == 2:
        print(usuario.remover_tarefa())
        {50 * '-'}
    elif sistema == 3: 
        print(usuario.concluir_tarefa())
        {50 * '-'}
    elif sistema == 4: 
        print(usuario.visualizar_tarefa())
        {50 * '-'}