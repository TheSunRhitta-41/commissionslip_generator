class Property:
    def __init__(self, address, postal_code, tenure, completion_year,
                 property_type, area, valuation, commission_rate=0.01):
        self.address = address
        self.postal_code = postal_code
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.valuation = valuation
        self.commission_rate = commission_rate

    def calculate_commission(self):
        return self.valuation * self.commission_rate

    def __str__(self):
        return f"{self.property_type} at {self.address} valued at ${self.valuation}"
