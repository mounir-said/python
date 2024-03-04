class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, product_id):
        if product_id >= 0 and product_id < len(self.products):
            product = self.products.pop(product_id)
            product.print_info()
        else:
            print("Invalid product id.")

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, is_increased=True)

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, is_increased=False)
