# Adicionar uma nova tarefa;
# Visualizar todas as tarefas;
# Marcar uma tarefa como concluída;
# Remover uma tarefa;
# Sair do programa.

from datetime import datetime as dt, timedelta


class cotidiano:
    '''
Para auxiliar no cotidiano, este módulo tem a capacidade de cadastrar tarefas para serem feitas e horários limites para realização da mesma.
Logo as tarefas são de curto-prazo, e não de longo-prazo, temos os seguintes métodos que podem ser utilizados no nosso programa.

    adicionar_tarefa: Neste comando é possível adicionar um titulo de uma tarefa a ser feita,
                      e um horário limite para realizar a tarefa no dia que foi cadastrada.

    concluir_tarefa: Neste comando é possível marcar uma tarefa como concluída, e assim
    passar a tarefa para a lista de tarefas realizadas.

    remover_tarefa: Permite remover uma tarefa que perdeu seu prazo, ou que o usuário
    não quer mais realizar.

    visualizar_tarefa: Permite visualizar tanto a lista de tarefas a fazer, quanto
    a lista de tarefas realizadas. Com base na escolha do usuário.
    '''
    def __init__(self):
        self.tarefas_a_fazer = []
        self.tarefas_realizadas = []

    def adicionar_tarefa(self):

        data_atual = dt.today()

        titulo_tarefa = input('Título da tarefa:')
        horario_limite = input('Digite um horário limite para realização da tarefa, no formato [HH:MM]: ')

        horario_atual = dt.now().strftime('%H:%M')
        hora_limite = dt.strptime(horario_limite, '%H:%M')
        hora_atual = dt.strptime(horario_atual, '%H:%M')
        
        if hora_limite < hora_atual:
            return 'Não é possível cadastrar tarefas para o dia seguinte'
        else:
            self.tarefas_a_fazer.append({'Tarefa' :titulo_tarefa, 'Data Limite' : data_atual, 'Horário Limite' : hora_limite})
            diferenca = hora_limite - hora_atual
            return f'''
Atividade {titulo_tarefa} cadastrada com sucesso.
Às {dt.now().hour} horas e {dt.now().minute} minutos.
Missão iniciada com sucesso.
Boa sorte em sua jornada!
Você tem {diferenca} horas para concluir sua atividade!'''
        
    def concluir_tarefa(self):

        selecionar_tarefa = input('Digite a tarefa que você concluiu:')
        for tarefa in self.tarefas_a_fazer:
            if tarefa['Tarefa'] == selecionar_tarefa:
                self.tarefas_realizadas.append(f' Concluiu as seguintes tarefas: {tarefa['Tarefa']}')
                tarefa.clear
                return 'Tarefa finalizada com sucesso, parabéns <3'
            else:
                return 'Tarefa não encontrada'
            
    def remover_tarefa(self):

        remover = input('Qual tarefa deseja remover:')
        for item in self.tarefas_a_fazer:
            if item['Tarefa'] == remover:
                item.clear
                return f'Tarefa {remover} removida com sucesso, esta é sua lista atual de tarefas:\n {self.tarefas_a_fazer}'
            else:
                return f'Tarefa {remover} não encontrada.'
            
    def visualizar_tarefa(self):
        selecione_lista = int(input('''
Digite [1] para visualizar tarefas a fazer
Digite [2] para visualizar as que foram realizadas                                    
Digite sua opção:'''))
        if selecione_lista == 1:
            return self.tarefas_a_fazer

        elif selecione_lista == 2:
            return self.tarefas_realizadas
        
        else:
            return 'Digite de acordo com as opções!'
        



x = cotidiano()

print(x.adicionar_tarefa())
print(x.concluir_tarefa())
print(x.tarefas_realizadas)