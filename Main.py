from CommercialProperty import CommercialProperty
from CommissionSlip import CommissionSlip
from Property import Property
from PropertyAgencyDirector import PropertyAgencyDirector
from PropertyAgent import PropertyAgent


def main():
    # Create properties
    property1 = Property("21 Egghead St", 511254, "Freehold", 2020, "Residential", 1200, 1000000)
    property2 = Property("26 Rouge St", 784236, "Leasehold", 2015, "Residential", 1400, 1500000)
    property3 = CommercialProperty("77 East Blue St", 318716, "Freehold", 2010, "Commercial", 1600, 2000000, "Office")
    property4 = CommercialProperty("88 North Blue St", 777777, "Leasehold", 2010, "Commercial", 1800, 2500000,
                                   "Factory")
    property5 = Property("73 Sky Island St", 355488, "Freehold", 2012, "Residential", 1000, 700000)
    property6 = Property("47 Good Lane St", 355488, "Freehold", 2012, "Residential", 1000, 700000)
    property7 = Property("93 Calm Belt", 521356, "Leasehold", 2018, "Residential", 1600, 1200000)
    property8 = Property("10 Merry St", 674123, "Freehold", 2015, "Residential", 1800, 1800000)
    property9 = CommercialProperty("55 Sunny St", 789012, "Freehold", 2013, "Commercial", 2000, 3000000, "Office")
    property10 = CommercialProperty("42 Elbaf St", 891234, "Leasehold", 2016, "Commercial", 2200, 3500000, "Factory")
    property11 = Property("15 God Valley St", 921346, "Freehold", 2019, "Residential", 1500, 1600000)
    property12 = Property("38 Alasbata St", 863412, "Leasehold", 2017, "Residential", 1700, 2200000)
    property13 = Property("39 Whole cake St", 245631, "Freehold", 2018, "Residential", 1400, 1900000)
    property14 = Property("27 Moby Dick St", 875421, "Leasehold", 2016, "Residential", 1600, 1400000)
    property15 = Property("81 Yoru St", 325896, "Freehold", 2014, "Residential", 1800, 2100000)
    property16 = CommercialProperty("23 Gryphon St", 654789, "Freehold", 2015, "Commercial", 2000, 2800000, "Office")
    property17 = CommercialProperty("54 Ace St", 987654, "Leasehold", 2019, "Commercial", 2200, 3200000, "Factory")
    property18 = Property("60 Murakumogiri St", 123987, "Freehold", 2013, "Residential", 1400, 1700000)
    property19 = Property("35 Heaven St", 456123, "Leasehold", 2017, "Residential", 1600, 2000000)
    property20 = Property("48 Enma St", 789456, "Freehold", 2016, "Residential", 1800, 2300000)

    # Create agents
    agent1 = PropertyAgent("Erwin Smith", "AG01", "Tomorrow Hope", 2005)
    agent2 = PropertyAgent("Levi Ackerman", "AG02", "Tomorrow Hope", 2006)
    agent3 = PropertyAgent("Kenny Ackerman", "AG03", "Tomorrow Hope", 2007)
    agent4 = PropertyAgent("Mikasa Ackerman", "AG04", "Tomorrow Hope", 2008)
    agent5 = PropertyAgent("Armin Arlert", "AG05", "Tomorrow Hope", 2009)
    agent6 = PropertyAgent("Sasha Blouse", "AG06", "Tomorrow Hope", 2010)

    # Assign properties to agents
    agent1.add_unsold_property(property1)
    agent1.add_unsold_property(property2)
    agent1.add_sold_property(property3)
    agent1.add_sold_property(property4)
    agent1.add_sold_property(property5)

    agent2.add_unsold_property(property3)
    agent2.add_unsold_property(property4)
    agent2.add_sold_property(property1)
    agent2.add_sold_property(property2)
    agent2.add_sold_property(property6)

    agent3.add_unsold_property(property5)
    agent3.add_unsold_property(property1)
    agent3.add_sold_property(property7)
    agent3.add_sold_property(property8)
    agent3.add_sold_property(property9)

    agent4.add_unsold_property(property6)
    agent4.add_unsold_property(property7)
    agent4.add_sold_property(property10)
    agent4.add_sold_property(property11)
    agent4.add_sold_property(property12)

    agent5.add_unsold_property(property8)
    agent5.add_unsold_property(property9)
    agent5.add_sold_property(property13)
    agent5.add_sold_property(property14)
    agent5.add_sold_property(property15)

    agent6.add_unsold_property(property10)
    agent6.add_unsold_property(property11)
    agent6.add_sold_property(property16)
    agent6.add_sold_property(property17)
    agent6.add_sold_property(property18)

    # Create directors
    director1 = PropertyAgencyDirector("Roger King", "D0A1", "Tomorrow Hope", 2000)
    director2 = PropertyAgencyDirector("Edward Strongman", "D0A2", "Tomorrow Hope", 2000)

    # Assign properties to directors
    director1.add_sold_property(property19)  # Director sells a property

    director2.add_sold_property(property20)  # Director sells a property

    # Assign agents to directors
    director1.add_agent(agent1)
    director1.add_agent(agent2)
    director1.add_agent(agent3)

    director2.add_agent(agent4)
    director2.add_agent(agent5)
    director2.add_agent(agent6)

    # Generate commission slips
    CommissionSlip.generate(agent1)
    CommissionSlip.generate(agent2)
    CommissionSlip.generate(agent3)
    CommissionSlip.generate(agent4)
    CommissionSlip.generate(agent5)
    CommissionSlip.generate(agent6)
    CommissionSlip.generate(director1)
    CommissionSlip.generate(director2)


if __name__ == "__main__":
    main()
