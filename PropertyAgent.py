class PropertyAgent:
    def __init__(self, name, registration_number, company, start_year, commission_sharing_rate=0.7):
        self.name = name
        self.registration_number = registration_number
        self.company = company
        self.start_year = start_year
        self.commission_sharing_rate = commission_sharing_rate
        self.unsold_properties = []
        self.sold_properties = []

    def add_unsold_property(self, prop):
        self.unsold_properties.append(prop)

    def add_sold_property(self, prop):
        self.sold_properties.append(prop)

    def calculate_commission(self):
        total_commission = 0
        for prop in self.sold_properties:
            total_commission += prop.calculate_commission() * self.commission_sharing_rate
        return total_commission

    def __str__(self):
        return f"Agent {self.name} ({self.registration_number})"
