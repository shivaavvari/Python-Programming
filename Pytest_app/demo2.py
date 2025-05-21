class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self,item,quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self,item,quantity):
        if quantity >= self.items[item]:
            del self.items[item]

        else:
            self.items[item] -= quantity

    def get_item_count(self,item):
        if item in self.items:
            return self.items[item]
        else:
            return 0
        
    def get_total_items(self):
        return sum(self.items.values())
    
    def get_cart_items(self):
        return list(self.items.keys())
    
    def clear_cart(self):
        self.items = {}
