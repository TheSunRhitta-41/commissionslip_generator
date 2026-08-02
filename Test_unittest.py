import unittest
from Main import Property, CommercialProperty, PropertyAgent, PropertyAgencyDirector, CommissionSlip


class TestPropertyClasses(unittest.TestCase):
    def setUp(self):
        # Initialize test data
        self.property1 = Property("21 Egghead St", 511254, "Freehold", 2020, "Residential", 1200, 1000000)
        self.property2 = Property("26 Rouge St", 784236, "Leasehold", 2015, "Residential", 1400, 1500000)
        self.commercial_property1 = CommercialProperty("77 East Blue St", 318716, "Freehold", 2010, "Commercial", 1600,
                                                       2000000, "Office")

        self.agent1 = PropertyAgent("Erwin Smith", "AG01", "Tomorrow Hope", 2005)
        self.agent2 = PropertyAgent("Levi Ackerman", "AG02", "Tomorrow Hope", 2006)

        self.director1 = PropertyAgencyDirector("Roger King", "D0A1", "Tomorrow Hope", 2000)

    def test_property_calculate_commission(self):
        # Test Property class calculate_commission method
        self.assertEqual(self.property1.calculate_commission(), 10000)  # Assuming commission_rate is 0.01

    def test_commercial_property_inheritance(self):
        # Test if CommercialProperty inherits from Property
        self.assertTrue(issubclass(CommercialProperty, Property))

    def test_agent_add_property(self):
        # Test if PropertyAgent can add properties
        self.agent1.add_unsold_property(self.property1)
        self.assertEqual(len(self.agent1.unsold_properties), 1)

    def test_director_add_agent(self):
        # Test if PropertyAgencyDirector can add agents
        self.director1.add_agent(self.agent1)
        self.assertEqual(len(self.director1.agents), 1)

    def test_generate_commission_slip(self):
        # Test if CommissionSlip generate method runs without errors
        try:
            CommissionSlip.generate(self.agent1)
            CommissionSlip.generate(self.director1)
        except Exception as e:
            self.fail(f"CommissionSlip generate method failed with error: {e}")


if __name__ == '__main__':
    unittest.main()
