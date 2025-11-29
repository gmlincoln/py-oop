class ShoppingCart:
    
    def __init__(self, product_title, product_quantity, product_price=120, product_discount=10):
        self.title = product_title
        self.price = product_price
        self.discount = (product_discount / 100) * self.price
        self.quantity = product_quantity
    
    def addCart(self):
        total_price = (self.price - self.discount) * self.quantity        
        return f"Product Name: {self.title}, Total Price - ${total_price}K"


product_title = input("What you wanna buy? ")
product_quantity = int(input("Add quantity: "))

shuvo = ShoppingCart(product_title, product_quantity)
print(f"Shuvo: {shuvo.addCart()}")


product_title1 = input("What you wanna buy? ")
product_quantity1 = int(input("Add quantity: "))
nargis = ShoppingCart(product_title1, product_quantity1)

print(f"Nargis: {nargis.addCart()}")
