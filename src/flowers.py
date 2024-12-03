from datetime import timedelta
from seeds import Seed

class Flower:
    MAX_AGE: int = 20
    
    def __init__(self, age: int, species: str, flower_seeds: int, lifespan: int, 
                 nectar_regeneration:float, start_of_bloom: int, flower_nectar: float, occupied: bool):
        self._age = age
        self._species = species
        self._flower_seeds = flower_seeds
        self._lifespan = lifespan
        self._nectar_regeneration = nectar_regeneration
        self._start_of_bloom = start_of_bloom
        self._flower_nectar = flower_nectar
        self._occupied = occupied
        self._number_visits = 0
        
       # Age
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    # Species
    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, value: str) -> None:
        self._species = value

    # Flower Seeds
    @property
    def flower_seeds(self) -> int:
        return self._flower_seeds

    @flower_seeds.setter
    def flower_seeds(self, value: int) -> None:
        self._flower_seeds = value

    # Lifespan
    @property
    def lifespan(self) -> int:
        return self._lifespan

    @lifespan.setter
    def lifespan(self, value: int) -> None:
        self._lifespan = value

    # Nectar Regeneration
    @property
    def nectar_regeneration(self) -> float:
        return self._nectar_regeneration

    @nectar_regeneration.setter
    def nectar_regeneration(self, value: float) -> None:
        self._nectar_regeneration = value

    # Start of Bloom
    @property
    def start_of_bloom(self) -> int:
        return self._start_of_bloom

    @start_of_bloom.setter
    def start_of_bloom(self, value: int) -> None:
        self._start_of_bloom = value

    # Flower Nectar
    @property
    def flower_nectar(self) -> float:
        return self._flower_nectar

    @flower_nectar.setter
    def flower_nectar(self, value: float) -> None:
        self._flower_nectar = value

    # Occupied
    @property
    def occupied(self) -> bool:
        return self._occupied

    @occupied.setter
    def occupied(self, value: bool) -> None:
        self._occupied = value

    # number_visits
    @property
    def number_visits(self) -> int:
        return self.number_visits
    
    @occupied.setter
    def number_visits(self, value: int) -> None:
        self._number_visits += value

    def increase_visits(self):
        self._number_visits += 1

    def update_flower(self, value: int) -> int:
        self.occupied = True
        curr_flower_nectar = self._flower_nectar - value + self._nectar_regeneration
        if curr_flower_nectar > 0:
            self._flower_nectar = curr_flower_nectar
        else:
            value = self._flower_nectar
            self._flower_nectar = 0
        return value
    
    def produce_seeds(self) -> bool:
        if self._number_visits >= 3 and self._species != "Invasive Flower":
            self.number_visits = 0
            return True
        elif self._number_visits >= 2 and self._species == "Invasive Flower":
            self.number_visits = 0
            return True
        return False

    def age_flower(self) -> bool:
        """Aging the flower over time."""
        self.age += 1
        if self.age > self.MAX_AGE:
            return True  # Flower dies after reaching lifespan
        return False

        