from store import Store
from product import Product

# Create instances of Product
product1 = Product("Shirt", 20, "Clothing")
product2 = Product("Phone", 500, "Electronics")
product3 = Product("Book", 15, "Books")

# Create instance of Store
my_store = Store("My Store")

# Add products to the store
my_store.add_product(product1)
my_store.add_product(product2)
my_store.add_product(product3)

# Test sell_product method
print("Before selling:")
for i, product in enumerate(my_store.products):
    print(f"{i}: ", end="")
    product.print_info()

my_store.sell_product(1)

print("\nAfter selling:")
for i, product in enumerate(my_store.products):
    print(f"{i}: ", end="")
    product.print_info()

# Test inflation method
print("\nAfter inflation:")
my_store.inflation(10)
for product in my_store.products:
    product.print_info()

# Test set_clearance method
print("\nAfter clearance:")
my_store.set_clearance("Clothing", 20)
for product in my_store.products:
    product.print_info()
