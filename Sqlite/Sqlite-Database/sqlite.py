import sqlite3
import time

class Product():

    def __int__(self,product_name,total):  #ürün ismini ve adetini aldık

        self.product_name = product_name
        self.total = total


    def __str__(self):
        return "NAME :{} TOTAL :{}".format(self.product_name,self.total)



class SuperMarket():

        def __init__(self):

            self.CreateDatabase()

        def CreateDatabase(self):

            self.db = sqlite3.connect("supermarket.db")
            self.imleç = self.db.cursor()

            x = "CREATE TABLE IF NOT EXISTS supermarket(product TEXT,total INT)"
            self.imleç.execute(x)


        def CloseDatabase(self):

            self.db.close()



        def AddProduct(self,isim,total):

            a = "insert into supermarket VALUES(?,?)"
            self.imleç.execute(a,(isim,total))
            self.db.commit()


        def ShowProducts(self):

            self.imleç.execute("Select * From supermarket")

            data = self.imleç.fetchall()

            if(len(data) ==0):
                print("Depoda ürün bulunmuyor....")
            else:
                for i in data:
                    x = i[0],i[1]
                    print(x)


        def DeleteProducts(self, ürünismi):
            self.imleç.execute("Select * From supermarket")

            data = self.imleç.fetchall()

            if (len(data) == 0):
                print("There are no products in the warehouse....")
            else:
                self.imleç.execute("delete from supermarket where product =?",(ürünismi,))
                self.db.commit()


        def IncreaseInQuantity(self,isim):   # Ürün arttırma
            self.imleç.execute("Select * from supermarket where product =? ",(isim,))

            data = self.imleç.fetchall() #Fetchall methou veritabanından bilgileri çekmeyi yarıyor.

            if (len(data) == 0):
                print("There are no products in the warehouse....")
            else:
                adet = data[0][1]
                ekleme= int(input("How much would you like to increase the number of products ?"))  #burda ne kadar artırmak istiyosak onu yazardırdık.
                adet+=ekleme

                self.imleç.execute("Update supermarket set total = ? where product =?",(adet,isim))  #burda ürünü update ettik.
                self.db.commit()







