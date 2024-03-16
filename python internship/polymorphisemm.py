#a = 10
#b = 20
#print('Addition of 2 numbers:',a+b)

#str1 = 'Hello '
#str2 = 'python'
#print('concatenation of 2 strings:',str1 + str2 )

#list1 = [1,2,3]
#list2 = ['A','B']
#print('concatenation of 2 lists:', list1+list2)

#class Abc:
#    x = 2+3
#    y = "Aysha "+"Amrin"
    
#obj = Abc()
#print(obj.x)
#print(obj.y)

#print(len("hellofriends"))

#print(len({"python","java","c++","c#"}))
#print(len({"Name":"Anjali","age":22,"city":"trivandram"}))

#class shape:
 #   def area(self):
  #      return 0
#class circle(shape):
#    def __init__(self,radius):
#          self.radius=radius
 #   def area(self):
  #      return 3.14 * self.radius **2
#circle=circle(radius=2)
#
# 
# print(circle.area())
    
    
class Geek:       
    def __init__(self, name, age):
        self.geekName = name
        self.geekAge  = age
           
def displayAge(self):
    print("Age:",self.geekAge)
obj = Geek("R2J",20)
print("Name:",obj.geekName)
obj.displayAge()
    