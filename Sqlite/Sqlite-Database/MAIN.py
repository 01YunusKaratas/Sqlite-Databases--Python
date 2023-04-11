from sqlite import *
import time



while(True):
    product = SuperMarket()
    print(""""
             WAREHOUSE INFORMATION
    ***********************************

        1- Show Products
        2- Add Product
        3- Delete Product
        4 -Increase The Number Of Products
    
    Press 'q' to exit...
    ***********************************
    """)



    choose = input("Choose: :")

    if (choose == "q"):
        print("Good a day :)")
        time.sleep(2)
        print("The application is closing...")
        time.sleep(1)
        break
    elif (choose =="1"):
        print(" ******-PRODUCT INFORMATION-******")
        product.ShowProducts()
    elif(choose=="2"):
        name = input("Product name you want to add :")
        adet = int(input("The number of products you want to add :"))
        product.AddProduct(name,adet)
    elif(choose =="3"):
        name = input("Product name you want to delete")
        sonSorgu=input("Do you wanna delete this product? :(1-YES,2-NOPE)")
        if(sonSorgu =="1"):
            product.DeleteProducts(name)
            print("Product deleted...")
        else:
            new = input("So, do you want to add a new product to the data?(1- YES,2 -NO)")
            if(new =="1"):
                name = input("Product name you want to add :")
                adet = int(input("The number of products you want to add :"))
                product.AddProduct(name,adet)
            else:
                   print("I redirect to main menu....")
    elif(choose =="4"):
        name = input("Which product would you like to increase?")
        product.IncreaseInQuantity(name)
