from funcionario import Funcionario

class Caelum(Funcionario):
    def mostra_tarefas(self):
        print("Fez coisa pra krl na Caelum...")

    def busca_curso_do_mes(self):
        mes = ""
        print(f"Mostrando cursos do mês de {mes}" if mes else "Mostrando curso de outro mês")