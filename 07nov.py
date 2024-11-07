class Product:
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return self.name, self.weight, self.category
class Shop:

    def get_products(self):
        __file_name = 'products.txt'
        open(__file_name,"r")
        __file_name.close()
        return __file_name.read

    def add(self, *products):
        current_products = self.get_products()
        file = open(self.__file_name, "a")
        for products in products:
            if str(products) not in current_products:
                file.write(str(products) + "\n")
                current_products = str(products) + "\n"

            else:
                print(f"Продукт {products} уже есть в магазине")
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())






