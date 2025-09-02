class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        """Update price by percent_change. Increase if True, decrease if False."""
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self
    
    def print_info(self):
        """Print product details"""
        print(f"Product: {self.name}, Category: {self.category}, Price: ${self.price:.2f}")
        return self


if __name__ == "__main__":
    print("Testing Product class directly...")
    p1 = Product("Laptop", 1200, "Electronics")
    p1.print_info()
    p1.update_price(0.1, True).print_info()   
    p1.update_price(0.2, False).print_info()  