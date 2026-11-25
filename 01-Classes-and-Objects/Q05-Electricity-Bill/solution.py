class ElectricityBill:
    def __init__(self, consumer_number, customer_name, units_consumed):
        self.consumer_number = consumer_number
        self.customer_name = customer_name
        self.units_consumed = units_consumed
    def calculate_energy_charge(self):
        if(self.units_consumed > 0 and self.units_consumed <= 100):
            return self.units_consumed * 1.50
        elif(self.units_consumed > 100 and self.units_consumed <= 200):
            return (100 *1.50) + ((self.units_consumed - 100) * 2.50)
        else:
            return (100 * 1.50) + (100 * 2.50) + ((self.units_consumed - 200) * 4.00)
    def calculate_fixed_charge(self):
        fixed_charge=75
        return fixed_charge
    def calculate_total_bill(self):
        return self.calculate_energy_charge() + self.calculate_fixed_charge()
    def display_bill(self):
        print("Consumer Number: ", self.consumer_number)
        print("Customer Name: ", self.customer_name)
        print("Units Consumed: ", self.units_consumed)
        print("\n")
        print(f"Energy Charge: ₹{self.calculate_energy_charge()}")
        print(f"Fixed Charge: ₹{self.calculate_fixed_charge()}")
        print(f"Total Bill: ₹{self.calculate_total_bill()}")
bill1=ElectricityBill("C101", "Amit Sharma", 80)
bill2=ElectricityBill("C102", "Priya Patil", 150)
bill3=ElectricityBill("C103", "Rahul Verma", 250)
print("========== ELECTRICITY BILL SYSTEM ==========\n")
bill1.display_bill()
print("\n---------------------------------------------\n")
bill2.display_bill()
print("\n---------------------------------------------\n")
bill3.display_bill()
    