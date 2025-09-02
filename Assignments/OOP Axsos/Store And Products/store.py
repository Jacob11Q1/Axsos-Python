from product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_product(self, new_product):
        """Add product to store"""
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        """Sell (remove) product from store by index"""
        if 0 <= id < len(self.products):
            product = self.products.pop(id)
            print("Sold product:")
            product.print_info()
        else:
            print("Invalid product id")
        return self
    
    def inflation(self, percent_increase):
        """Increase price of all products"""
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    
    def set_clearance(self, category, percent_discount):
        """Apply discount to all products in a category"""
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self


if __name__ == "__main__":
    print("Testing Store class directly...")
    store = Store("Tech Shop")
    p1 = Product("Laptop", 1200, "Electronics")
    p2 = Product("Phone", 800, "Electronics")
    store.add_product(p1).add_product(p2)
    store.inflation(0.1)
    for p in store.products:
        p.print_info()