import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def handle_popola_dropdown_ruolo(self):
        ruoli = self._model.read_ruoli()
        return ruoli

    def handle_crea_grafo(self, e):
        if self._view.dd_ruolo.value is not None:
            ruolo = str(self._view.dd_ruolo.value)
            self._model.build_graph(ruolo)
            nodi = self._model.number_of_nodes()
            archi = self._model.number_of_edges()
            self._view.list_risultato.clean()
            self._view.list_risultato.controls.append(ft.Text(f'Nodi: {nodi}| Archi: {archi}'))
            self.enable_selections()
            self._view.update()
        else:
            self._view.show_alert(f'Errore nella selezione del ruolo')


    def handle_classifica(self, e):
        self._model.classifica()
        self._view.list_risultato.clean()

        self._view.update()

    def enable_selections(self):
        self._view.dd_iniziale.disabled = False
        self._view.btn_classifica.disabled = False
        self._view.btn_cerca_percorso.disabled = False