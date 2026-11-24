class HotelBooking:
    def __init__(self, booking_id, guest_name, room_type, price_per_day, number_of_days):
        self.booking_id=booking_id
        self.guest_name=guest_name
        self.room_type=room_type
        self.price_per_day=price_per_day
        self.number_of_days=number_of_days
    def calculate_room_charges(self):
        return self.price_per_day * self.number_of_days
    def calculate_discount(self):
        if self.number_of_days >= 5:
            discount = self.calculate_room_charges()*(10/100)
            return discount
        else:
            return 0
    def calculate_final_amount(self):
        return self.calculate_room_charges() - self.calculate_discount()
    def display_booking_details(self):
        print("Booking ID: ", self.booking_id)
        print("Guest Name: ", self.guest_name)
        print("Room Type: ", self.room_type)
        print("Number of Days: ", self.number_of_days)
        print(f"\nRoom Charges: ₹{self.calculate_room_charges()}")
        print(f"Discount: ₹{self.calculate_discount()}")
        print(f"Final Amount: ₹{self.calculate_final_amount()}")
booking1=HotelBooking("B101", "Amit Sharma", "Deluxe", 3500, 4)
booking2=HotelBooking("B102", "Priya Patil", "Standard", 2000, 6)
print("========== HOTEL BOOKING SYSTEM ==========\n")
booking1.display_booking_details()
print("\n------------------------------------------\n")
booking2.display_booking_details()
