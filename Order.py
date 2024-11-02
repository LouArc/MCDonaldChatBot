class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def add_item(self, name, price, quantity=1):
        self.items.append({
            'name': name,
            'price': price,
            'quantity': quantity
        })
        self.total_price += price * quantity

    def remove_item(self, name):
        for item in self.items:
            if item['name'] == name:
                self.total_price -= item['price'] * item['quantity']
                self.items.remove(item)
                break

    def calculate_total(self):
        return self.total_price

    def display_order(self):
        if (len(self.items) >= 1):
            for item in self.items:
                print(
                    f"{item['quantity']} x {item['name']} - ${item['price']:.2f} each")
            print(f"Total Price: ${self.calculate_total():.2f}")
        else:
            print("Todavia no has pedido nada")
