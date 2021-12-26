from alura import Alura
from caelum import Caelum

class Hipster:
    def __str__(self):
        return f"Hipster {self.nome}"

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

jose = Junior("José")
carlos = Pleno("Carlos")
lais = Senior("Lais")

print(lais)
jose.busca_perguntas_sem_resposta()
jose.mostra_tarefas()
carlos.busca_perguntas_sem_resposta()
carlos.busca_curso_do_mes()
carlos.mostra_tarefas()