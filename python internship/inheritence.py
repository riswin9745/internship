#class Animal:
 #   def __init__(self,name):
  #      self.name=name
#class Dog(Animal):
 #   def make_sound(self):
  #      return"woof"
#d1=Dog("jack")
#print(d1.name)
#print(d1.make_sound())

#class Brands:
 #   brand_name_1 ="Amazon"
  #  brand_name_2 ="Ebay"
    
#class products(Brands):
 #   prod_1 ="oline Ecommerce store"
  #  prod_2 ="online store"
    
#Obj_1 = products()
#print(Obj_1.brand_name_1+" is an "+Obj_1.prod_1)
#print(Obj_1.brand_name_2+" is an "+Obj_1.prod_2)


class Brands:
    brand_name_1 ="Amazon"
    brand_name_2 ="Ebay"
    
class products:
    prod_1 ="oline Ecommerce store"
    prod_2 ="online store"
    
class popularity(Brands,products):
    prod_1_popularity = 100
    prod_2_popularity = 70
    
Obj_1=popularity()
print(Obj_1.brand_name_1+" is an "+Obj_1.prod_1+"is",Obj_1.prod_1_popularity)
print(Obj_1.brand_name_2+" is an "+Obj_1.prod_2)



