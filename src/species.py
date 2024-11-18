class Species:
    def __init__(self, name: str, population_size: int, consumption_rate: int, growth_rate: float):
        self.name = name
        self.population_size = population_size
        self.consumption_rate = consumption_rate  # Resources consumed per individual per time step
        self.growth_rate = growth_rate            # Growth rate of the population per time step


    def update_population(self, available_resources: int):
        """
        Updates the population size based on resource availability.
        If resources are sufficient, the population grows; otherwise, it declines.
        """
        if available_resources >= self.population_size * self.consumption_rate:
            # Population grows if enough resources are available
            growth = int(self.population_size * self.growth_rate)
            self.population_size += growth
        else:
            # Population declines if resources are insufficient
            decline = int(self.population_size * (1 - self.growth_rate))
            self.population_size -= decline

    def __str__(self):
        return f"{self.name}: Population = {self.population_size}, Growth Rate = {self.growth_rate}, Consumption Rate = {self.consumption_rate}"
