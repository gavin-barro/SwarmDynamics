from species import Species

class LocalSpecies(Species):
    def __init__(self, name: str, population_size: int, consumption_rate: int, growth_rate: float, resistance: float):
        super().__init__(name, population_size, consumption_rate, growth_rate)
        self.resistance = resistance  # Natural resistance factor against environmental changes or invasive species


    def update_population(self, available_resources: int):
        """
        Updates the population size with consideration of the resistance factor.
        Higher resistance may reduce the impact of invasive species or resource scarcity.
        """
        if available_resources >= self.population_size * self.consumption_rate:
            growth = int(self.population_size * self.growth_rate * self.resistance)
            self.population_size += growth
        else:
            decline = int(self.population_size * (1 - self.growth_rate * self.resistance))
            self.population_size -= decline

    def __str__(self):
        return f"Local {super().__str__()}, Resistance = {self.resistance}"

