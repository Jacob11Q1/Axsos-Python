from product import Product
from store import Store

my_store = Store("SuperMart")

p1 = Product("Apple", 1.0, "Food")
p2 = Product("Shampoo", 5.5, "Cosmetics")
p3 = Product("Laptop", 1200, "Electronics")


my_store.add_product(p1).add_product(p2).add_product(p3)


print("\n--- Products in store ---")
for product in my_store.products:
    product.print_info()


print("\n--- Selling product at index 1 ---")
my_store.sell_product(1)


print("\n--- Applying 10% inflation ---")
my_store.inflation(0.1)
for product in my_store.products:
    product.print_info()


print("\n--- Applying 50% clearance on Electronics ---")
my_store.set_clearance("Electronics", 0.5)
for product in my_store.products:
    product.print_info()