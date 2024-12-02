class Seed:
    
    def __init__(self, age: int, species: str, lifespan: int, start_of_bloom: int, occupied: bool,
                 nectar_regeneration: float, active: bool):
        self._age = age
        self._species = species
        self._lifespan = lifespan
        self._start_of_bloom = start_of_bloom
        self._occupied = occupied
        self._nectar_regeneration = nectar_regeneration
        self._active = active
    
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        self._age = value

    @property
    def species(self) -> str:
        return self._species

    @species.setter
    def species(self, value: str) -> None:
        self._species = value

    @property
    def lifespan(self) -> int:
        return self._lifespan

    @lifespan.setter
    def lifespan(self, value: int) -> None:
        self._lifespan = value

    @property
    def start_of_bloom(self) -> int:
        return self._start_of_bloom

    @start_of_bloom.setter
    def start_of_bloom(self, value: int) -> None:
        self._start_of_bloom = value

    @property
    def occupied(self) -> bool:
        return self._occupied

    @occupied.setter
    def occupied(self, value: bool) -> None:
        self._occupied = value

    @property
    def nectar_regeneration(self) -> float:
        return self._nectar_regeneration

    @nectar_regeneration.setter
    def nectar_regeneration(self, value: float) -> None:
        self._nectar_regeneration = value

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        self._active = value
        
        
    