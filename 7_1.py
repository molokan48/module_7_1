
class Shop:

    __file_name = "product.txt"

    def add(self , *products):
        file = open(self.__file_name , 'r')
        ret = file.read()
        file.close()

        for Product in products:
            if Product.name not in ret:
                file = open(self.__file_name , 'a')
                file.write( f' {Product} \n')
                file.close()
            else:
                print(f'Продукт {Product.name} уже есть в магазине')



    def get_products(self):
        file = open(self.__file_name , 'r')
        ret = file.read()
        file.close()
        return ret




class Product:
    def __init__(self , name , weight , category):
        if isinstance(name , str):
            self.name = name
        else:
            return TypeError

        if isinstance(weight , float):
            self.weight = weight
        else:
            return TypeError
        if isinstance(category , str):
            self.category = category
        else:
            return TypeError

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"



s1 = Shop()
p1 = Product( 'Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
#print(p1)
#print(p3)

s1.add(p1, p2, p3)

print(s1.get_products())