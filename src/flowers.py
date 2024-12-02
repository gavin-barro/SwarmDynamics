from datetime import timedelta
from typing import List
from seeds import Seed

class Flower:
    
    def __init__(self, age: int, species: str, flower_seeds: int, lifespan: int, 
                 nectar_regeneration:float, start_of_bloom: timedelta, flower_nectar: float, occupied: bool, 
                 blocked_seeds: List[Seed]):
        self.age = age
        self.species = species
        self.flower_seeds = flower_seeds
        self.lifespan = lifespan
        self.nectar_regeneration = nectar_regeneration
        self.start_of_bloom = start_of_bloom
        self.flower_nectar = flower_nectar
        self.occupied = occupied
        self.blocked_seeds = blocked_seeds
        
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
    def start_of_bloom(self) -> timedelta:
        return self._start_of_bloom

    @start_of_bloom.setter
    def start_of_bloom(self, value: timedelta) -> None:
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

    # Blocked Seeds
    @property
    def blocked_seeds(self) -> List[seeds]:
        return self._blocked_seeds

    @blocked_seeds.setter
    def blocked_seeds(self, value: List[seeds]) -> None:
        self._blocked_seeds = value
    
        