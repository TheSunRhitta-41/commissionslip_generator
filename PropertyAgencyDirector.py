from PropertyAgent import PropertyAgent


class PropertyAgencyDirector(PropertyAgent):
    def __init__(self, name, registration_number, company, start_year,
                 commission_sharing_rate=0.75, overriding_commission_rate=0.05):
        super().__init__(name, registration_number, company, start_year, commission_sharing_rate)
        self.overriding_commission_rate = overriding_commission_rate
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def calculate_overriding_commission(self):
        total_overriding_commission = 0
        for agent in self.agents:
            total_overriding_commission += agent.calculate_commission() * self.overriding_commission_rate
        return total_overriding_commission

    def calculate_total_commission(self):
        return self.calculate_commission() + self.calculate_overriding_commission()

    def __str__(self):
        return f"Director {self.name} ({self.registration_number})"
