class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.items.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        return "There is no discount to apply."

    def void_last_transaction(self):
        if len(self.items) > 0:
            last_item = self.items.pop()
            self.total -= last_item["price"] * last_item["quantity"]

    def items_in_cart(self):
        return sum(item["quantity"] for item in self.items)