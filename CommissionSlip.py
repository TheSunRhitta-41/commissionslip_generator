from PropertyAgencyDirector import PropertyAgencyDirector


class CommissionSlip:
    @staticmethod
    def generate(agent):
        print(f"Commission Slip for {agent}")
        print("Sold Properties:")
        for prop in agent.sold_properties:
            commission = prop.calculate_commission()
            shared_commission = commission * agent.commission_sharing_rate
            print(f"{prop}: Commission = ${commission:.2f}, Shared = ${shared_commission:.2f}")

        total_commission = agent.calculate_commission()
        print(f"Total Commission Earned: ${total_commission:.2f}")

        if isinstance(agent, PropertyAgencyDirector):
            print("\nOverriding Commission from Agents:")
            for sub_agent in agent.agents:
                overriding_commission = sub_agent.calculate_commission() * agent.overriding_commission_rate
                print(f"{sub_agent}: Overriding Commission = ${overriding_commission:.2f}")
            total_overriding_commission = agent.calculate_overriding_commission()
            print(f"Total Overriding Commission Earned: ${total_overriding_commission:.2f}")
            print(f"Total Income Earned: ${agent.calculate_total_commission():.2f}")
        print("\n")
