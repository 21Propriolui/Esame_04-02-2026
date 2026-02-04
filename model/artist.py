from dataclasses import dataclass

@dataclass
class Artist:
    id : int
    name : str
    indice : float

    def __str__(self):
        return f"{self.name} (ID: {self.id} {self.indice})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.artist_id

    def __hash__(self):
        return hash(self.id)