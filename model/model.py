import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self.artist_map = {}

    def read_ruoli(self):
        ruoli = DAO.get_roles()
        return ruoli

    def build_graph(self, role: str):
        self.G.clear()
        artists = DAO.get_artists_by_role(role)
        self._artist_map = {artist.id : artist for artist in artists}
        connected_artists = DAO.get_connected_artists(role)
        for artist in connected_artists:
            if artist.id1 in self._artist_map:
                artista_1 = self._artist_map[artist.id1]
                artista_2 = self._artist_map[artist.id2]
                peso = abs(artista_1.indice - artista_2.indice)
                if artista_1.indice < artista_2.indice:
                    self.G.add_edge(artista_1.id, artista_2.id, weight=peso)
                elif artista_2.indice < artista_1.indice:
                    self.G.add_edge(artista_2.id, artista_1.id, weight=peso)

    def number_of_nodes(self):
        return self.G.number_of_nodes()

    def number_of_edges(self):
        return self.G.number_of_edges()

    def classifica(self):
        pass
        """
        uscenti = self.G.out_edges()
        entranti = self.G.in_edges()            
        """