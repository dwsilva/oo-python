from abc import ABC
from collections.abc import MutableSequence
import filme
import serie
import playlist

# def inserir_filme_na_lista(object):
#     filme.Filme = filme.append(filmes_e_series)
#     pass

def mostrar_itens_da_lista(playlist):
    print(f"\nTamanho da playlist: {len(playlist_fim_de_semana)}")
    for programa in playlist_fim_de_semana:
        print(programa)
    print("\nFim da Playlist!")

filme1 = filme.Filme("vingadores - guerra infinita", 2020, 120)
filme2 = filme.Filme("robocop", 1996, 75)
serie1 = serie.Serie("Vikins", 2017, 5)
serie2 = serie.Serie("Game of Thrones", 2019, 7)
filme1.dar_like()
filme1.dar_like()
filme2.dar_like()
filme2.dar_like()
serie1.dar_like()
serie1.dar_like()
serie1.dar_like()
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()

filmes_e_series = [filme1, serie1, filme2, serie2]
playlist_fim_de_semana = playlist.Playlist('fim de semana', filmes_e_series)
mostrar_itens_da_lista(filmes_e_series)


