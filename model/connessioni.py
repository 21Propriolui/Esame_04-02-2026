from dataclasses import dataclass

@dataclass
class Connessioni:
    id1 : int
    id2 : int
    indice : float

    def __str__(self):
        return f'{self.id1},{self.id2},{self.indice}'

    def __eq__(self, other):
        return self.id1 == other.id1 and self.id2 == other.id2

    def __hash__(self):
        return hash(self.id1), hash(self.id2)