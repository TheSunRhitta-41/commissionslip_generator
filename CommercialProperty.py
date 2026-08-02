from Property import Property


class CommercialProperty(Property):
    def __init__(self, address, postal_code, tenure, completion_year, property_type, area,
                 valuation, commercial_type, commission_rate=0.01):
        super().__init__(address, postal_code, tenure, completion_year, property_type, area, valuation, commission_rate)
        self.commercial_type = commercial_type

    def __str__(self):
        return f"{self.commercial_type} {super().__str__()}"
