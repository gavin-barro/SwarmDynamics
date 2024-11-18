from species import Species
from local_species import LocalSpecies

class InvasiveSpecies(Species):
    
    def __init__(self, name: str, population_size: int, consumption_rate: int, growth_rate: float, breeding_co: float):
        super().__init__(name, population_size, consumption_rate, growth_rate)
        self.breeding_co = breeding_co  # Rate at which the invasive species spreads, potentially affecting other species
        

    def impact_on_local_species(self, local_species: LocalSpecies):
        """
        Reduces the population of local species based on the invasive species' spread rate.
        """
        if isinstance(local_species, LocalSpecies):
            impact = int(local_species.population_size * self.spread_rate)
            local_species.population_size -= impact

    def __str__(self):
        return f"Invasive {super().__str__()}, Spread Rate = {self.spread_rate}"
