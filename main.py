from Product import Product
from CheckoutRegister import CheckoutRegister

def construct_product_items(productItemsArrayList):
    productItemsArrayList.append(Product(501,"Chocolate",1,100))
    productItemsArrayList.append(Product(502,"PopCorn",1,45))
    productItemsArrayList.append(Product(503,"Biscuit",2,18))
    productItemsArrayList.append(Product(504,"FaceWash",1,180))
    productItemsArrayList.append(Product(505,"Oil",6,30))
    productItemsArrayList.append(Product(506,"Soup, 2 Packets",2,50))
    productItemsArrayList.append(Product(508,"Pillow Cover",1,300))
    productItemsArrayList.append(Product(507,"Mango, 3 Pieces",3,90))
    productItemsArrayList.append(Product(509,"Pen Stand",1,50))
    productItemsArrayList.append(Product(510,"Milk, 2 Litres",2,2.0))


print("***** Welcome to JAGDIV Store checkout! *****")
input1 = "N"
input2 = "Y"
productItems = []

construct_product_items(productItems)

while (input1 != "Q"):
    regsisterObject = CheckoutRegister()
    input2 = "Y"
    totalCost = 0
    regsisterObject.save_product_list(productItems)
    while (input2 == "Y"):
        enteredCode = input("Enter the Code of your product : ")
        matchedItem = 0;
        for itemInstance in productItems:
            if str(itemInstance.productItemCode) == str(enteredCode):
                matchedItem = 1
                break
        if matchedItem == 0:
            print("Entered Product does not exist in our store!!!")
        else:
            print("%s - $%s" % (str(itemInstance.productItemName),str(itemInstance.productItemCost)))
            totalCost = totalCost + itemInstance.productItemCost
            regsisterObject.scan_item(enteredCode)
            input2 = input("Do you want to scan more products ? (Y/N) ")

    regsisterObject.payBill(totalCost)
    regsisterObject.print_receipt()
    print("***** We Thank you for shopping at JAGDIV Store! *****")
    input1 = input("(N)ext customer, or (Q)uit ? ")
