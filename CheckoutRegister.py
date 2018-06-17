class CheckoutRegister:
    totalCost = 0
    itemsPurchased = []
    finalList = []
    priceArray = []
    price = 0


    def __init__(self):
        totalCost = 0
        itemsPurchased = []
        finalList = []
        priceArray = []
        price = 0


    def print_receipt(self):
        print("\n***** Final Receipt *****")
        for item in self.itemsPurchased:
            print ("%s      $%s" % (item.productItemName,item.productItemCost))

        print("\nTotAmt amount remaining :    $%.2f" % self.totalCost)
        print("Amount received :            $%.2f" % self.price)
        print("Change given back :          $%.2f\n\n" % (self.price - self.totalCost))
        self.bag_products(self.itemsPurchased)


    def payBill(self,finalPrice):
        self.totalCost = finalPrice
        while self.totalCost > self.price:
            prompt = ("Payment remaining: %.2f  \nPlease enter an amount to pay: " % (self.totalCost - self.price))
            self.price = self.price + self.get_value(prompt)

    def bag_products(self,items_list):
        baggedItems = []
        nonBaggedItems = []
        BAG_WEIGHT_MAXIMUM = 5.0
        for item in items_list:
            if item.productItemWeight > BAG_WEIGHT_MAXIMUM:
                items_list.remove(item)
                nonBaggedItems.append(item)
        presentBagContents = []
        presentBagWeight = 0.0
        while len(items_list) > 0:
            temp_item = items_list[0]
            items_list.remove(temp_item)
            if presentBagWeight + temp_item.productItemWeight <= BAG_WEIGHT_MAXIMUM:
                presentBagContents.append(temp_item)
                presentBagWeight += temp_item.productItemWeight
            else:
                baggedItems.append(presentBagContents)
                presentBagContents = [temp_item]
                presentBagWeight = temp_item.productItemWeight
            if (len(items_list) == 0):
                baggedItems.append(presentBagContents)
        for index, bag in enumerate(baggedItems):
            output = 'Your Bag ' + str(index + 1) + ' consists of: '
            for product in bag:
                output += product.productItemName + '\t'
            print(output, '\n')
        if (len(nonBaggedItems) > 0):
            output = 'Non-bagged items: '
            for item in nonBaggedItems:
                output += item.productItemName + '\t'
            print(output,'\n')


    def save_product_list(self,finalProductList):
            self.finalList = finalProductList

    def accept_payment(self,amountEntered):
        self.priceArray.append(amountEntered)


    def scan_item(self,code):
            for item in self.finalList:
                if str(item.productItemCode) == str(code):
                    self.itemsPurchased.append(item)


    def get_value(self,prompt):
       amt = float(0.0)
       while True:
           try:
               amt = float(input(prompt))
               if amt < 0.0:
                   print("Don't give negative money!")
                   continue
               break
           except ValueError:
                   print('Please enter a valid amount value.')
       return amt
