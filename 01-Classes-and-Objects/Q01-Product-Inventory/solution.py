class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id=product_id
        self.product_name=product_name
        self.price=price
        self.quantity=quantity
    def calculate_stock_value(self):
        return self.price*self.quantity
    def display_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Price: ₹{self.price}")
        print(f"Available Quantity: {self.quantity}")
        print(f"Total Stock Value: ₹{self.calculate_stock_value()}")
product1 = Product("P101", "Rice", 60, 50)
product2 = Product("P102", "Wheat", 40, 30)
product3 = Product("P103", "Sugar", 45, 20)
print("========== PRODUCT INVENTORY ==========\n")
product1.display_details()
print("---------------------------------------")
product2.display_details()
print("---------------------------------------")
product3.display_details()


