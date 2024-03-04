class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.id = None  # Unique id

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1 + percent_change / 100)
        else:
            self.price *= (1 - percent_change / 100)

    def print_info(self):
        print(f"Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}")
