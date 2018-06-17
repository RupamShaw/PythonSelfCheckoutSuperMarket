class Product:
    productItemCost = 0.0
    productItemName = ""
    productItemWeight = 0.0
    productItemCode = 00

    def __init__(self,productItemCode,productItemName,productItemWeight,productItemCost):
        self.productItemCode = productItemCode
        self.productItemName = productItemName
        self.productItemWeight = productItemWeight
        self.productItemCost = productItemCost

    def __str__(self):
        return str(self.productItemCode) + " " + str(self.productItemCost) + ", " + self.productItemName + ", " + self.productItemWeight
