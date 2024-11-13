from pprint import pprint
class Product: # создаем класс продукты
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self): # возващаем строку с данными по продукту
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    __file_name = 'products.txt' # создает текстовый файл
    def get_products(self): # вывод, что есть в магазине (накладную - nak)
        file = open(self.__file_name, 'r')
        nak = file.read() # читаем файл, nak будет str и служебный \n не будет отображаться
        print(nak)
        file.close()
    def add(self, *products):
        file = open(self.__file_name, 'r')
        nak = file.read() # читаем файл, nak будет str
        file.close()
        sklad = nak.split('\n') # преображаем текст в список продуктов в магазине
        file = open(self.__file_name, 'a')
        for i in range(len(products)):
             if str(products[i]) in sklad: # проверяем есть то продукт в магазине
                 print(f'Продукт {products[i]} уже есть в магазине')
             else:
                 file.write(f'{products[i]}')
                 if i != len(products): # условие для перехода на следующую строку, но без создания пустой строки
                     file.write('\n')
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2.__str__())

s1.add(p1, p2, p3)

print(s1.get_products())